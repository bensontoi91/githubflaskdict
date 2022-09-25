import os 

import requests
from requests.exceptions import HTTPError
from flask import Flask, render_template, request


app = Flask(__name__)
api_token = ''
def get_api_dictionary_response(word) -> dict:
    base_url= 'https://owlbot.info/api/v4/dictionary/'

    # headers={
    # 'Authorization':"Token "+ os.getenv('OWL_BOT_AUTH')
    # }
    headers={
    'Authorization':"Token "+ 'df4f180f13f8e9ab823909888384d9e7d1d265f9'
    }

    url = f'{base_url}{word}'

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print(response.status_code)
    return response.json()


@app.route("/", methods=['GET', 'POST']) 
def home():
    # if request.method == 'POST':
    word = request.form.get('word', 'dog').strip().lower()
    # try: 
    try: 
        data = get_api_dictionary_response(word)
    except HTTPError:
        data = None
    return render_template("index.html", data=data, word=word)


if __name__ == '__main__':
    app.run(debug=True,port=5020)

