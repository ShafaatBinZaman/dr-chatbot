import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV


input_file = "data/training_data.csv"
df = pd.read_csv(input_file)


X = df.drop(columns=["disease_label"])  
y = df["disease_label"]  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


xgb_model = XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='mlogloss')


param_grid = {
    'n_estimators': [100, 200, 300],  
    'max_depth': [3, 6, 10], 
    'learning_rate': [0.01, 0.05, 0.1],  
    'subsample': [0.8, 0.9, 1.0],  
    'colsample_bytree': [0.8, 0.9, 1.0],  
}


grid_search = GridSearchCV(estimator=xgb_model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2, scoring='accuracy')


grid_search.fit(X_train, y_train)


best_xgb_model = grid_search.best_estimator_

y_pred = best_xgb_model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:")
print(classification_report(y_test, y_pred))


import joblib
model_filename = "disease_classifier_xgb_model.pkl"
joblib.dump(best_xgb_model, model_filename)
print(f"Model saved as: {model_filename}")
