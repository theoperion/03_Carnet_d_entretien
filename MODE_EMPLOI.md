# Carnet T3 · Mode d'emploi

> **Le seul document à suivre** pour l'appli du carnet d'entretien et de l'inventaire de l'appartement.
> Même méthode que Versus : Claude propose une étape → tu valides (« OK étape X ») → Claude fait, teste, met en ligne → tu vérifies → on coche.
> Dernière mise à jour : 05/11/2026

## 1. Ce que c'est

| Morceau | Où |
|---|---|
| Appli téléphone | ce dépôt (GitHub Pages, public) : `index.html`, `sw.js`, `manifest.json`, icônes |
| Script Google (API) | dépôt privé `theoperion/app_scripts`, dossier `carnet-t3/` (Code, Export, Video) |
| Données | Google Sheet « Appartement T3 · Carnet & inventaire » : Tableau de bord, Entretien, Historique, Consommables, Inventaire, Jeux de société, Achats Amazon, Contacts, Stats achats |

**Mise en ligne** : Claude publie sur `main` chaque étape validée, en disant ce qu'il publie (autorisé par Théo le 05/11/2026). E-mails d'échéance : envoyés par un réveil du script, indépendant de l'adresse ; **un seul mail par tâche et par échéance, jamais de relance** (la tâche reste dans l'appli jusqu'à « FAIT ») ; garanties et plafond : une fois aussi ; état visible dans l'appli (« Mail d'échéance : ✅ actif »).

**Les 3 interdits** : plus de copier-coller dans l'éditeur Apps Script ; plus jamais « Nouveau déploiement » (une seule adresse) ; rien sans étape validée ici.

## 2. Adresse officielle du script

| Script | Adresse officielle | Anciennes adresses |
|---|---|---|
| Carnet T3 | `…wsDzmjF3…`, inscrite dans l'appli | ✅ les 7 anciennes servent le même code (marquées « ancienne adresse ») |

## 3. Feuille de route

Légende : ⬜ à faire · 🟡 proposé · 🔧 en cours · ✅ fait et vérifié

### Phase 0 · Remettre de l'ordre
- ✅ 0.1 Code du script récupéré dans `app_scripts/carnet-t3` (identique à la version en ligne n°14)
- ✅ 0.2 Audit complet → checklist : `app_scripts/audits/carnet-t3-2026-11.md` (objectif : corriger les bugs sans chambouler l'appli)
- ✅ 0.3 Une seule adresse : les 7 anciennes adresses servent le même code
- ✅ B1 Lien de l'appli dans les e-mails corrigé (`03_Carnet_d_entretien`) · script version Google 15
- ✅ Étape 1 · **File d'attente hors connexion fiable** (appli 1.8) : une erreur n'efface plus les autres saisies (erreur passagère = réessai, refus = seule cette saisie est retirée, avec message) ; identifiant unique par envoi → plus de doublon après une coupure ; créé puis modifié = une seule écriture ; supprimé avant l'envoi = rien ne part ; les lignes suivent après une suppression ; délai maximal 30 s ; ressaisir la clé ne vide plus la file ; plus de passage « fantôme ». Testé avec un faux serveur.
- ✅ Étape 2 · **Autres bugs** : mise à jour fiable (`version.js`, un seul numéro ; réseau d'abord) ; fréquences décimales bien comptées ; mail de test sans effet sur le rappel ; fond vert du thème Chantier ; confirmation avant de supprimer un contact ; chargement plus rapide.
- ✅ Étape 3 · **Sécurité** (script 1.8) : plus d'action par l'adresse (clé hors URL) ; mauvaises clés freinées ; bibliothèque PDF de l'export vérifiée par empreinte avant exécution.
- ✅ Étape 4 · **Export et ménage** : verrou au démarrage de l'export ; fonctions dangereuses de `Video.js` retirées (la galerie photos reste). Gros exports : chaque étape est découpée en passes de 4 min 30 (limite Google 6 min).
- **Numéro de version** : dans `version.js`, le seul endroit à changer.
- ✅ 0.4 Numéro de version unique (`version.js`)
- ✅ Étape 5 · **Mail une seule fois** (script 1.8.1) : plus de relance tous les 7 jours pour une tâche en retard.

## 4. Journal

| Date | Étape | Quoi |
|---|---|---|
| 05/11/2026 | 0.1 | Mode d'emploi créé ; script récupéré (Code 709 l., Export 1 272 l., Video 206 l.) ; audit lancé |
| 05/11/2026 | 0.2–0.3, B1 | Audit ; 8 adresses alignées ; lien des e-mails corrigé (version Google 15) |
| 05/11/2026 | 1–4 | Appli 1.8 et script 1.8 (version Google 16, 8 adresses) : toute la checklist corrigée sauf l'export > 6 min |
| 05/11/2026 | 5 | Mail d'échéance envoyé une seule fois par tâche, sans relance (script 1.8.1, version Google 17, 8 adresses) |
| 05/11/2026 | 6 | Appli 1.8.3 : le hors connexion n'efface plus celui de Versus ni du carnet de Carla |
| 05/11/2026 | 7 | Export plus rapide (appli 1.8.4, Export 2.4, version Google 18) : l'appli lance elle-même chaque étape au lieu d'attendre Google (1 à 2 min d'attente par étape supprimées) ; anciennes adresses du script supprimées, une seule reste |
| 06/11/2026 | 8 | Export 2.5 (version Google 19) : toute la ligne de l'index des annexes est cliquable ; « Ouvrir le PDF » ouvre le fichier lui-même (l'aperçu Google Drive ignore les liens internes « Annexe ») |
