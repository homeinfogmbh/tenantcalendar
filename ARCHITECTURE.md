# tenantcalendar
Stand: 2026-07-29, geprüft gegen Commit 13d2d82

## Zweck
Mieter-Kalender für die ComCat-App: Verwaltung und Anzeige von Terminen/
Ereignissen für Mieter (Kunden-, Gruppen- und Nutzer-Ebene), inkl.
Push-Benachrichtigung.

## Stack & Einstiegspunkte
Python 3, Flask/`wsgilib`, Peewee via `peeweeplus`, XML via `pyxb`, Push via
`firebase_admin`. Package `tenantcalendar`.

## Schnittstellen
### Konsumiert
- **Dependencies:** `comcatlib`, `cmslib`, `hwdb`, `mdb`, `firebase_admin`,
  `pyxb`, `werkzeug`, `wsgilib`, `peewee`, `peeweeplus`.

### Bietet an
- **ORM-Modelle + Endpunkte** für Mieter-Termine (Customer-/Membership-/User-
  Ebene). Von `dscms4`/`comcat` (Kalender-Endpunkte) eingebunden.

## Deployment / Laufzeit
Reine Bibliothek; von den ComCat-Backends importiert. Kein eigener Dienst.
⚠️ ANNAHME: Push-Credentials in der Konfiguration außerhalb des Repos.

## Ersetzbarkeit
Kopplungsgrad: **mittel**. Abgegrenzte Kalenderfunktion; an `comcatlib`/`cmslib`
und FCM gebunden.

## Weitere Doku
- `README.md` (Zweck, Verweis auf `comcat`).
- Verwandt: `comcat`, `dscms4`, `tenantforum`.
- ⚠️ ANNAHME: Zentrales Repo `homeinfo-architektur` (Ordner `komponenten/`) noch
  nicht geprüft.
