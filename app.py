from flask import Flask, request, jsonify
import mlflow.pyfunc
import pandas as pd

app = Flask(__name__)

import mlflow

mlflow.set_tracking_uri('http://localhost:5000')


@app.route('/dont_miss_hits', methods=['POST'])
def dont_miss_hits():
    # model = mlflow.pyfunc.load_model("models:/Spotify_dont_miss_hits/1")
    model = mlflow.pyfunc.load_model("local_models/model_dont_miss_hits/")
    data = request.get_json()
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)
    return jsonify({'prediction': prediction.tolist()})

@app.route('/dont_overestimate', methods=['POST'])
def dont_overestimate():
    # model = mlflow.pyfunc.load_model("models:/Spotify_dont_overestimate/1")
    model = mlflow.pyfunc.load_model("local_models/model_dont_overestimate/")
    data = request.get_json()
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(port=8000, debug=True)


# mlflow-artifacts:/811932844240729824/3028e01f53df44a792c46490c946b2cd/artifacts/model/MLmodel
