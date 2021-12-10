from flask import Flask, render_template
app = Flask(__name__)
from bs4 import BeautifulSoup
import urllib.request, webbrowser


@app.route('/',methods=("GET", "POST"), strict_slashes=False)
def index():
	login = scrapper('facebook')
	webbrowser.open(login)
	return render_template("index.html")

def scrapper(query):
    url = 'https://google.com/search?q='+query

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
    link = link + '/login'
    return link

if __name__ == '__main__':
	app.run(debug=True)