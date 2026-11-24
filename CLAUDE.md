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
- **En ligne** : appli 1.8.7 (« Comment ça marche » complet). Script en ligne : 1.8.2.
- **Prêt, pas encore en ligne** : script **1.9** dans `app_scripts/carnet-t3/Code.js` (adresse du Sheet après la clé, mails de garantie par nom + date, page « Installer mon carnet », `serveur.nom`). À envoyer **depuis un ordinateur** (`clasp push --force` + `deployer.py`) ; Théo n'a pas d'ordinateur pour l'instant. En attendant : bouton « Ouvrir le Sheet » masqué.
- **En cours** : appli **1.9** « plusieurs carnets » (lien `#s=`, données séparées par carnet, partager le lien) sur la branche `claude/hopeful-galileo-265cjb`, **pas sur main**. Relue par carnet-utilisateur (8 retouches, dont 1 bloquante iPhone) et carnet-code (sécurité : un carnet étranger peut lire la clé du carnet principal → à corriger avant de publier) : liste dans `app_scripts/carnet-t3/IDEES.md` (plan 1.9). Corriger, re-tester (`multi.js` : une saisie ne doit jamais partir vers un autre carnet), puis publier sur main.
- **Ensuite** : un 3e carnet (script à copier du T3, son propre Sheet ; détails privés dans `app_scripts/carnet-t3/IDEES.md`, nécessite un ordinateur), modules par carnet (étape 4), le carnet T4 sur l'appli commune.
- L'appli de Carla (dépôt 07) range ses données sous `carnetT4.` : pas de collision avec `carnet.`.
