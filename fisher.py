from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'hello'

@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    q:普通关键字 & isbn
    start
    page
    isbn
    :return:
    """
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    short_q = q.replace('-', '')
    if '-' in q and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'
    pass

app.run()