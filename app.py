from flask import Flask, request, redirect, url_for
import string
import random

app = Flask(__name__)

# Dictionary to store the shortened URLs
url_mapping = {}

# Function to generate a random string for the short URL
def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/')
def index():
    return '''
        <h1>URL Shortener</h1>
        <form action="/shorten" method="post">
            <input type="url" name="url" required>
            <input type="submit" value="Shorten">
        </form>
    '''

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    short_id = generate_short_id()
    url_mapping[short_id] = original_url
    return f'Shortened URL: <a 
href="/{short_id}">{request.host_url}{short_id}</a>'

@app.route('/<short_id>')
def redirect_to_url(short_id):
    original_url = url_mapping.get(short_id)
    if original_url:
        return redirect(original_url)
    else:
        return '<h1>URL not found!</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

