import mysql.connector
from contextlib import contextmanager

@contextmanager
def get_db_cursor(commit=False):
   
    cursor = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bharath@2003",  
            database="ai_agent"  
        )

        if connection.is_connected():
            print(" Database connection successful!")
        else:
            print("Database connection failed!")

        cursor = connection.cursor(dictionary=True)
        yield cursor

        if commit:
            connection.commit()

    except mysql.connector.Error as e:
        print("Database error:", e)
        yield None

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("Database connection closed.")


def create_table():
    """Ensure the memory table exists."""
    with get_db_cursor(commit=True) as cursor:
        if cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS memory (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    `key` VARCHAR(255) UNIQUE,
                    `value` TEXT
                )
            ''')
            print("Memory table verified/created successfully.")

if __name__ == "__main__":
    with get_db_cursor() as cursor:
        if cursor:
            print("Connection test completed successfully.")
        else:
            print("Connection test failed.")
	

