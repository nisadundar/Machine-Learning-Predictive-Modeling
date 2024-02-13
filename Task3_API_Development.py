from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Flask uygulamasını başlat
app = Flask(__name__)

# Eğitilmiş modeli yükle
file_path = 'C:/Users/user/Desktop/assigment/random_forest_model.pkl'
model = joblib.load(file_path)

# Tahmin fonksiyonu
def predict(input_data):
    # Girdiyi DataFrame'e dönüştür
    input_df = pd.DataFrame(input_data, index=[0])
    prediction = model.predict(input_df)
    return prediction

# API endpoint'i
@app.route('/predict', methods=['POST'])
def get_prediction():
    # Gelen isteği JSON olarak al
    input_data = request.get_json()
    # Tahmini al
    prediction = predict(input_data)
    # Tahmini JSON olarak dön
    return jsonify({'prediction': prediction.tolist()})

# test.py
import requests

url = 'http://127.0.0.1:5000/predict'
my_obj = {
    'sepal_length': 5.1,
    'sepal_width': 3.5,
    'petal_length': 1.4,
    'petal_width': 0.2
}

response = requests.post(url, json=my_obj)

print(response.json())



if __name__ == '__main__':
    app.run(debug=True)


