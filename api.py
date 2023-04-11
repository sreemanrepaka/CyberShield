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
    sentiments = ["age", "not bullying", "miscellaneous","racism", "religion", "gender"]
    all_categories_names = np.array(sentiments)
    return all_categories_names[prediction]

@app.route('/predict', methods=['GET'])
def web_scrape():
    # "C:\Users\sreem\Downloads\chromedriver_win32\chromedriver.exe"
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode

    # Set up ChromeDriver executable path
    chromedriver_path = r'C:\Users\sreem\Downloads\chromedriver_win32\chromedriver.exe'
    service = Service(executable_path=chromedriver_path)
    # Create a new ChromeDriver instance with the service and options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get('http://localhost:8080')

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
    import requests

    # Wait for the div to be loaded
    try:
        # Wait for the div element to be present
        divs = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.q-list.q-pa-sm'))
        )

        # Print the text contents of the div element
        lst = []
        res=[]
        for div in divs:
            tweets = div.text.split('\n')
            lst.append(tweets[1])
        for i in lst:
            url = 'http://127.0.0.1:5000/predict'
            myobj = {'text': i}

            x = requests.post(url, json=myobj)
            res.append(x.text)
        return res




    except TimeoutException:
        print("Timed out waiting for the div element to be present")

    finally:
        # Quit the driver
        driver.quit()




# Run the app
if __name__ == '__main__':
    app.run(debug=True)




