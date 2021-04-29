from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'get_your_own_key_lmaoooooo'

# Flask-Bootstrap requires this line
Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField('PENIS LENGTH INTEGER ONLY', validators=[DataRequired()])
    submit = SubmitField('Submit')

    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = NameForm()
        peen = ""
        if form.validate_on_submit():
            length = int(form.name.data)
            peen = "B"
            for x in range(0, length):
                peen = peen + "="
            peen = peen + "D"

        else:
            peen = "NO PENIS"
        return render_template('index.html', form=form, peen=peen)


if __name__ == "__main__":
    app.run(threaded=True)