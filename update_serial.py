import pandas as pd
import os
import mysql.connector

# chargement du fichier csv
df = pd.read_csv("updated_serial_numbers.csv")

# Connexion au MySQL 
conn = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="root",
    database="acme"
)

cursor = conn.cursor()

# Boucle pour parcourir les lignes du CSV et appliquer le update
for _, row in df.iterrows():
    
    if pd.isnull(row["employee_id"]) or pd.isnull(row["serial_number"]):
        continue  
    employee_id = int(row["employee_id"])
    new_serial = str(row["serial_number"])

    cursor.execute("""
        UPDATE BADGE
        SET serial_number = %s
        WHERE employee_id = %s
    """, (new_serial, employee_id))

cursor.execute("SELECT serial_number FROM BADGE WHERE employee_id = %s", (employee_id,))
current = cursor.fetchone()[0]

#Verification
if current == new_serial:
    print(f"employee_id {employee_id} has correct serial_number")
else:
    print(f" ERROR: employee_id {employee_id} has serial_number {current}, expected {new_serial}")


conn.commit()
cursor.close()
conn.close()



