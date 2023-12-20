from flask import Flask
from deepcorrect import DeepCorrect

app = Flask(__name__)
@app.route("/")
def index() :
    with open("text.txt", "r") as f :
        txt = f.read()
        corrector = DeepCorrect('params_path', 'checkpoint_path')
        return corrector.correct(txt)

if __name__ == "__main__" :
    app.run(port=5000, debug=False)