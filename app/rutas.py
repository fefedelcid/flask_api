from app import app, render_template
from app.api import search_item, TEST_DATA

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


@app.route('/')
def Index():
    return render_template("index.html")


def items():
    return render_template("items.html")

@app.route('/items/')
@app.route('/items/<int:page>')
@app.route('/item/<int:id>')
def itemPage(id=None, page=0):
    item=TEST_DATA
    if id!=None:
        item = search_item(id)
    return render_template("items.html", id=id, item=item, page=page)