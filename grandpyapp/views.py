from flask import Flask, render_template, request, jsonify
import inputWords
import json
import random

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
            with open('anecdote.json') as random_anecdote:
                data = json.load(random_anecdote)
                anecdote = random.choice(data["anecdote_wiki"])
            return jsonify({'question_input' : anecdote + test_input["wiki"]})
            #return jsonify({'question_input' : anecdote + str(test_input["google_map"]["longitude"])})

    return app

if __name__ == "__main__":
    create_app().run(debug=True)
