from flask import Flask, abort, request, redirect, session
import articles_app
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)




@app.route('/')
@app.route('/login')
def login_page():
    session["is_authorized"] = False
    return(f'<html><head><title>Login</title></head>'
                f'<body><h1>Введите логин и пароль для входа:</h1>'
                f'<ul></ul>'
                f'<form action="/check_login" method="post">Login: <input type = "text" name = "login"><br>Password: <input type = "text" name = "password"><br>'
                f'<input type="submit" value="Sign in"></form><a href="/registrate">Зарегистрироваться</a></body>'
                f'</html>')

@app.route('/registrate')
def registrate_page():
    session["is_authorized"] = False
    return(f'<html><head><title>Registrate</title></head>'
                f'<body><h1>Введите логин и пароль для регистрации:</h1>'
                f'<ul></ul>'
                f'<form action="/registrate_login" method="post">Login: <input type = "text" name = "login"><br>Password: <input type = "text" name = "password"><br>'
                f'<input type="submit" value="Sign in"></form><a href="/login">Залогиниться</a></body>'
                f'</html>')

@app.route('/registrate_login', methods=['POST'])
def registrate_login():
    login = request.form.get('login')
    password = request.form.get('password')
    if len(login) == 0 or len(password) == 0:
        return redirect("http://127.0.0.1:8080/registrate", code=302)
    result = articles_app.reg_login(login, password)
    if result is True:
        return redirect("http://127.0.0.1:8080/login", code=302)
    else:
        session["user_id"] = result
        session["is_authorized"] = True
        return redirect("http://127.0.0.1:8080/articles", code=302)

@app.route('/check_login', methods=['POST'])
def check_login():
    login = request.form.get('login')
    password = request.form.get('password')
    user_id = articles_app.check_login(login, password)
    if user_id != None:
        session["user_id"] = user_id
        session["is_authorized"] = True
        return redirect("http://127.0.0.1:8080/articles", code=302)
    else:
        return redirect("http://127.0.0.1:8080/login", code=302)


@app.route('/articles')
def main_page():
    if session.get("is_authorized") != True:
        return redirect("http://127.0.0.1:8080/login", code=302)
    result = articles_app.get_all_articles()
    articles_html = '\n'.join(
        f'<li><a href="/article/{article.id}">{article.title}</a></li>'
        for article in result)
    return (f'<html><head><title>Articles APP</title></head>'
            f'<body><h1>All Articles</h1>'
            f'<ul>{articles_html}</ul>'
            f'</body>'
            f'</html>')


@app.route('/article/like', methods=['POST'])
def likes():
    article_id = request.form.get('article_id')
    if session.get(article_id):
        session[article_id] = False
        articles_app.delete_likes(article_id)
        return redirect(f"http://127.0.0.1:8080/article/{article_id}", code=302)
    else:
        session[article_id] = True
        articles_app.save_likes(article_id)
        return redirect(f"http://127.0.0.1:8080/article/{article_id}", code=302)

@app.route('/article/<int:article_id>')
def article_page(article_id: int):
    if session.get("is_authorized") != True:
        return redirect("http://127.0.0.1:8080/login", code=302)
    article = articles_app.get_article(article_id)
    if article[0] == []:
        abort(404, "Article not found")
    else:
        return (f'<html><head><a href="/articles">Main Page</a><title>Articles APP</title></head>'
                f'<body><h1>{article[0].title}</h1><h2>{article[0].author}</h2>'
                f'<ul><li>{article[0].text}</li></ul>'
                f'<form action="/article/like" method="post"><input type = "submit" value = "Like:"">{article[0].like_count}'
                f'<input type="hidden" value="{article[0].id}"name="article_id"/></form></body>'
                f'</html>')


if __name__ == '__main__':
    app.run(port=8080, debug=True)

# /Name?name =
