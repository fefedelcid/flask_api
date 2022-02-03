from app import app


@app.route('/')
def Index():
    print('index!')
    return "<h1>Hola mundo!</h1>"

@app.errorhandler(404)
def page_not_found(error):
    return "La página no existe."