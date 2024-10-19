import sqlite3

# Step 1: Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('/Users/stas_chi/Documents/Projects/Izba AI/backend/databases/price_paid_data.db')  # Replace with your database file

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Run a SELECT query to fetch data
cursor.execute("SELECT AVG(price) FROM price_paid_data WHERE property_type = 'D' AND date_of_transfer LIKE '%/2020'")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Step 4: Close the connection
conn.close()