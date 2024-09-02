# coding=utf-8
import sqlite3
import os

database = "data.db"


def connection(base):
    conn = sqlite3.connect(base)
    return conn


def create_table_if_not_exists(conn):
    try:
        cursor = conn.cursor()
        # Check if the table exists
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='temperatures';")
        result = cursor.fetchone()

        if not result:
            # Create the table if it doesn't exist
            cursor.execute('''
                CREATE TABLE temperatures (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    temperature REAL NOT NULL
                );
            ''')
            print("Table 'temperatures' created successfully.")
        else:
            print("Table 'temperatures' already exists.")

    except sqlite3.Error as e:
        print(f"An error occurred while checking or creating the table: {e}")


def base_writing(temp_data):
    date_str, temperature_str = temp_data.split(',')
    temperature = float(temperature_str)
    record = (date_str, temperature)
    try:
        conn = connection(database)
        cursor = conn.cursor()
        # Ensure the table exists
        create_table_if_not_exists(conn)

        # Proceed with the intended operation
        cursor.execute(
            "INSERT INTO temperatures (date, temperature) VALUES (?, ?)",
            record)
        # Commit the transaction to save the changes to the database
        conn.commit()

        print("I've done with record: ", record)

    except sqlite3.Error as e:
        print(f"An error occurred during database operation: {e}")
    finally:
        conn.close()


def base_reading():
    try:
        conn = connection(database)
        cursor = conn.cursor()
        # Ensure the table exists
        create_table_if_not_exists(conn)

        # Proceed with the intended operation
        cursor.execute("SELECT date FROM temperatures")
        date = cursor.fetchall()
        print("This is date (SELECT date FROM temperatures):", date)

    except sqlite3.Error as e:
        print(f"An error occurred during database operation: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    base_writing("2024-08-08, 20")
    base_reading()
