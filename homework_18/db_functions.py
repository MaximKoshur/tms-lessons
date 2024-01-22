from dataclasses import dataclass
import sqlite3


@dataclass
class Product:
    id: int
    name: str
    description: str
    category_id: int


def load_product() -> list[Product]:
    with sqlite3.connect('Product.db') as connection:
        result = connection.execute('SELECT * FROM Product')
        return [Product(id=i[0], name=i[1], description=i[2], category_id=i[3]) for i in result.fetchall()]


def load_category(category_id) -> list[Product]:
    with sqlite3.connect('Product.db') as connection:
        result = connection.execute('SELECT category.name,Product.id FROM Product JOIN category ON '
                                    'Product.category_id = category.id WHERE Product.category_id = ?', (category_id,))
        answer = result.fetchall()
        category = answer[0][0]
        answer = [i[1] for i in answer]
        answer.insert(0, category)
        if answer:
            return answer
        else:
            raise ValueError


def load_product_id(product_id):
    with sqlite3.connect('Product.db') as connection:
        result = connection.execute('SELECT * FROM Product WHERE id = ?', (product_id,))
        answer = [Product(id=i[0], name=i[1], description=i[2], category_id=i[3]) for i in result.fetchall()]
        if answer:
            return answer
        else:
            raise ValueError
#
#
# def save_likes(article_id):
#     likes = get_article(article_id)[0].like_count
#     with sqlite3.connect('Flask.db') as connection:
#         connection.execute('UPDATE article SET like_count = ? WHERE id = ?',
#                            (likes + 1, article_id))
#     return likes + 1
#
#
# def save_article(article: Article):
#     print(article.id)
#     with sqlite3.connect('Flask.db') as connection:
#         connection.execute('UPDATE article SET title = ?, text = ?, author = ?, like_count = ? WHERE id = ?',
#                            (article.title, article.text, article.author, article.like_count, article.id))

# print(get_article(int(input())))
# print(get_all_articles())
# article = Article(id=1, title='Snakessss', text='Snakessss', author='Ydav', like_count=0)
# print(save_article(article))
print(load_category(2))