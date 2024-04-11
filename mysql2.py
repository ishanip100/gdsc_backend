from flask import Flask, jsonify, request
import mysql.connector

app = Flask(_name_)

# Configure MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ishani@123",
    database="test"
)

# Define the cursor
cursor = db.cursor(dictionary=True)

# Example data initialization (You can perform this directly in your MySQL database)

@app.route('/')
def index():
    city = request.args.get('city')
    if city:
        query = "SELECT * FROM news_articles WHERE city = %s"
        cursor.execute(query, (city,))
    else:
        query = "SELECT * FROM news_articles"
        cursor.execute(query)
    articles = cursor.fetchall()
    return jsonify({'articles': articles})

@app.route('/article/<int:id>')
def get_article(id):
    query = "SELECT * FROM news_articles WHERE id = %s"
    cursor.execute(query, (id,))
    article = cursor.fetchone()
    if article:
        return jsonify(article)
    else:
        return jsonify({'error': 'Article not found'}), 404

if _name_ == '_main_':
    app.run(debug=True)
