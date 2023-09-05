import pandas as pd
import datetime
from joblib import load, dump
from sklearn.preprocessing import OneHotEncoder

brands = ['Abarth', 'Alfa', 'Audi', 'BMW', 'Chevrolet', 'Citroen', 'Cupra', 'DS', 'Dacia', 'Fiat', 'Ford', 'Honda',
          'Hyundai', 'Jaguar', 'Jeep', 'Kia', 'Land', 'Lexus', 'Mazda', 'Mercedes', 'Mini', 'Mitsubishi', 'Nissan',
          'Opel', 'Peugeot', 'Porsche', 'Renault', 'SEAT', 'Skoda', 'Smart', 'Ssangyong', 'Subaru', 'Suzuki',
          'Toyota', 'Volkswagen', 'Volvo']
fuels = ['Diésel', 'Eléctrico', 'GLP', 'Gasolina', 'Híbrido']
gearboxes = ['Automatica', 'Manual']


def run_model(df):
    regr = load('model.joblib')

    X_categorical = df[['brand', 'fuel', 'gearbox']]

    enc = OneHotEncoder(categories=[brands, fuels, gearboxes], handle_unknown='ignore')

    X_categorical_encoded = pd.DataFrame(enc.fit_transform(X_categorical).toarray())

    year = datetime.datetime.now().year

    df['age'] = year - df['year'].astype('int')

    X_numerical = df[['age', 'mileage (kms)']]

    X = pd.concat([X_numerical, X_categorical_encoded], axis=1)

    X.columns = X.columns.astype(str)

    predictions = regr.predict(X)

    return predictions
