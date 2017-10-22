import urllib2

from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from flask_assets import Environment, Bundle
from google import google

# Configure app.
app = Flask(__name__)
app.config.from_object('config.DevConfig')

# Compile style assets.
assets = Environment(app)
scss = Bundle('scss/base.scss', filters='pyscss', output='css/all.css')
assets.register('scss_all', scss)

@app.route('/', methods=['GET'])
def index():
    if len(img_urls) < 15:
        for topic in ['baseball', 'food']:
            if len(img_urls) > 15:
                continue
            for result in google.search(topic, 1):
                content = urllib2.urlopen(result.link).read()
                soup = BeautifulSoup(content, 'html.parser')
                for link in soup.find_all('img'):
                    if link.get('src'):
                        img_urls.append(link.get('src'))
    if request.method == 'GET':
        return render_template('index.html', urls=img_urls)
    return render_template('404.html')

if __name__ == '__main__':
    img_urls = []
    app.run()
