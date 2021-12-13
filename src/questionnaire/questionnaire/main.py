from flask import Flask, render_template, Response
from flask_bootstrap import Bootstrap
from questionnaire.forms import formLPP
from io import StringIO
class LPPData:
    def __init__(self):

        self.data = list()
        self.a = 5
        self.b = 5

    def generate_file(self):

        msg = "type;value\n"

        for item in self.data:
            msg += '{};{}\n'.format(item[0], item[1])
        file_buffer = StringIO(msg)
        file_buffer.seek(0)
        return file_buffer

app = Flask(__name__)
bootstrap = Bootstrap(app)
lpp_val = LPPData()

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
        lpp_val.data.append(['a',form.a.data])
        lpp_val.data.append(['b',form.b.data])
        lpp_val.data.append(['c',form.c.data])
        lpp_val.data.append(['d',form.d.data])
        lpp_val.data.append(['e',form.e.data])
        lpp_val.data.append(['f',form.f.data])
        lpp_val.data.append(['g',form.g.data])
        lpp_val.data.append(['h',form.h.data])
        lpp_val.data.append(['i',form.i.data])
        lpp_val.data.append(['j',form.j.data])
        lpp_val.data.append(['k',form.k.data])
        lpp_val.data.append(['l',form.l.data])
        lpp_val.data.append(['m',form.m.data])
        lpp_val.data.append(['n',form.n.data])

        print("Data Validated")
        print(lpp_val.data)
        form.validated = True
    return render_template('questionnaire_lpp.html', form=form)

@app.route('/questionnaire_uei', methods=['GET', 'POST'])
def questionnaire_uei():
    return render_template('questionnaire_uei.html')

@app.route("/download", methods=['GET', 'POST'])
def download(file_name='lpp'):
    generated_file = lpp_val.generate_file()
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