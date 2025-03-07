import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset (UCI Adult Income Dataset)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
columns = ["age", "workclass", "fnlwgt", "education", "education_num",
           "marital_status", "occupation", "relationship", "race", "sex",
           "capital_gain", "capital_loss", "hours_per_week", "native_country", "income"]
data = pd.read_csv(url, names=columns, na_values=" ?", skipinitialspace=True)

# Data preprocessing
data = data.dropna()
data["income"] = data["income"].apply(lambda x: 1 if x == ">50K" else 0)
X = data.select_dtypes(include=["int64", "float64"])  # Select numerical features
y = data["income"]

# Train a model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
