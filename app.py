from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

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

    brand = request.form["brand"]
    model_name = request.form["model"]
    year = int(request.form["year"])
    km = float(request.form["km"])
    fuel = request.form["fuel"]
    mileage = float(request.form["mileage"])
    transmission = request.form["transmission"]
    owner = request.form["owner"]
    engine = float(request.form["engine"])
    seats = int(request.form["seats"])

    brand = le_brand.transform([brand])[0]
    model_name = le_model.transform([model_name])[0]
    fuel = le_fuel.transform([fuel])[0]
    transmission = le_trans.transform([transmission])[0]
    owner = le_owner.transform([owner])[0]

    car_age = 2026 - year

    if car_age == 0:
        car_age = 1

    km_per_year = km / car_age
    engine_per_seat = engine / seats

    data = np.array([[
        brand,
        model_name,
        km,
        fuel,
        mileage,
        transmission,
        owner,
        engine,
        seats,
        car_age,
        km_per_year,
        engine_per_seat
    ]])

    prediction = model.predict(data)[0]

    return render_template(
        "index.html",
        prediction=f"₹ {prediction:,.0f}",
        form_data=request.form
    )


if __name__ == "__main__":
    app.run(debug=True)