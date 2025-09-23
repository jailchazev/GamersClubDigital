# app.py
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)