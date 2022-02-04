from app import app
from json import dump, load

def load_JSON_data(filename=""):
    global data
    with open(filename, "r") as f:
        data = load(f)
    return data

@app.route('/api/')
@app.route('/api/items/')
def api_home():
    return data


@app.route('/api/item/<int:id>')
def api_product(id):
    return search_item(id)

def search_item(id):
    for prod in data['products']:
        if prod["id"] == id:
            return prod

TEST_DATA = load_JSON_data('app\static\data_test.json')
