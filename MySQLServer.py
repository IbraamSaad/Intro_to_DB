import mysql.connector

def create_database(db_name="alx_book_store"):
    """Creates the specified database if it doesn't exist using the explicit statement."""
    mydb = None  # Initialize mydb outside the try block

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ebr@#_012"
        )

        mycursor = mydb.cursor()

        # Directly use the requested statement
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        mydb.commit()  # Important: Commit after CREATE DATABASE

        print(f"Database '{db_name}' created/verified successfully!")  # More accurate message

    except mysql.connector.Error as err:
        print(f"Error creating/verifying database: {err}")  # More general error message

    finally:
        if mydb and mydb.is_connected():  # Check if mydb is initialized and connected
            mycursor.close()
            mydb.close()

if __name__ == "__main__":
    create_database()