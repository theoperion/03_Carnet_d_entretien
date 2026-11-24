#!/usr/bin/env python3
"""Fabrique une COPIE FIGÉE de l'appli pour un carnet remis à quelqu'un (règle de Théo : après la remise, plus aucune
mise à jour). La copie vit dans fige/<dossier>/ et ne sera plus jamais modifiée une fois « definitif » à True.

    python3 outils/figer.py <nom>     → (re)fabrique une copie fige/<nom>/ (aucune pour l'instant)
    python3 outils/figer.py commun ../mon_carnet → (re)fabrique la version commune dans le dépôt privé Mon_Carnet
                                       (servi par Cloudflare Pages, comme Mon_Budget) : pas de carnet par défaut,
                                       chacun colle le lien de SON carnet puis sa clé.
    python3 outils/figer.py --verifier → échoue si une copie définitive a été modifiée

Ce que la copie a de différent : son carnet par défaut (celui de la personne), ses données du téléphone à part
(préfixe cf-<dossier>.), son propre hors connexion (cache carnet-fige-<dossier>-…), son propre nom d'appli.
Aucun prénom ici (dépôt public) : les dossiers ont un nom neutre (t4…)."""
import hashlib, json, os, re, shutil, sys

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
FIGES = {
    # Version commune (dépôt privé Mon_Carnet, Cloudflare Pages) pour toutes les personnes à qui Théo transfère un Sheet.
    "commun": {"id": None, "nom": "Mon carnet", "court": "", "definitif": False, "externe": True},
    # (24/11) l'ancienne copie fige/t4/ est remplacée par la version commune ci-dessus (https://mon-carnet-cs7.pages.dev/).
}
FICHIERS = ["index.html", "sw.js", "version.js", "manifest.json", "icon-192.png", "icon-512.png", "icon-maskable-512.png"]

def lire(f): return open(os.path.join(RACINE, f), encoding="utf-8").read()
def empreinte(d):   # noms ET contenus des fichiers : un fichier renommé, ajouté ou retiré change aussi l'empreinte
    return hashlib.sha256(b"".join(f.encode() + b"\0" + open(os.path.join(d, f), "rb").read() for f in sorted(os.listdir(d)) if f != "EMPREINTE" and not f.startswith(".") and os.path.isfile(os.path.join(d, f)))).hexdigest()

def fabriquer(nom, c, sortie=None):
    if c.get("externe") and not sortie: sys.exit(f"✗ {nom} se fabrique dans son propre dépôt : python3 outils/figer.py {nom} <dossier du dépôt>")
    dest = os.path.abspath(sortie) if sortie else os.path.join(RACINE, "fige", nom)
    if c["definitif"] and os.path.exists(dest): sys.exit(f"✗ fige/{nom} est définitive : on n'y touche plus (règle de Théo).")
    os.makedirs(dest, exist_ok=True)
    for f in FICHIERS:
        if f.endswith(".png"): shutil.copyfile(os.path.join(RACINE, f), os.path.join(dest, f))
    def remp(s, a, b, n=1):
        assert s.count(a) == n, (a[:60], s.count(a)); return s.replace(a, b)
    h = lire("index.html")
    h = remp(h, "const FIGE = null;", "const FIGE = " + json.dumps({"dossier": nom, "id": c["id"], "nom": c["nom"]}, ensure_ascii=False) + ";   // COPIE FIGÉE (outils/figer.py) : ne pas modifier")
    h = remp(h, "localStorage.getItem('carnet.theme')", f"localStorage.getItem('cf-{nom}.theme')")
    titre = f"Carnet {c['court']}" if c["court"] else c["nom"]
    h = remp(h, "<title>Carnet T3</title>", f"<title>{titre}</title>")
    h = remp(h, '<h1 id="htitle">Carnet · T3</h1>', f'<h1 id="htitle">{c["nom"]}</h1>')
    open(os.path.join(dest, "index.html"), "w", encoding="utf-8").write(h)
    w = lire("sw.js")
    w = remp(w, "'carnet-t3-'", f"'carnet-fige-{nom}-'", 2)
    w = remp(w, "  if (u.pathname.includes('/fige/')) return;   // 1.9.2 : les copies figées (fige/…) ont leur propre hors connexion\n", "")
    open(os.path.join(dest, "sw.js"), "w", encoding="utf-8").write(w)
    shutil.copyfile(os.path.join(RACINE, "version.js"), os.path.join(dest, "version.js"))
    m = json.loads(lire("manifest.json"))
    m.update({"name": f"Carnet d'entretien · {c['court']}" if c["court"] else "Mon carnet d'entretien", "short_name": titre, "description": "Entretien et historique du logement"})
    json.dump(m, open(os.path.join(dest, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    if c.get("externe"):
        version0 = re.search(r'app: "([^"]+)"', lire("version.js")).group(1)
        open(os.path.join(dest, "README.md"), "w", encoding="utf-8").write(f"""# Mon carnet d'entretien (version commune)

Appli de carnet d'entretien (PWA) pour toute personne qui a son propre fichier Google « carnet d'entretien » et son script.
Servie par Cloudflare Pages depuis ce dépôt privé : https://mon-carnet-cs7.pages.dev/

- Au premier lancement, l'appli demande le **lien de ton carnet** (reçu par message), puis ta **clé**. Ils restent sur ton téléphone.
- **Tes données sont dans ton fichier Google**, jamais ici : ce dépôt ne contient que le programme.
- Version **figée** (appli {version0}) : elle ne change pas toute seule. Fabriquée depuis l'appli de Théo par `outils/figer.py commun`
  (dépôt 03_Carnet_d_entretien). Ne rien modifier ici à la main (fichier EMPREINTE).
""")
    open(os.path.join(dest, "EMPREINTE"), "w").write(empreinte(dest) + "\n")
    version = re.search(r'app: "([^"]+)"', lire("version.js")).group(1)   # hors de la f-string : marche aussi avec Python < 3.12
    print(f"→ {os.path.relpath(dest, RACINE)}/ fabriquée (appli {version})" + (" · DÉFINITIVE" if c["definitif"] else ""))

if sys.argv[1:] == ["--verifier"]:
    ko = 0
    for nom, c in FIGES.items():
        if c.get("externe"): continue   # vérifiée dans son propre dépôt
        d = os.path.join(RACINE, "fige", nom)
        if not os.path.exists(d):
            if c["definitif"]: print(f"✗ fige/{nom} est définitive mais a disparu"); ko = 1
            continue
        if open(os.path.join(d, "EMPREINTE")).read().strip() != empreinte(d): print(f"✗ fige/{nom} a été modifiée à la main"); ko = 1
    sys.exit(ko)
if len(sys.argv) not in (2, 3) or sys.argv[1] not in FIGES: sys.exit(__doc__)
fabriquer(sys.argv[1], FIGES[sys.argv[1]], sys.argv[2] if len(sys.argv) == 3 else None)
