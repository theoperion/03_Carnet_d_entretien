# Carnet T3 — carnet d'entretien et inventaire de l'appartement

Appli de Théo pour suivre l'entretien de son T3 (échéances, passages, mail d'échéance) et l'inventaire des biens (garanties, plafond MAIF, photos, consommables, jeux de société), avec un petit jeu de motivation (aquarium, trophées, séries, vacances). En ligne : https://theoperion.github.io/03_Carnet_d_entretien/

**Ce dépôt est public.** Les agents et les idées sont dans le dépôt **privé** `app_scripts` (`.claude/agents/carnet-*.md`, `carnet-t3/IDEES.md`). Anciennes fiches : `archives/`. Journal des versions : `MODE_EMPLOI.md`.

## Règles de travail
- Tout en français, simplement. Claude propose → Théo valide (« OK … ») → Claude fait, teste, met en ligne, ajoute une ligne au journal → Théo vérifie.
- Objectif : améliorer **sans chambouler une appli qui marche** (export compris).
- Aucun identifiant, jeton, adresse e-mail ni ID de Sheet/Drive dans ce dépôt (l'adresse du script dans `index.html` est publique par nature).

## Où est quoi
- Appli (GitHub Pages) : `index.html` (tout le code, mode d'emploi intégré `ouvrirAide`), `sw.js` (hors connexion), `manifest.json`, icônes.
- **Version** : `version.js` (`app` + `date`), seul endroit à changer à chaque mise en ligne (renouvelle aussi le cache).
- Script Google (API, mails, export PDF) : `app_scripts/carnet-t3/` (`Code.js`, `Export.js`, `Video.js`).
- Données : Google Sheet « Appartement T3 · Carnet & inventaire » (Entretien, Historique, Inventaire, Contacts, Jeux de société, Consommables…).

## Mettre en ligne
- **Appli** : changer `version.js`, publier sur `main` (autorisé par Théo le 05/11/2026), dire ce qui est publié.
- **Script** (même adresse) : une fois par machine `npx -y @google/clasp@3.4.1 login` (compte de Théo) ; dans `app_scripts/carnet-t3` : `clasp push --force` puis `python3 ../outils/deployer.py "Carnet 1.x : ce qui change"`. **Jamais « Nouveau déploiement »**, jamais de copier-coller dans l'éditeur. `git pull --rebase` avant de pousser `app_scripts` (partagé).

## Règles à ne pas casser
- **Mail d'échéance : un seul par tâche et par échéance, jamais de relance** (la tâche reste dans l'appli jusqu'à « FAIT ») ; garanties et plafond MAIF : une fois aussi ; le mail de test ne touche à rien.
- **File hors connexion** (1.8) : aucune saisie perdue ni doublée (identifiant par envoi, fusion créer/modifier, délai 30 s, erreur passagère = réessai).
- Le hors connexion n'efface que ses caches `carnet-t3-…` (Versus et le carnet de Carla sont sur le même domaine).
- Bouton retour du téléphone : ferme la fenêtre ouverte → tableau de bord → quitte.
- Tester avant de publier : `python3 -m http.server` + Playwright (Chromium) avec un **faux serveur** (intercepter `https://script.google.com/**`), jamais les vraies données. Théo est sur Firefox Android ; ça doit aussi marcher sur Chrome et iPhone.

## Agents (dans `app_scripts/.claude/agents/`, lecture seule)
4 agents, chacun répond ✅ / ⚠ / « non concerné » avec preuve : **`carnet-syndic`** (expert du logement : échéances, mails, inventaire, jeu de motivation) · **`carnet-code`** (file hors connexion, version, caches, appli ↔ script, sécurité, export) · **`carnet-utilisateur`** (Théo sur son téléphone, captures à 390 px) · **`carnet-avocat`** (gros changement ou nouvelle idée).
Qui relit quoi : texte ou petit affichage → personne ; nouvel écran/geste → utilisateur ; calcul, échéance, mail → syndic + code ; données, envois, mise en ligne du script → code ; gros changement → les 4. À chaque version, dire à Théo quels agents ont relu et pourquoi.

## État au 24/11/2026 (point de reprise de la conversation « Perso · Carnet »)
- **En ligne** : appli **1.9.1** « plusieurs carnets » (lien `#s=`, données séparées par carnet, « Partage et autres carnets » dans Réglages, « Ouvrir ce carnet ? », données étrangères filtrées) + modules par carnet (`mod()`, T4 deviné par son adresse, sinon `serveur.modules`) + carnet d'essai sans script (`#s=carnet_essai_exemple_2026`) ; 1.9.3 : **version commune** pour les carnets transférés, dépôt privé `Mon_Carnet` servi par Cloudflare Pages, fabriquée par `python3 outils/figer.py commun ../mon_carnet` (même copie pour tous, contenu selon le carnet) ; 1.9.2 : **copies figées** `fige/<dossier>/` (`outils/figer.py`, ex. `fige/t4/`) pour les carnets remis, qui ne reçoivent plus aucune mise à jour (règle de Théo) : ne jamais retoucher une copie « definitif ». Script en ligne : 1.8.2.
- **Prêt, pas encore en ligne** : script **2.0** (code commun `app_scripts/carnet-commun/` + `Reglages.js` par carnet, marche à suivre dans `app_scripts/carnet-t3/IDEES.md` : T3 d'abord, T4 avant le transfert ; contient tout le script **1.9** : adresse du Sheet après la clé, mails de garantie par nom + date, page « Installer mon carnet », `serveur.nom`). **Publier l'appli avant le script T4** (ses mails mènent à `fige/t4/`). À envoyer **depuis un ordinateur** (`clasp push --force` + `deployer.py`), puis ouvrir l'adresse du script et vérifier que l'id après `#s=` est celui d'`API_URL`. En attendant : bouton « Ouvrir le Sheet » masqué, nom du carnet = « Carnet · T3 » par défaut.
- **Ensuite** : un 3e carnet (script à copier du T3, son propre Sheet ; détails privés dans `app_scripts/carnet-t3/IDEES.md`, nécessite un ordinateur), passer Carla sur l'appli commune (puis archiver le dépôt 07). Retouches « plus tard » des agents : `app_scripts/carnet-t3/IDEES.md`.
- L'appli de Carla (dépôt 07) range ses données sous `carnetT4.` : pas de collision avec `carnet.`.
