from flask import Flask, render_template, Response
from flask_bootstrap import Bootstrap
from questionnaire.forms import formLPP, formUEI
from io import StringIO


class LPPData:
    def __init__(self):

        self.data = list()

    def generate_file(self):

        msg = "itemID,answer\n"

        for item in self.data:
            msg += '{},{}\n'.format(item[0], item[1])
        file_buffer = StringIO(msg)
        file_buffer.seek(0)
        return file_buffer


class UEIData:
    def __init__(self):

        self.data = list()

    def generate_file(self):

        msg = "itemID,answer\n"

        for item in self.data:
            msg += '{},{}\n'.format(item[0], item[1])
        file_buffer = StringIO(msg)
        file_buffer.seek(0)
        return file_buffer

    def score(self, id, score):

        scoring_map = {'1': {'c1': 1, 'c2': 2, 'c3':3},
                       '2': {'c1': 1, 'c2': 2, 'c3':3},
                       '3': {'c1': 1, 'c2': 2, 'c3':3},
                       '4': {'c1': 1, 'c2': 2, 'c3':3},
                       '5': {'c1': 1, 'c2': 2, 'c3':3},
                       '6': {'c1': 1, 'c2': 2, 'c3':3},
                       '7': {'c1': 1, 'c2': 2, 'c3':3},
                       '8': {'c1': 1, 'c2': 2, 'c3':3},
                       '9': {'c1': 1, 'c2': 3},
                       '10': {'c1': 1, 'c2': 3},
                       '11': {'c1': 1, 'c2': 3},
                       '12': {'c1': 1, 'c2': 2, 'c3':3},
                       '13': {'c1': 1, 'c2': 2, 'c3':3},
                       '14': {'c1': 1, 'c2': 3},
                      }
        id_score = scoring_map[id]
        return id_score[score]

app = Flask(__name__)
bootstrap = Bootstrap(app)
lpp_val = LPPData()
uei_val = UEIData()

@app.route('/')
@app.route('/index')
def index():
    return render_template('intro.html')


@app.route('/select_questionnaire', methods=['GET', 'POST'])
def select_questionnaire():
    return render_template('select_questionnaire.html')

@app.route('/questionnaire_lpp', methods=['GET', 'POST'])
def questionnaire_lpp():
    form = formLPP()
    print("here")

    if form.validate_on_submit():
        lpp_val.data.clear()
        lpp_val.data.append(['A',form.a.data])
        lpp_val.data.append(['B',form.b.data])
        lpp_val.data.append(['C',form.c.data])
        lpp_val.data.append(['D',form.d.data])
        lpp_val.data.append(['E',form.e.data])
        lpp_val.data.append(['F',form.f.data])
        lpp_val.data.append(['G',form.g.data])
        lpp_val.data.append(['H',form.h.data])
        lpp_val.data.append(['I',form.i.data])
        lpp_val.data.append(['J',form.j.data])
        lpp_val.data.append(['K',form.k.data])
        lpp_val.data.append(['L',form.l.data])
        lpp_val.data.append(['M',form.m.data])
        lpp_val.data.append(['N',form.n.data])

        print("Data Validated")
        print(lpp_val.data)
        form.validated = True
    return render_template('questionnaire_lpp.html', form=form)

@app.route('/questionnaire_uei', methods=['GET', 'POST'])
def questionnaire_uei():
    form = formUEI()
    print("UHEI: here")
    if form.validate_on_submit():
        print("Data validated")
        uei_val.data.clear()
        uei_val.data.append(['1',uei_val.score('1', form.a.data)])
        uei_val.data.append(['2',uei_val.score('2', form.b.data)])
        uei_val.data.append(['3',uei_val.score('3', form.c.data)])
        uei_val.data.append(['4',uei_val.score('4', form.d.data)])
        uei_val.data.append(['5',uei_val.score('5', form.e.data)])
        uei_val.data.append(['6',uei_val.score('6', form.f.data)])
        uei_val.data.append(['7',uei_val.score('7', form.g.data)])
        uei_val.data.append(['8',uei_val.score('8', form.h.data)])
        uei_val.data.append(['9',uei_val.score('9', form.i.data)])
        uei_val.data.append(['10',uei_val.score('10', form.j.data)])
        uei_val.data.append(['11',uei_val.score('11', form.k.data)])
        uei_val.data.append(['12',uei_val.score('12', form.l.data)])
        uei_val.data.append(['13',uei_val.score('13', form.m.data)])
        uei_val.data.append(['14',uei_val.score('14', form.n.data)])

        form.validated = True

    return render_template('questionnaire_uei.html', form=form)

@app.route("/download", methods=['GET', 'POST'])
def download(file_name='lpp'):
    generated_file = lpp_val.generate_file()
    response = Response(generated_file, mimetype="text/csv")
    # add a filename
    response.headers.set(
        "Content-Disposition", "attachment", filename="{0}.csv".format(file_name)
    )
    return response


@app.route("/download_uei", methods=['GET', 'POST'])
def download_uei(file_name='uei'):
    generated_file = uei_val.generate_file()
    response = Response(generated_file, mimetype="text/csv")
    # add a filename
    response.headers.set(
        "Content-Disposition", "attachment", filename="{0}.csv".format(file_name)
    )
    return response


def main():
    app.config['SECRET_KEY'] = 'any secret string'
    app.run(debug=True)

if __name__ == "__main__":
    main()