# Zad_Dowland_1
# Dokumentacja programu
## Pobieranie danych z bazy MySQL do Pythona przy użyciu Pandas

### 1. Informacje ogólne

**Nazwa programu:** Pobieranie danych z bazy `wodospady`

**Język programowania:** Python

**Wykorzystane technologie:**
- MySQL / MariaDB – system zarządzania bazą danych.
- XAMPP – lokalne środowisko serwera bazodanowego.
- `mysql.connector` – biblioteka umożliwiająca połączenie Pythona z bazą MySQL.
- Pandas – biblioteka do pobierania, przetwarzania i prezentowania danych tabelarycznych.

### 2. Cel programu

Celem programu jest nawiązanie połączenia z lokalną bazą danych `wodospady`, pobranie wszystkich rekordów z tabeli `kontynenty`, a następnie przedstawienie pobranych informacji w dwóch formach:

1. Jako listy krotek (`lista_tupli`).
2. Jako tabeli wyświetlonej w konsoli przy użyciu biblioteki Pandas.

Program zamyka połączenie z bazą danych po zakończeniu operacji.

### 3. Import bibliotek

```python
import mysql.connector
import pandas as pd
```

**`mysql.connector`**

Biblioteka służy do nawiązywania połączenia z serwerem MySQL lub zgodnym serwerem MariaDB, wykonywania zapytań SQL oraz zarządzania połączeniem.

**`pandas`**

Biblioteka służy do pracy z danymi tabelarycznymi. W programie wykorzystywany jest obiekt `DataFrame`, który umożliwia przechowywanie i wyświetlanie wyników zapytania SQL.

### 4. Nawiązanie połączenia z bazą danych

```python
polaczenie = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wodospady",
    port=3306
)
```

Funkcja `mysql.connector.connect()` tworzy połączenie z serwerem bazy danych.

Znaczenie parametrów:

| Parametr | Opis |
|---|---|
| `host="localhost"` | Serwer znajduje się na lokalnym komputerze. |
| `user="root"` | Nazwa użytkownika bazy danych. |
| `password=""` | Puste hasło, jeśli tak skonfigurowano konto. |
| `database="wodospady"` | Nazwa bazy danych, z którą program się łączy. |
| `port=3306` | Port serwera MySQL/MariaDB. |

Obiekt połączenia zostaje zapisany w zmiennej `polaczenie` i jest wykorzystywany w kolejnych operacjach.

### 5. Sprawdzenie połączenia

```python
if polaczenie.is_connected():
    print("Połączono z bazą danych MySQL")
```

Metoda `is_connected()` sprawdza, czy połączenie z serwerem jest aktywne.

Jeśli połączenie jest aktywne, program wyświetla komunikat potwierdzający nawiązanie połączenia.

### 6. Pobieranie danych za pomocą Pandas

```python
df = pd.read_sql_query(
    "SELECT * FROM kontynenty",
    polaczenie
)
```

Funkcja `pd.read_sql_query()` wykonuje zapytanie SQL i zapisuje jego wynik w obiekcie `DataFrame`.

Zapytanie:

```sql
SELECT * FROM kontynenty;
```

oznacza pobranie wszystkich kolumn i wszystkich rekordów z tabeli `kontynenty`.

Wyniki zostają zapisane w zmiennej `df`.

### 7. Konwersja danych na listę krotek

```python
lista_tupli = list(df.itertuples(index=False, name=None))
```

Ta instrukcja przekształca dane z obiektu `DataFrame` na listę krotek.

Poszczególne elementy działania:

- `df.itertuples()` – przechodzi przez kolejne wiersze tabeli i zwraca je jako krotki.
- `index=False` – pomija indeks wiersza.
- `name=None` – tworzy zwykłe krotki zamiast nazwanych krotek.
- `list()` – zamienia otrzymany iterator w listę.

Przykładowa postać wyniku:

```python
[
    (1, "Europa"),
    (2, "Azja"),
    (3, "Afryka")
]
```

Powyższe wartości są przykładowe. Rzeczywisty wynik zależy od danych zapisanych w tabeli `kontynenty`.

### 8. Wyświetlenie listy krotek

```python
print(f"Lista krotek: {lista_tupli}")
```

Instrukcja `print()` wyświetla listę krotek w konsoli.

Zastosowanie f-stringa umożliwia umieszczenie wartości zmiennej `lista_tupli` bezpośrednio w tekście komunikatu.

### 9. Wyświetlenie danych w formie tabeli

```python
print(df.to_string(index=False))
```

Metoda `to_string()` przekształca zawartość obiektu `DataFrame` w tekstową tabelę.

Parametr `index=False` powoduje, że indeks wierszy nie jest wyświetlany jako dodatkowa kolumna.

Dzięki temu dane są prezentowane w czytelniejszej formie.

### 10. Zamknięcie połączenia

```python
polaczenie.close()
```

Metoda `close()` zamyka połączenie z bazą danych.

Jest to ważne, ponieważ pozwala zwolnić wykorzystywane zasoby serwera i ogranicza ryzyko pozostawienia niepotrzebnego aktywnego połączenia.

### 11. Algorytm działania programu

1. Zaimportowanie bibliotek `mysql.connector` i `pandas`.
2. Nawiązanie połączenia z bazą `wodospady`.
3. Sprawdzenie, czy połączenie jest aktywne.
4. Wykonanie zapytania SQL pobierającego dane z tabeli `kontynenty`.
5. Zapisanie wyników zapytania w obiekcie `DataFrame`.
6. Konwersja wierszy `DataFrame` na listę krotek.
7. Wyświetlenie listy krotek.
8. Wyświetlenie danych w postaci tabeli tekstowej.
9. Zamknięcie połączenia z bazą danych.

### 12. Wymagania do uruchomienia programu

- Zainstalowany Python.
- Uruchomiony serwer MySQL/MariaDB w XAMPP.
- Istniejąca baza danych `wodospady`.
- Istniejąca tabela `kontynenty`.
- Prawidłowe dane logowania do serwera.
- Zainstalowane biblioteki:

```bash
python -m pip install mysql-connector-python pandas
```

### 13. Możliwe błędy

**Błąd połączenia z serwerem**

Może wystąpić, jeśli serwer MySQL/MariaDB nie działa, port jest nieprawidłowy lub dane logowania są błędne.

**Brak bazy danych**

Jeśli baza `wodospady` nie istnieje, program nie będzie mógł nawiązać połączenia z określoną bazą.

**Brak tabeli**

Jeśli tabela `kontynenty` nie istnieje, zapytanie SQL zakończy się błędem.

**Brak biblioteki**

Jeżeli Python nie może zaimportować `mysql.connector` lub `pandas`, należy zainstalować odpowiednią bibliotekę w używanym środowisku.

### 14. Podsumowanie

Program demonstruje podstawową integrację Pythona z relacyjną bazą danych. Wykorzystuje zapytanie SQL do pobierania rekordów, bibliotekę Pandas do przechowywania i prezentowania danych oraz mechanizm konwersji danych tabelarycznych na listę krotek.

Rozwiązanie stanowi podstawę do dalszej nauki przetwarzania danych, automatyzacji zadań i budowania prostych procesów ETL (Extract, Transform, Load), wykorzystywanych w inżynierii danych.
