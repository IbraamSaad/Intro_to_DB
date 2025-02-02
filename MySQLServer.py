import mysql.connector

try:

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Ebr@#_012",
        database = "alx_book_store"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    mydb.commit()

    print(f"Database {mydb} created successfully!")

except mysql.connector.Error as err:
        print(f"Error creating/verifying database: {err}")
finally:
      if mydb and mydb.is_connected():
            mycursor.close()
            mydb.close()
            


