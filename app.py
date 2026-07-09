import joblib
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

model = joblib.load("study_marks_predictor_linreg.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test", methods=["GET"])
def test():
    return "hello"


@app.route("/user", methods=["POST"])
def user():
    data = request.get_json()

    study = float(data.get("study"))

    prediction = model.predict([[study]])

    marks = round(prediction[0][0], 2)

    return jsonify({
        "marks": marks
    })


if __name__ == "__main__":
    app.run(debug=True)