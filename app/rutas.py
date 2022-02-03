from app import app


@app.route('/')
def Index():
    return "<h1>Hola mundo!</h1>"