from flask import Flask, render_template, Response
from flask_bootstrap import Bootstrap
from forms import formLPP
from io import StringIO
class LPPData:
    def __init__(self):
        self.a = 5
        self.b = 5

    def generate_file(self):

        msg = "type;score\n"
        msg += '{};{}\n'.format('a', self.a)
        msg += '{};{}\n'.format('b', self.b)
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
        lpp_val.a = form.a.data
        lpp_val.b = form.b.data
        print("Data Validated")
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

if __name__ == "__main__":
    app.config['SECRET_KEY'] = 'any secret string'
    app.run(debug=True)