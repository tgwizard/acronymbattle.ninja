from flask import Flask, render_template, request, abort

from abn.repos import CompetitionRepo


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', competitions=CompetitionRepo.list())


@app.route('/competitions/<slug>', methods=['GET'])
def start_competition(slug):
    competition = CompetitionRepo.get(slug)
    if not competition:
        abort(404)

    return render_template('competition.html', competition=competition, answers=[], index=1)


@app.route('/competitions/<slug>', methods=['POST'])
def show_acronym(slug):
    competition = CompetitionRepo.get(slug)
    if not competition:
        abort(404)

    index = int(request.form['index'])
    answer = request.form['answer']
    answers = request.form.getlist('answers')

    answers.append(answer)

    if index < 1 or index > len(competition.acronyms):
        abort(404)
    if index == len(competition.acronyms):
        return show_result(competition, answers)

    return render_template('competition.html', competition=competition, answers=answers, index=index+1)


def show_result(competition, answers):
    class Result(object):
        def __init__(self, acronym, answer):
            self.acronym = acronym
            self.answer = answer
            self.is_correct = self._is_correct()

        def _is_correct(self):
            answer = self.answer.replace('-', ' ').lower()
            correct_answer = self.acronym.answer.replace('-', ' ').lower()
            return answer == correct_answer

    results = [Result(acronym, answer) for acronym, answer in zip(competition.acronyms, answers)]
    num_correct = len([x for x in results if x.is_correct])
    num_total = len(competition.acronyms)

    return render_template(
        'result.html',
        competition=competition,
        results=results,
        num_correct=num_correct,
        num_total=num_total
    )
