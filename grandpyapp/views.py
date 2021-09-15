from flask import Flask, render_template, request, jsonify, json
import inputWords
import json
import random
# coding: utf-8

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/process', methods=['POST', 'GET'])
    def process_wiki():
        question_input = request.form["question_input"]
        if question_input:
            test_input = inputWords.main(question_input)
            if test_input["status"] == "ok":
                with open('anecdote.json', encoding="utf-8") as rand_anecdo:
                    data = json.load(rand_anecdo)
                    anecdote = random.choice(data["anecdote_wiki"])
                    anecdote_map = random.choice(data["anecdote_google"])
                    address = test_input["google_map"]["adresse"]
                lon=test_input["google_map"]["longitude"]
                lat=test_input["google_map"]["latitude"]
                return jsonify({'status':test_input["status"],
                    'question_input' : anecdote_map +
                    str(address) + ". sa latitude et sa longitude sont: "+
                    str(lat) +" et "+ str(lon), 'wiki_input' : anecdote +
                    test_input["wiki"], 'longitude_input':lon,
                    'latitude_input':lat})
            else:
                with open('anecdote.json', encoding="utf-8") as rand_anecdo:
                    data = json.load(rand_anecdo)
                    anecdote_unknown = random.choice(data["unknown"])
                    return jsonify({'status':test_input["status"],
                        'question_input' : anecdote_unknown})


    return app

if __name__ == "__main__":
    create_app().run(debug=True)
