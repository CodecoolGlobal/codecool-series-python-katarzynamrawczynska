from flask import Flask, render_template, url_for
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')

@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/shows/most-rated/<int:id>')
def most_rated(id):
    offset = (id-1)*15
    shows = queries.get_most_rated_shows(offset)
    #shows = shows[::-1]
    return render_template('most-rated.html', shows=shows)

@app.route('/tv-show/<int:show_id>', methods=["GET", "POST"])
def show(show_id):
    shows = queries.get_all_shows()
    return render_template("show.html", shows=shows, show_id=show_id)

def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
