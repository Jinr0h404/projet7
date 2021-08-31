from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST', 'GET'])
def process():
    question_input = request.form["question_input"]
    if question_input:
        print("ok")
        return jsonify({'question_input' : question_input})
    

if __name__ == "__main__":
    app.run(debug=True)
