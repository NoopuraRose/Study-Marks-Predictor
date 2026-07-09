import joblib
from flask import Flask,request

app = Flask(__name__)
model = joblib.load("study_marks_predictor_linreg.pkl")

@app.route("/test", methods = ["GET"])
def test():
    return "hello"

@app.route("/user", methods = ["POST"])
def user():
    input = request.get_json()
    print(input)
    study = input.get("study")
    print(study)
    new_marks = model.predict([[study]])
    result = round(new_marks[0][0], 2)
    print("Predicted marks = ", result)
    return {"marks": result}

if __name__ == "__main__":
    app.run()