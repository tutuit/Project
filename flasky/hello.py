from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    dataset = None
    now = None

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        import mysql.connector
        import datetime

        now = datetime.datetime.now()
        db = mysql.connector.connect(host='localhost', user='test', password='TESTtest123', database='asset')
        cur = db.cursor()
        cur.execute('SELECT * FROM asset_info WHERE Location=%s', (name,))
        dataset = cur.fetchall()
    return render_template('index.html', form=form, name=name, comments=dataset, currenttime=now)
ggggg
G   grant

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/test')
def get_data_fromdb():
    import mysql.connector
    import datetime

    now =datetime.datetime.now()
    db = mysql.connector.connect(host='localhost', user='test', password='TESTtest123', database='asset')
    cur = db.cursor()
    cur.execute('SELECT * FROM asset_info')
    dataset = cur.fetchall()

    return render_template('test.html', comments=dataset, currenttime=now)


@app.route('/onlyfortest')
def fortestuse():
    return render_template('onlyfortest.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


class NameForm(Form):
    name = StringField('What is your location?', validators=[DataRequired()])
    submit = SubmitField('Submit')

if __name__ == '__main__':
    app.run(debug=True)





# manager = Manager(app)
#
# if __name__ == '__main__':
#     manager.run()
