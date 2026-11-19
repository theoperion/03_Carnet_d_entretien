# Carnet T3 (carnet d'entretien + inventaire de l'appartement) — passation pour Claude

À lire avant toute action, puis lire **`MODE_EMPLOI.md`** (le seul document de suivi : feuille de route, règles, journal).
Ce fichier remplace la mémoire des conversations précédentes (jusqu'au 18/11/2026).

## Qui, comment
- **Théo** (GitHub `theoperion`), francophone : répondre **en français**, simplement, sans jargon.
- **Méthode** : Claude propose une étape → Théo valide (« OK étape X ») → Claude fait, teste, met en ligne
  (ligne dans le journal de `MODE_EMPLOI.md`) → Théo vérifie → on coche. Claude peut publier directement sur `main`.
- Objectif fixé par Théo : corriger et améliorer **sans chambouler une appli qui marche** (export compris).

## Façon de travailler avec Théo (demandée par Théo le 19/11/2026, valable pour TOUTES les conversations)
- **Être force de proposition** : à chaque échange, proposer de soi-même des idées, des améliorations et des pistes originales, pas seulement exécuter ce qui est demandé.
- **Être innovant et ambitieux** (« pousser l'IA et le code dans leurs retranchements ») et **challenger Théo** : donner un avis franc, dire quand une idée peut être meilleure, proposer une alternative.
- **Travailler ensemble** : Claude propose → Théo choisit et valide → Claude construit. Après chaque étape, relancer avec la suite et 2 ou 3 idées nouvelles.

## Où est quoi
- Appli téléphone : ce dépôt (GitHub Pages, **public**) : `index.html` (tout le code), `sw.js` (hors connexion),
  `manifest.json`, icônes. **Version** : `version.js` (`app` + `date`), seul endroit à changer à chaque mise en ligne.
- Script Google (API, mails d'échéance, export PDF) : dépôt **privé** `theoperion/app_scripts`, dossier `carnet-t3/`
  (`Code.js`, `Export.js`, `Video.js`). Audit de référence : `app_scripts/audits/carnet-t3-2026-11.md`.
- Données : Google Sheet « Appartement T3 · Carnet & inventaire » (sur le compte Google de Théo).

## Mettre le script en ligne (sans changer d'adresse)
- Une fois par machine : `npx -y @google/clasp@3.4.1 login` (compte Google de Théo ; rien de secret dans GitHub).
- Dans `app_scripts/carnet-t3` : `clasp push --force` puis `python3 ../outils/deployer.py "Carnet 1.x : ce qui change"`.
- **Jamais « Nouveau déploiement »** dans l'éditeur Apps Script (créerait une nouvelle adresse) ; jamais de copier-coller dans l'éditeur.
- `app_scripts` est partagé avec d'autres conversations : `git pull --rebase` avant de pousser.

## Règles
- **Mails d'échéance : un seul par tâche et par échéance, jamais de relance** (la tâche reste dans l'appli jusqu'à « FAIT »).
- Aucun identifiant / jeton / adresse e-mail dans ce dépôt public.
- Le hors connexion ne doit effacer que ses propres caches (Versus et le carnet de Carla sont sur le même domaine).
- Bouton retour du téléphone (1.8.5) : ferme la fenêtre ouverte, puis revient au tableau de bord, puis quitte. Validé, ne pas casser.
- Tester avant de publier : `python3 -m http.server` + Playwright (Chromium), avec un **faux serveur** (intercepter
  `https://script.google.com/**`), jamais les vraies données ; Théo utilise Firefox Android, ça doit aussi marcher sur Chrome et iPhone.

## État au 18/11/2026
Appli 1.8.5, Export 2.5. Tout l'audit de novembre est corrigé (voir `MODE_EMPLOI.md`). Pas de chantier en cours :
demander à Théo ce qu'il veut faire ensuite.
