# Klon Gladiatusa

Przeglądarkowa gra RPG inspirowana Gladiatusem, zbudowana w Django. Projekt skupia się na klasycznym loopie rozgrywki: rozwój postaci, ekwipunek, walka z przeciwnikami, zdobywanie łupu oraz handel z NPC.

## Spis treści

- [Najważniejsze funkcje](#najważniejsze-funkcje)
- [Stack technologiczny](#stack-technologiczny)
- [Szybki start](#szybki-start)
- [Dokumentacja](#dokumentacja)
- [Status projektu](#status-projektu)
- [Roadmapa](#roadmapa)
- [Autorzy](#autorzy)

## Najważniejsze funkcje

| Obszar | Status | Opis |
| --- | --- | --- |
| Profil gracza | Gotowe | Statystyki bazowe i pochodne, poziomy, doświadczenie, punkty statystyk, HP i stamina. |
| Walka | Gotowe | Lokacje z przeciwnikami, strategie walki, log walki, nagrody, koszt staminy i loot. |
| Ekwipunek | Gotowe | Plecak, zakładanie i zdejmowanie przedmiotów, bonusy ze statystyk wyposażenia. |
| Przedmioty | Gotowe | Typy ekwipunku, mikstury, poziom przedmiotu, wartość, obrażenia i bonusy. |
| Handlarze | Gotowe | Kowal i alchemik, oferty czasowe, kupowanie oraz sprzedawanie. |
| Autoryzacja | Gotowe | Rejestracja, logowanie i wylogowanie użytkownika. |
| Interakcje HTMX | Gotowe | Fragmenty widoków dla walki, banneru gracza, plecaka i ofert handlarzy. |

## Stack technologiczny

- Python 3.x
- Django 5.1
- SQLite jako baza developerska
- Django templates
- HTMX
- Alpine.js
- Tailwind CSS przez CDN
- Pillow dla obrazów i portretów przeciwników

## Szybki start

Pełna instrukcja znajduje się w pliku [instalacja.md](instalacja.md). Minimalny scenariusz lokalny:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd klon
python manage.py migrate
python manage.py runserver
```

Po uruchomieniu aplikacja będzie dostępna pod adresem:

```text
http://127.0.0.1:8000/
```

## Dokumentacja

- [Instalacja i uruchomienie](instalacja.md)
- [Struktura projektu](struktura.md)
- [Dokumentacja modułów](api.md)

## Status projektu

Projekt jest grywalnym prototypem. Najważniejsze systemy są już połączone, ale kod nadal ma miejsca typowe dla etapu rozwoju:

- konfiguracja produkcyjna nie jest jeszcze wydzielona ze `settings.py`,
- baza SQLite i pliki mediów są traktowane jako lokalne środowisko developerskie,
- część tras i widoków wymaga dalszego porządkowania,
- balans walki, dropów i ekonomii można rozwijać iteracyjnie.

## Roadmapa

Najbardziej naturalne kolejne kroki:

1. Wydzielenie ustawień środowiskowych: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, baza danych.
2. Uporządkowanie routingu profilu i endpointów HTMX.
3. Dodanie seedów lub komend management dla lokacji, przeciwników i przedmiotów startowych.
4. Rozbudowa testów walki, ekwipunku, handlu i rejestracji.
5. Dodanie widoku administracyjnego lub panelu do zarządzania balansem gry.
6. Przygotowanie konfiguracji pod hosting z PostgreSQL.

## Autorzy

- Denis Kuczka
- Mateusz Rduch
