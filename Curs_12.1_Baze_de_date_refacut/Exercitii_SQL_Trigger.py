# importare sqlite3
import sqlite3

# creare baza de date si conectare la aceasta
conn = sqlite3.connect("sales.db")

# creare cursor
cursor = conn.cursor()

# creare tabel principal
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL
    );
    """
)
conn.commit()

# creare tabel sales_log
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS sales_log (
        id INTEGER,
        old_amount REAL,
        new_amount REAL,
        note TEXT
    );
    """
)
conn.commit()

# creare trigger care se declanseaza la inserare date
cursor.execute(
    """
    CREATE TRIGGER IF NOT EXISTS sales_insert_trigger
    AFTER INSERT ON sales
    BEGIN
        INSERT INTO sales_log SELECT NEW.id, NULL, NEW.amount, "New sale inserted";
    END;
    """
)
conn.commit()

# creare trigger care se declanseaza la modificare date
cursor.execute(
    """
    CREATE TRIGGER IF NOT EXISTS sales_update_trigger
    AFTER UPDATE ON sales
    BEGIN
        INSERT INTO sales_log SELECT OLD.id, OLD.amount, NEW.amount, "Sale amount updated"
        WHERE OLD.amount != NEW.amount;
    END;
    """
)
conn.commit()

# trebuie sa fac drop la trigger-ul sales_update_trigger pentru ca am facut un typo
cursor.execute("DROP TRIGGER IF EXISTS sales_update_trigger")
conn.commit()

# recreez din nou trigger-ul sales_update_trigger fara typo
cursor.execute(
    """
    CREATE TRIGGER IF NOT EXISTS sales_update_trigger
    AFTER UPDATE ON sales
    BEGIN
        INSERT INTO sales_log SELECT OLD.id, OLD.amount, NEW.amount, "Sale amount updated"
        WHERE OLD.amount != NEW.amount;
    END;
    """
)
conn.commit()

# creare trigger care se declanseaza la stergere de date
cursor.execute(
    """
    CREATE TRIGGER IF NOT EXISTS delete_sales_trigger
    AFTER DELETE ON sales
    BEGIN
        INSERT INTO sales_log SELECT OLD.id, OLD.amount, "Sale deleted";
    END;
    """
)
conn.commit()

# stergere trigger -> trebuie refacut cu un parametru aditional
cursor.execute("DROP TRIGGER IF EXISTS delete_sales_trigger")
conn.commit()

# refacere delete_sales_trigger cu parametru aditional
cursor.execute(
    """
    CREATE TRIGGER IF NOT EXISTS delete_sales_trigger
    AFTER DELETE ON sales
    BEGIN
        INSERT INTO sales_log SELECT OLD.id, OLD.amount, NULL, "Sale deleted!";
    END;
    """
)
conn.commit()

# inserare date in tabelul sales
cursor.execute(
    """
    INSERT INTO sales (amount) VALUES (3966);
    """
)
conn.commit()

# stergere date din tabelul sales
cursor.execute(
    """
    DELETE FROM sales WHERE id = 1;
    """
)
conn.commit()

# modificare date in tabelul sales
cursor.execute(
    """
    UPDATE sales SET amount = 100000 WHERE id = 2;
    """
)
conn.commit()

# stergere din tabelul sales unde cantitatea egala cu 3966
cursor.execute(
    """
    DELETE FROM sales WHERE amount=3966;
    """
)
conn.commit()
