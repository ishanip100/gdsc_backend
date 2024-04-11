import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="local_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object
cursor = conn.cursor()

# Create a table for cities and news links
cursor.execute("""
    CREATE TABLE IF NOT EXISTS city_news_links (
        id INT AUTO_INCREMENT PRIMARY KEY,
        city VARCHAR(255),
        news_link TEXT
    )
""")

# Commit the changes
conn.commit()

# Close cursor and connection
cursor.close()
conn.close()
