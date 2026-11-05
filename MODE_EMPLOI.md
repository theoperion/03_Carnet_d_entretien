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

**Mise en ligne** : Claude publie sur `main` chaque étape validée, en disant ce qu'il publie (autorisé par Théo le 05/11/2026). E-mails d'échéance : envoyés par un réveil du script, indépendant de l'adresse ; état visible dans l'appli (« Mail d'échéance : ✅ actif »).

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
- 🟡 Étape 1 · File d'attente hors connexion fiable (A1 à A6) · Étape 2 · Autres bugs (B2 à B7) · Étape 3 · Sécurité (C1 à C3) · Étape 4 · Ménage (E1)
- ⬜ 0.4 Numéro de version unique (comme Versus)

## 4. Journal

| Date | Étape | Quoi |
|---|---|---|
| 05/11/2026 | 0.1 | Mode d'emploi créé ; script récupéré (Code 709 l., Export 1 272 l., Video 206 l.) ; audit lancé |
| 05/11/2026 | 0.2–0.3, B1 | Audit ; 8 adresses alignées ; lien des e-mails corrigé (version Google 15) |
