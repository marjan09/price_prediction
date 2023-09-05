from flask import Flask
from flask import request, jsonify
from pandas import json_normalize
from main import run_model
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/predict', methods=['GET'])
def predict():
    brand = request.args.get('brand')
    fuel = request.args.get('fuel')
    gearbox = request.args.get('gearbox')
    year = request.args.get('year')
    mileage = request.args.get('mileage')

    if not (brand or fuel or gearbox or year or mileage):
        return jsonify({'error': 'Input can not be empty - Please provide a value '})

    dict_for_df = {'brand': brand,
                   'fuel': fuel,
                   'gearbox': gearbox,
                   'year': year,
                   'mileage (kms)': mileage}

    df = json_normalize(dict_for_df)

    pred = run_model(df)

    return jsonify({'price': (pred.item())})


if __name__ == '__main__':
    app.run(debug=True)


