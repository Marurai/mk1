from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bonjour, voici mon site déployé avec Railway !"

if __name__ == "__main__":
    app.run(debug=True)
