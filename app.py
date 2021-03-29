from flask import Flask, render_template, abort, request, redirect, url_for
from models import db, User, Article, find_by_text
from flask_migrate import Migrate
import locale

locale.setlocale(locale.LC_ALL, '')
app = Flask(__name__)
app.secret_key = b'12#$%^&*hsyshsy'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def homepage():
    return render_template('index.html', title='Главная страница', articles=Article.query.all())


@app.route('/register')
def register():
    return render_template('Registration.html')


@app.route('/login')
def login():
    return render_template('Login.html')


@app.route('/search')
def search():
    text = request.args['text']
    result = Article.query.filter(db.or_(
        Article.title.like(f'%{text}%'),
        Article.body.like(f'%{text}%')
    )).all()


@app.route('/articles/new', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        img_url = request.form['img_url']
        title = request['title']
        body = request['body']

        article = Article(img_url=img_url, title=title, body=body)

        db.session.add(article)
        db.session.commit()

        return redirect(url_for('homepage'))

    return render_template('new_article.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run()
