# Instalacja i uruchomienie

Ten projekt jest aplikacją Django umieszczoną w katalogu `klon/`. Zależności są trzymane w `requirements.txt` w katalogu głównym repozytorium.

## Wymagania

- Python 3.x
- Git
- Dostęp do terminala

Na Windowsie, jeśli komenda `python` otwiera Microsoft Store, użyj launchera `py`, na przykład `py -3.13`.

## 1. Pobranie projektu

```bash
git clone https://github.com/Exhil95/klon_gladiatusa.git
cd klon_gladiatusa
```

## 2. Środowisko wirtualne

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows przez launcher `py`:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Instalacja zależności

```bash
pip install -r requirements.txt
```

## 4. Migracje bazy danych

Przejdź do katalogu aplikacji Django:

```bash
cd klon
```

Uruchom migracje:

```bash
python manage.py migrate
```

Opcjonalnie utwórz konto administratora:

```bash
python manage.py createsuperuser
```

## 5. Uruchomienie serwera

```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem:

```text
http://127.0.0.1:8000/
```

Panel administratora:

```text
http://127.0.0.1:8000/admin/
```

## 6. Testy

Testy uruchamiaj z katalogu `klon/`:

```bash
python manage.py test
```

Jeśli korzystasz z Windowsowego launchera:

```powershell
py -3.13 manage.py test
```

## Przydatne komendy

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py test
python manage.py runserver
```

## Rozwiązywanie problemów

| Problem | Co sprawdzić |
| --- | --- |
| `ModuleNotFoundError` | Czy aktywowane jest `.venv` i czy wykonano `pip install -r requirements.txt`. |
| `manage.py` nie istnieje | Czy terminal jest w katalogu `klon/`, a nie w katalogu głównym repozytorium. |
| Brak lokacji lub przeciwników | Czy baza zawiera dane startowe dodane przez panel admina, fixture albo ręcznie. |
| Błędy obrazów przeciwników | Czy pliki istnieją w `klon/media/portraits/` i czy rekordy w bazie wskazują poprawne ścieżki. |

## Uwagi produkcyjne

Obecna konfiguracja jest developerska. Przed hostingiem należy co najmniej:

- przenieść `SECRET_KEY` do zmiennych środowiskowych,
- ustawić `DEBUG = False`,
- uzupełnić `ALLOWED_HOSTS`,
- skonfigurować statyczne pliki i media,
- rozważyć PostgreSQL zamiast SQLite.
