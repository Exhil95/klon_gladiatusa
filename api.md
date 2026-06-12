# Dokumentacja modułów

Ten plik opisuje wewnętrzne moduły projektu. Nie jest to publiczne REST API, tylko mapa modeli, widoków, tras i zależności między aplikacjami Django.

## Przegląd aplikacji

| Aplikacja | Główna rola |
| --- | --- |
| `members` | Konta użytkowników: rejestracja, logowanie, wylogowanie. |
| `user_profile` | Dane gracza: statystyki, poziom, doświadczenie, HP, stamina, złoto. |
| `items` | Definicje przedmiotów, slotów, mikstur i bonusów. |
| `inventory` | Instancje przedmiotów przypisane do użytkownika oraz obsługa wyposażenia. |
| `lokacje` | Lokacje, przeciwnicy, mapa i walka. |
| `merchant` | Handlarze, rotujące oferty, kupowanie i sprzedawanie. |
| `klon_gl` | Konfiguracja całego projektu Django. |

## `klon_gl`

Główna konfiguracja Django.

### Najważniejsze pliki

| Plik | Rola |
| --- | --- |
| `settings.py` | Zainstalowane aplikacje, middleware, baza SQLite, statyczne pliki, media, język i strefa czasu. |
| `urls.py` | Główna mapa URL-i projektu. |
| `asgi.py` | Wejście ASGI. |
| `wsgi.py` | Wejście WSGI. |

### Główne trasy

| URL | Cel |
| --- | --- |
| `/` | Przekierowanie do profilu gracza. |
| `/admin/` | Panel administratora Django. |
| `/members/` | Trasy logowania i rejestracji. |
| `/user_profile/` | Profil gracza i rozdawanie statystyk. |
| `/lokacje/` | Mapa, lokacje i walka. |
| `/merchant/` | Handlarze. |
| `/inventory/` | Plecak i wyposażenie. |

## `members`

Obsługuje podstawową autoryzację użytkownika.

### Widoki

| Widok | Rola |
| --- | --- |
| `login_user` | Loguje użytkownika i przekierowuje do profilu. |
| `logout_user` | Wylogowuje użytkownika i wraca do formularza logowania. |
| `register_user` | Tworzy konto przez `UserCreationForm`, loguje użytkownika i przechodzi do profilu. |

### Trasy

| URL | Nazwa |
| --- | --- |
| `/members/login_user` | `login_user` |
| `/members/logout_user` | `logout_user` |
| `/members/register_user` | `register_user` |

## `user_profile`

Centralny moduł postaci gracza.

### Model `UserProfile`

Najważniejsze pola:

| Grupa | Pola |
| --- | --- |
| Użytkownik | `user` |
| Statystyki | `strength`, `dexterity`, `constitution`, `intelligence` |
| Statystyki bazowe | `base_strength`, `base_dexterity`, `base_constitution`, `base_intelligence` |
| Rozwój | `level`, `experience`, `stat_points` |
| Zasoby | `gold`, `hp`, `max_hp`, `stamina`, `max_stamina` |
| Walka | `attack`, `base_attack`, `defence`, `base_defence` |
| Regeneracja | `last_regen`, `last_regen_stm` |

### Metody modelu

| Metoda | Rola |
| --- | --- |
| `lvlup_exp()` | Wylicza wymagane doświadczenie do kolejnego poziomu. |
| `dodaj_exp(exp)` | Dodaje doświadczenie i obsługuje awans. |
| `lvlup()` | Podnosi poziom, dodaje punkty statystyk i odnawia HP oraz staminę. |
| `hp_regen()` | Regeneruje HP na podstawie czasu, inteligencji i budowy fizycznej. |
| `stamina_regen()` | Regeneruje staminę na podstawie czasu i inteligencji. |
| `equipped_items()` | Pobiera założone przedmioty użytkownika. |
| `update_stats()` | Przelicza statystyki po zmianie ekwipunku lub statystyk bazowych. |

### Widoki

| Widok | Rola |
| --- | --- |
| `WidokProfilu` | Główny widok profilu gracza. |
| `WidokRozdaniaStaystyk` | Dodaje punkt do wybranej statystyki. |
| `profil_gracza` | Funkcyjna wersja widoku profilu. Obecnie trasa jest powielona z `WidokProfilu`. |

### Sygnały

`create_user_profile` tworzy `UserProfile` automatycznie po utworzeniu użytkownika Django.

## `items`

Definiuje przedmioty dostępne w grze.

### Model `Item`

| Pole | Rola |
| --- | --- |
| `name`, `description` | Nazwa i opis przedmiotu. |
| `rarity` | Rzadkość: common, uncommon, rare, epic, legendary. |
| `slot` | Slot ekwipunku, na przykład weapon, shield, head, chest. |
| `item_type` | Typ: ekwipunek, mikstura HP, mikstura staminy. |
| `item_level` | Poziom przedmiotu. |
| `dmg`, `dmg_min`, `dmg_max` | Obrażenia. |
| `item_strength`, `item_dexterity`, `item_constitution`, `item_intelligence` | Bonusy statystyk. |
| `value` | Wartość przedmiotu u handlarzy. |
| `effect_value` | Wartość efektu mikstury. |

### Metody

| Metoda | Rola |
| --- | --- |
| `dmg_calc()` | Wylicza minimalne i maksymalne obrażenia na podstawie `dmg`. |

## `inventory`

Łączy użytkowników z konkretnymi egzemplarzami przedmiotów.

### Model `InventoryItem`

| Pole | Rola |
| --- | --- |
| `user` | Właściciel przedmiotu. |
| `item` | Definicja przedmiotu z aplikacji `items`. |
| `equipped` | Informacja, czy przedmiot jest założony. |

### Widoki

| Widok | Rola |
| --- | --- |
| `backpack_view` | Wyświetla plecak użytkownika. |
| `equip_item` | Zakłada przedmiot i zdejmuje poprzedni przedmiot z tego samego slotu. |
| `unequip_item` | Zdejmuje przedmiot. |
| `give_item` | Dodaje przedmiot użytkownikowi, przydatne developersko. |
| `use_potion` | Zużywa miksturę HP lub staminy. |
| `refresh_banner` | Odświeża pasek stanu gracza przez HTMX. |

### Trasy

| URL | Nazwa |
| --- | --- |
| `/inventory/plecak/` | `backpack` |
| `/inventory/equip/<item_id>/` | `equip_item` |
| `/inventory/unequip/<item_id>/` | `unequip_item` |
| `/inventory/give/<item_id>/` | `give_item` |
| `/inventory/use/<item_id>/` | `use_potion` |
| `/inventory/ajax/refresh-banner/` | `refresh_banner` |

## `lokacje`

Odpowiada za mapę świata, lokacje, przeciwników i walkę.

### Model `Enemy`

| Pole | Rola |
| --- | --- |
| `name`, `description` | Nazwa i opis przeciwnika. |
| `lvl`, `type` | Poziom i typ przeciwnika: normalny, elita, boss. |
| `base_strenght`, `base_intelect`, `base_dexterity`, `base_constitution` | Bazowe statystyki przeciwnika. |
| `base_hp`, `base_attack`, `base_defence` | Statystyki bojowe. |
| `gold_drop`, `drop_chance`, `loot_table` | Nagrody za pokonanie przeciwnika. |
| `portrait` | Portret przeciwnika. |

### Model `Location`

| Pole | Rola |
| --- | --- |
| `name` | Nazwa lokacji. |
| `enemies` | Przeciwnicy dostępni w lokacji. |

### Silnik walki

`BattleEngine` symuluje walkę turową:

- wybiera modyfikatory strategii: agresywnej, defensywnej albo zbalansowanej,
- liczy obrażenia gracza i przeciwnika,
- obsługuje trafienia krytyczne, blok i unik,
- kończy walkę po śmierci jednej ze stron albo po limicie 20 tur,
- zwraca końcowe HP gracza, HP przeciwnika, wynik i log walki.

### Widoki

| Widok | Rola |
| --- | --- |
| `mapa_view` | Wyświetla mapę i nazwy lokacji. |
| `beast_dung_view` | Lokacja Zdziczałe Lochy. |
| `circus_view` | Lokacja Cyrk Gladiatorów. |
| `dessert_hills_view` | Lokacja Pustynne Wzgórza. |
| `plains_view` | Lokacja Równiny. |
| `fight_view` | Obsługuje formularz walki, koszt staminy, nagrody, loot i wynik. |
| `refresh_banner` | Odświeża pasek stanu gracza po walce. |

### Trasy

| URL | Nazwa |
| --- | --- |
| `/lokacje/` | `mapa` |
| `/lokacje/beast_dungeon/` | `beast_dung` |
| `/lokacje/circus/` | `circus` |
| `/lokacje/dessert_hills/` | `dessert_hills` |
| `/lokacje/plains/` | `plains` |
| `/lokacje/fight/<enemy_id>/` | `fight` |
| `/lokacje/ajax/refresh-banner/` | `refresh_banner` |

## `merchant`

Odpowiada za handel z NPC.

### Model `MerchantOffer`

| Pole | Rola |
| --- | --- |
| `item` | Przedmiot w ofercie. |
| `price` | Cena zakupu. |
| `available_until` | Czas wygaśnięcia oferty. |
| `type` | Typ handlarza: kowal albo alchemik. |
| `stock` | Liczba dostępnych sztuk. |

### Generowanie ofert

| Funkcja | Rola |
| --- | --- |
| `generate_blacksmith_offer()` | Tworzy czasową ofertę ekwipunku dla kowala. |
| `generate_alchemist_offer()` | Tworzy czasową ofertę mikstur dla alchemika. |

### Widoki

| Widok | Rola |
| --- | --- |
| `blacksmith_page_view` | Strona kowala z ofertą i plecakiem gracza. |
| `blacksmith_offer_fragment` | Fragment HTMX z ofertą kowala. |
| `buy_offer_view` | Kupowanie przedmiotu od kowala. |
| `sell_to_merchant` | Sprzedaż przedmiotu kowalowi. |
| `alchemist_page_view` | Strona alchemika z ofertą i plecakiem gracza. |
| `buy_offer_alchemist` | Kupowanie mikstury od alchemika. |
| `sell_to_alchemist` | Sprzedaż przedmiotu alchemikowi. |
| `backpack_fragment`, `backpack_fragment_alchemist` | Fragmenty HTMX plecaka. |
| `merchant_view` | Ogólny widok handlarza. |

### Trasy

| URL | Nazwa |
| --- | --- |
| `/merchant/blacksmith/` | `blacksmith_page` |
| `/merchant/blacksmith/offer/` | `blacksmith_offer` |
| `/merchant/blacksmith/offers/` | `blacksmith_offer_fragment` |
| `/merchant/blacksmith/buy/<offer_id>/` | `buy_offer` |
| `/merchant/blacksmith/sell/<item_id>/` | `sell_to_merchant` |
| `/merchant/blacksmith/backpack-fragment/` | `backpack_fragment` |
| `/merchant/merchant/` | `merchant_view` |
| `/merchant/alchemist/` | `alchemist` |
| `/merchant/alchemist/buy/<offer_id>/` | `buy_offer_alchemist` |
| `/merchant/alchemist/sell/<item_id>/` | `sell_to_alchemist` |
| `/merchant/alchemist/backpack-fragment/` | `backpack_fragment_alchemist` |

## Zależności między modułami

```text
User
└── UserProfile
    ├── InventoryItem
    │   └── Item
    ├── BattleEngine
    │   └── Enemy
    │       └── loot_table -> Item
    └── MerchantOffer
        └── Item
```

## Testy

Testy są uruchamiane przez Django:

```bash
cd klon
python manage.py test
```

Najważniejsze aktualne obszary testów:

- levelowanie i regeneracja profilu gracza,
- renderowanie mapy lokacji,
- podstawowe scenariusze wygranej i przegranej walki.
