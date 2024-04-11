from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock list of news articles with city information
articles = [
    {'id': 1, 'title': 'News Article 1', 'content': 'Content of News Article 1', 'city': 'New York'},
    {'id': 2, 'title': 'News Article 2', 'content': 'Content of News Article 2', 'city': 'Los Angeles'},
    {'id': 3, 'title': 'News Article 3', 'content': 'Content of News Article 3', 'city': 'New York'}
]

@app.route('/')
def index():
    city = request.args.get('city')
    filtered_articles = [article for article in articles if not city or article['city'] == city]
    return jsonify({'articles': filtered_articles})

@app.route('/article/<int:id>')
def get_article(id):
    '''http://127.0.0.1:5000/article/1'''
    article = next((article for article in articles if article['id'] == id), None)
    if article:
        return jsonify(article)
    else:
        return jsonify({'error': 'Article not found'}), 404

@app.route('/api/news')
def api_news():
    city = request.args.get('city')
    """http://127.0.0.1:5000/api/news?city=New%20York"""
    filtered_articles = [article for article in articles if not city or article['city'] == city]
    return jsonify({'articles': filtered_articles})

if __name__ == '__main__':
    app.run(debug=True)