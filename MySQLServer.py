import mysql.connector

def create_database(db_name="alx_book_store"):
    
    try:
        mydb = mysql.connector.connect(
            host="localhost",  
            user="root",       
            password="Ebr@#_012"   
        )

        mycursor = mydb.cursor()

        
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}") 

        mydb.commit() 

        print(f"Database '{db_name}' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == 1007:  
             print(f"Database '{db_name}' already exists.")
        else:
            print(f"Error creating database: {err}")

    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

if __name__ == "__main__":
    create_database()  
