from app import app


@app.route('/')
def Index():
    print('index!')
    return "<h1>Hola mundo!</h1>"
