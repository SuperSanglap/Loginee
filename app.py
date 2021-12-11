from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from bs4 import BeautifulSoup
import urllib.request


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/', methods = ['POST'])
def my_form_post():
	text = request.form['text']
	text = text.replace("login", " ")
	text = text.replace(" ", "+")
	login = scrapper(text)
	return redirect(login)

def scrapper(query):
    url = f'https://google.com/search?q={query}+login'

    request = urllib.request.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    raw_response = urllib.request.urlopen(request).read()
    html = raw_response.decode("utf-8")

    soup = BeautifulSoup(html, 'html.parser')

    divs = soup.select("#search div.g")
    for div in divs:
        results = div.select("cite")

        if (len(results) >= 1):
            link = results[0]
            link = link.get_text()
            break
    link = link.replace(" ", "")
    link = link.replace("›", "/")
    return link

if __name__ == '__main__':
	app.run()