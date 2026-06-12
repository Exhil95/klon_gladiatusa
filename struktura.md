# Struktura projektu

Repozytorium składa się z katalogu głównego z dokumentacją i zależnościami oraz katalogu `klon/`, który jest właściwym projektem Django.

```text
klon_gladiatusa/
├── README.md
├── instalacja.md
├── struktura.md
├── api.md
├── requirements.txt
└── klon/
    ├── manage.py
    ├── db.sqlite3
    ├── klon_gl/
    ├── members/
    ├── user_profile/
    ├── lokacje/
    ├── inventory/
    ├── items/
    ├── merchant/
    ├── templates/
    ├── static/
    └── media/
```

## Katalog główny

| Ścieżka | Rola |
| --- | --- |
| `README.md` | Główna strona projektu: opis, funkcje, szybki start i roadmapa. |
| `instalacja.md` | Instrukcja instalacji, uruchomienia i testowania. |
| `struktura.md` | Opis organizacji katalogów i odpowiedzialności modułów. |
| `api.md` | Dokumentacja wewnętrznych modułów, modeli, widoków i tras. |
| `requirements.txt` | Lista zależności Pythona. |
| `.vscode/launch.json` | Konfiguracja uruchamiania Django w Visual Studio Code. |

## Projekt Django: `klon/`

| Ścieżka | Rola |
| --- | --- |
| `manage.py` | Główne narzędzie administracyjne Django. |
| `db.sqlite3` | Lokalna baza developerska SQLite. |
| `klon_gl/` | Konfiguracja projektu Django. |
| `templates/` | Wspólne szablony, takie jak `base.html`, `navbar.html`, `sidebar.html`, `banner_up.html`. |
| `static/` | Pliki statyczne: CSS, HTMX, Alpine.js, obrazy. |
| `media/` | Pliki wgrywane lub używane jako media, między innymi portrety przeciwników. |

## Aplikacje Django

| Aplikacja | Odpowiedzialność |
| --- | --- |
| `members/` | Logowanie, rejestracja i wylogowanie użytkowników. |
| `user_profile/` | Profil gracza, statystyki, HP, stamina, exp, levelowanie i sygnał tworzenia profilu. |
| `lokacje/` | Lokacje, przeciwnicy, mapa oraz silnik walki. |
| `inventory/` | Plecak, zakładanie przedmiotów, zdejmowanie przedmiotów, mikstury i banner gracza. |
| `items/` | Definicje przedmiotów, typy, sloty, obrażenia, bonusy i wartość. |
| `merchant/` | Handlarze, oferty czasowe, kupowanie i sprzedawanie. |

## Konwencje Django w projekcie

Każda aplikacja trzyma standardowe pliki Django:

- `models.py` dla modeli bazy danych,
- `views.py` dla widoków i logiki HTTP,
- `urls.py` dla tras aplikacji, jeśli aplikacja wystawia endpointy,
- `admin.py` dla konfiguracji panelu admina,
- `tests.py` dla testów,
- `migrations/` dla migracji bazy danych,
- `templates/<nazwa_aplikacji>/` dla szablonów aplikacji.

## Szablony i frontend

Projekt używa klasycznych szablonów Django, z warstwą interakcji opartą o HTMX i Alpine.js.

Najważniejsze wspólne szablony:

- `klon/templates/base.html` - główny layout,
- `klon/templates/sidebar.html` - boczna nawigacja,
- `klon/templates/navbar.html` - nawigacja górna,
- `klon/templates/banner_up.html` - pasek stanu gracza,
- `klon/templates/enemy_list.html` - lista przeciwników w lokacji.

Szablony aplikacyjne są trzymane wewnątrz aplikacji, na przykład:

- `klon/lokacje/templates/lokacje/`,
- `klon/inventory/templates/inventory/`,
- `klon/merchant/templates/merchants/`,
- `klon/members/templates/authenticate/`,
- `klon/user_profile/templates/profil_gracza/`.

## Pliki statyczne i media

| Ścieżka | Zawartość |
| --- | --- |
| `klon/static/css/custom.css` | Dodatkowe style projektu. |
| `klon/static/js/htmx.min.js` | Lokalna kopia HTMX. |
| `klon/static/js/alpine.min.js` | Lokalna kopia Alpine.js. |
| `klon/static/images/` | Obrazy interfejsu, tło, favicon, mapa. |
| `klon/media/portraits/` | Portrety przeciwników używane przez model `Enemy`. |

## Uwagi porządkowe

- `klon/` jest katalogiem, z którego należy uruchamiać `manage.py`.
- `db.sqlite3` ułatwia lokalny rozwój, ale dla produkcji warto użyć migracji i osobnej bazy.
- `items/` nie ma obecnie własnego `urls.py`, ponieważ definicje przedmiotów są używane przez inne aplikacje.
- `user_profile/urls.py` zawiera powieloną trasę `profil/`; Django używa pierwszego pasującego wzorca.
