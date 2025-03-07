import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def test_model_prediction():
    test_input = np.array([50, 83311, 13, 0, 0, 40]).reshape(1, -1)
    pred = model.predict(test_input)
    assert pred in [0, 1], "Model prediction is invalid"
