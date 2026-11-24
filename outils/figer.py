#!/usr/bin/env python3
"""Fabrique une COPIE FIGÉE de l'appli pour un carnet remis à quelqu'un (règle de Théo : après la remise, plus aucune
mise à jour). La copie vit dans fige/<dossier>/ et ne sera plus jamais modifiée une fois « definitif » à True.

    python3 outils/figer.py t4        → (re)fabrique fige/t4/ à partir de l'appli actuelle
    python3 outils/figer.py --verifier → échoue si une copie définitive a été modifiée

Ce que la copie a de différent : son carnet par défaut (celui de la personne), ses données du téléphone à part
(préfixe cf-<dossier>.), son propre hors connexion (cache carnet-fige-<dossier>-…), son propre nom d'appli.
Aucun prénom ici (dépôt public) : les dossiers ont un nom neutre (t4…)."""
import hashlib, json, os, re, shutil, sys

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
FIGES = {
    # T4 : remis à sa propriétaire au transfert. Passer definitif à True LE JOUR DU TRANSFERT (plus aucune modification ensuite).
    "t4": {"id": "AKfycbysEJTeMDjtS2WHicGgse_l9PJ0h6NL7mYTExIOTW1_aHGp31UzkBzhhTmnsFg1NXsy", "nom": "Carnet · T4", "court": "T4", "definitif": False},
}
FICHIERS = ["index.html", "sw.js", "version.js", "manifest.json", "icon-192.png", "icon-512.png", "icon-maskable-512.png"]

def lire(f): return open(os.path.join(RACINE, f), encoding="utf-8").read()
def empreinte(d): return hashlib.sha256(b"".join(open(os.path.join(d, f), "rb").read() for f in sorted(os.listdir(d)) if f != "EMPREINTE")).hexdigest()

def fabriquer(nom, c):
    dest = os.path.join(RACINE, "fige", nom)
    if c["definitif"] and os.path.exists(dest): sys.exit(f"✗ fige/{nom} est définitive : on n'y touche plus (règle de Théo).")
    os.makedirs(dest, exist_ok=True)
    for f in FICHIERS:
        if f.endswith(".png"): shutil.copyfile(os.path.join(RACINE, f), os.path.join(dest, f))
    def remp(s, a, b, n=1):
        assert s.count(a) == n, (a[:60], s.count(a)); return s.replace(a, b)
    h = lire("index.html")
    h = remp(h, "const FIGE = null;", "const FIGE = " + json.dumps({"dossier": nom, "id": c["id"], "nom": c["nom"]}, ensure_ascii=False) + ";   // COPIE FIGÉE (outils/figer.py) : ne pas modifier")
    h = remp(h, "localStorage.getItem('carnet.theme')", f"localStorage.getItem('cf-{nom}.theme')")
    h = remp(h, "<title>Carnet T3</title>", f"<title>Carnet {c['court']}</title>")
    h = remp(h, '<h1 id="htitle">Carnet · T3</h1>', f'<h1 id="htitle">{c["nom"]}</h1>')
    open(os.path.join(dest, "index.html"), "w", encoding="utf-8").write(h)
    w = lire("sw.js")
    w = remp(w, "'carnet-t3-'", f"'carnet-fige-{nom}-'", 2)
    w = remp(w, "  if (u.pathname.includes('/fige/')) return;   // 1.9.2 : les copies figées (fige/…) ont leur propre hors connexion\n", "")
    open(os.path.join(dest, "sw.js"), "w", encoding="utf-8").write(w)
    shutil.copyfile(os.path.join(RACINE, "version.js"), os.path.join(dest, "version.js"))
    m = json.loads(lire("manifest.json"))
    m.update({"name": f"Carnet d'entretien · {c['court']}", "short_name": f"Carnet {c['court']}", "description": "Entretien et historique du logement"})
    json.dump(m, open(os.path.join(dest, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(os.path.join(dest, "EMPREINTE"), "w").write(empreinte(dest) + "\n")
    print(f"→ fige/{nom}/ fabriquée (appli {re.search(r'app: \"([^\"]+)\"', lire('version.js')).group(1)}){' · DÉFINITIVE' if c['definitif'] else ''}")

if sys.argv[1:] == ["--verifier"]:
    ko = 0
    for nom, c in FIGES.items():
        d = os.path.join(RACINE, "fige", nom)
        if not os.path.exists(d): continue
        if open(os.path.join(d, "EMPREINTE")).read().strip() != empreinte(d): print(f"✗ fige/{nom} a été modifiée à la main"); ko = 1
    sys.exit(ko)
if len(sys.argv) != 2 or sys.argv[1] not in FIGES: sys.exit(__doc__)
fabriquer(sys.argv[1], FIGES[sys.argv[1]])
