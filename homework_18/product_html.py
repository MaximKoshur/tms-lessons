from flask import Flask, abort, request, redirect, session
import db_functions
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
@app.route('/products')
def main_page():
    result = db_functions.load_product()
    products = str()
    categories = str()
    for i in result:
        categories = categories + f'<a href="/Category/{i.category_id}">{db_functions.load_category(i.category_id)[0]}</a>' + '<br>'
    for i in result:
        if session[i.id]:
            products = products + (f'<li><a href="/products_favorite/{i.id}">{i.name}</a></li>') + '\n'
        else:
            products = products + (f'<li><a href="/products/{i.id}">{i.name}</a></li>') + '\n'

    return (f'<html><head>{categories}<a href="/favorites_page">Favorites Products</a><title>Products</title></head>'
            f'<body><h1>All Products</h1>'
            f'<ul>{products}</ul>'
            f'</body>'
            f'</html>')


@app.route('/Category/<int:category_id>')
def categories_page(category_id):
    result = db_functions.load_category(category_id)
    name = result[0]
    result.pop(0)
    products = str()
    for i in result:
        product = db_functions.load_product_id(i)
        if session[product[0].id]:
            products = products + (f'<li><a href="/products_favorite/{product[0].id}">{product[0].name}</a></li>') + '\n'
        else:
            products = products + (f'<li><a href="/products/{product[0].id}">{product[0].name}</a></li>') + '\n'

    return (f'<html><head><a href="/products">Main Page</a><br><a href="/favorites_page">Favorites Products</a><title>Categories</title></head>'
            f'<body><h1>{name}</h1>'
            f'<ul>{products}</ul>'
            f'</body>'
            f'</html>')


@app.route('/favorites_page')
def favorites_page():
    result = db_functions.load_product()
    products = str()
    for i in result:
        if session[i.id]:
            products = products + (f'<li><a href="/products_favorite/{i.id}">{i.name}</a></li>') + '\n'
    if products == '':
        return(f'<html><head><a href="/products">Main Page</a><title>Favorite Products</title></head>'
            f'<body><h1>Favorite Products</h1>'
            f'<ul>No Favorite Products</ul>'
            f'</body>'
            f'</html>')
    return (f'<html><head><a href="/products">Main Page</a><title>Favorite Products</title></head>'
            f'<body><h1>Favorite Products</h1>'
            f'<ul>{products}</ul>'
            f'</body>'
            f'</html>')

@app.route('/products/<int:product_id>')
def article_page(product_id: int):
    product = db_functions.load_product_id(product_id)
    if product[0] == []:
        abort(404, "Product not found")
    else:
        session[product_id] = False
        return (f'<html><head><a href="/Category/{product[0].category_id}">{db_functions.load_category(product[0].category_id)[0]}</a><br><a href="/products">Main Page</a><br><a href="/favorites_page">Favorites Products</a><title>Product</title></head>'
                f'<body><h1>{product[0].name}</h1><h2>{product[0].description}</h2>'
                f'<ul></ul>'
                f'<form action="/favorites" method="post"><input type = "submit" value = "Добавить в избранное">'
                f'<input type="hidden" value="{product[0].id}"name="product_id"/></form>'
                f'</body>'
                f'</html>')


@app.route('/products_favorite/<int:product_id>')
def article_page_favorite(product_id: int):
    product = db_functions.load_product_id(product_id)
    if product[0] == []:
        abort(404, "Product not found")
    else:
        session[product_id] = True  #почемуууууууууу
        return (f'<html><head><a href="/Category/{product[0].category_id}">{db_functions.load_category(product[0].category_id)[0]}</a><br><a href="/products">Main Page</a><br><a href="/favorites_page">Favorites Products</a><title>Product</title></head>'
                f'<body><h1>{product[0].name}&#10027;</h1><h2>{product[0].description}</h2>'
                f'<ul></ul>'
                f'<form action="/unfavorites" method="post"><input type = "submit" value = "Убрать из избранного">'
                f'<input type="hidden" value="{product[0].id}"name="product_id"/></form>'
                f'</body>'
                f'</html>')


@app.route('/favorites', methods=['POST'])
def favorites():
    product_id = request.form.get('product_id')
    session[product_id] = True
    return redirect(f"/products_favorite/{product_id}", code=302)


@app.route('/unfavorites', methods=['POST'])
def unfavorites():
    product_id = request.form.get('product_id')
    session[product_id] = False
    return redirect(f"/products/{product_id}", code=302)


if __name__ == '__main__':
    app.run(port=8080, debug=True)