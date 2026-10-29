import mysql.connector
import pandas as pd

polaczenie = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    # Zmieniono bazę na „wodospady”, widoczną na przesłanym zrzucie.
    database="wodospady",
    port=3306
)

if polaczenie.is_connected():
    print("Połączono z bazą danych MySQL")

# Zmieniono pobieranie: pandas odczytuje tabelę „kontynenty” z bazy „wodospady”.
df = pd.read_sql_query("SELECT * FROM kontynenty", polaczenie)

# Zamienia wiersze z DataFrame na krotki i zapisuje je w liście lista_tupli.
lista_tupli = list(df.itertuples(index=False, name=None))

print(f"Lista krotek: {lista_tupli}")

# Wyświetla dane w konsoli w formie tabeli, bez dodatkowej kolumny indeksu.
print(df.to_string(index=False))


polaczenie.close()