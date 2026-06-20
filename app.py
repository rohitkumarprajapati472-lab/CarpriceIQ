from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and encoders
with open("car_price_model.pkl", "rb") as f:
    artifacts = pickle.load(f)

model = artifacts["model"]
le_brand = artifacts["le_brand"]
le_model = artifacts["le_model"]
le_fuel = artifacts["le_fuel"]
le_owner = artifacts["le_owner"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        brand = request.form["brand"].strip()
        model_name = request.form["model"].strip()
        year = int(request.form["year"])
        km = float(request.form["km"])
        fuel = request.form["fuel"].strip()
        owner = request.form["owner"].strip()
        seats = int(request.form["seats"])

        print("Brand entered:", brand)
        print("Available brands:", le_brand.classes_)

        brand = le_brand.transform([brand])[0]
        model_name = le_model.transform([model_name])[0]
        fuel = le_fuel.transform([fuel])[0]
        owner = le_owner.transform([owner])[0]

        data = np.array([[
            brand,
            model_name,
            year,
            km,
            fuel,
            owner,
            seats
        ]])

        prediction = model.predict(data)[0]

        return render_template(
            "index.html",
            prediction=f"₹ {prediction:,.0f}",
            form_data=request.form
        )

    except Exception as e:
        print("ERROR:", e)

        return render_template(
            "index.html",
            prediction=f"Error: {str(e)}",
            form_data=request.form
        )


if __name__ == "__main__":
    app.run(debug=True)