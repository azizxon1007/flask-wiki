from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Wikipedia API URL
WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            response = requests.get(WIKIPEDIA_API_URL, {
                'action': 'query',
                'format': 'json',
                'list': 'search',
                'srsearch': query
            }).json()

            search_results = response.get('query', {}).get('search', [])
            return render_template('search.html', results=search_results, query=query)
    
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
