import numpy as np
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS
# Load the model that you just saved
lr = joblib.load("model.pkl")
cv=joblib.load('vectorizer.pkl')
tfidf=joblib.load('transformer.pkl')


app = Flask(__name__)
CORS(app)

# Define a POST endpoint for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input text from the request

    input_text = request.json['text']
    print(input_text)
    if not input_text:
        print("empty")

    # Transform the input text using the loaded vectorizer and transformer
    input_text_cv = cv.transform([input_text])
    input_text_tf = tfidf.transform(input_text_cv)

    # Make a prediction on the transformed input text
    prediction = lr.predict(input_text_tf)[0].tolist()

    # Return the prediction as a JSON response
    # prediction=jsonify({'prediction': prediction})
    sentiments = ["age", "not bullying", "racism", "religion", "gender"]
    all_categories_names = np.array(sentiments)
    return all_categories_names[prediction]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)




