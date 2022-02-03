from app import app


@app.route('/')
@app.route('/api')
def Index():
    return {"Hola":"Mundo"}