from flask import Flask, render_template

from abn.repos import CompetitionRepo


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', competitions=CompetitionRepo.get_competitions())
