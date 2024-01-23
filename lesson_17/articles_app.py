from dataclasses import dataclass
import sqlite3


@dataclass
class Article:
    id: int
    title: str
    text: str
    author: str
    like_count: int


def get_all_articles() -> list[Article]:
    with sqlite3.connect('Flask.db') as connection:
        result = connection.execute('SELECT * FROM article')
        return [Article(id=i[0], title=i[1], text=i[2], author=i[3], like_count=i[4]) for i in result.fetchall()]


def get_article(article_id):
    with sqlite3.connect('Flask.db') as connection:
        result = connection.execute('SELECT * FROM article WHERE id = ?', (article_id,))
        answer = [Article(id=i[0], title=i[1], text=i[2], author=i[3], like_count=i[4]) for i in result.fetchall()]
        if answer:
            return answer
        else:
            raise ValueError


def save_likes(article_id):
    likes = get_article(article_id)[0].like_count
    with sqlite3.connect('Flask.db') as connection:
        connection.execute('UPDATE article SET like_count = ? WHERE id = ?',
                           (likes + 1, article_id))
    return likes + 1

def delete_likes(article_id):
    likes = get_article(article_id)[0].like_count
    with sqlite3.connect('Flask.db') as connection:
        connection.execute('UPDATE article SET like_count = ? WHERE id = ?',
                           (likes - 1, article_id))
    return likes - 1

def reg_login(login, password):
    with sqlite3.connect('Flask.db') as connection:
        result = connection.execute("SELECT id , login FROM users")
        for i in result.fetchall():
            if login in i[1]:
                return True
        connection.execute("INSERT INTO users(login, password)"
                                "VALUES (?, ?);",
                           (login, password))

        return i[0]


def check_login(login, password):
    with sqlite3.connect('Flask.db') as connection:
        result = connection.execute("SELECT * FROM users")
        authorization = None
        for i in result.fetchall():
            if login == i[1] and password == i[2]:
                authorization = i[0]
        return authorization


def save_article(article: Article):
    print(article.id)
    with sqlite3.connect('Flask.db') as connection:
        connection.execute('UPDATE article SET title = ?, text = ?, author = ?, like_count = ? WHERE id = ?',
                           (article.title, article.text, article.author, article.like_count, article.id))

# print(get_article(int(input())))
# print(get_all_articles())
# article = Article(id=1, title='Snakessss', text='Snakessss', author='Ydav', like_count=0)
# print(save_article(article))
#print(check_login("Maxim", "1111"))