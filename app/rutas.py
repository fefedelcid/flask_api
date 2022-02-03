from app import app


@app.route('/')
def Index():
    return {"Hola":"Mundo"}