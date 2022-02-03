from app import app, render_template


@app.route('/')
def Index():
    print('index!')
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")