# 🚗 AI Car Price Predictor

A machine learning web application that estimates the resale price of a used car in Indian rupees. Enter a few details about the car and get an instant price estimate from a trained Random Forest model, served through a Flask web interface.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Random%20Forest-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

<!-- Add a screenshot of your app here:
![App Screenshot](screenshots/home.png)
-->

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [How to Use](#how-to-use)
- [Model Details](#model-details)
- [Model Performance](#model-performance)
- [Future Improvements](#future-improvements)
- [Author](#author)
- [License](#license)

---

## Overview

Pricing a used car is hard. This project trains a regression model on 12,000 used-car listings and exposes it through a clean web interface, so anyone can get a quick estimate without touching any code.

The user supplies seven details: brand, model, manufacturing year, kilometres driven, fuel type, owner type and number of seats. The app encodes these inputs, passes them to the trained model and displays the predicted price.

## Features

- **Instant price prediction** in Indian rupees (₹), also shown in lakh or crore
- **Live summary panel** that updates as the user fills in the form
- **Progress indicator** showing how many details have been entered
- **Input validation** in the browser, with clear error messages
- **Friendly error handling** when a brand or model is not recognised
- **Responsive design** that works on desktop, tablet and mobile
- **Accessible UI** with visible keyboard focus and reduced-motion support

## Tech Stack

| Area | Tools |
| --- | --- |
| Language | Python |
| Machine learning | scikit-learn (Random Forest Regressor), NumPy, pandas |
| Data analysis | Matplotlib, Seaborn |
| Web framework | Flask |
| Frontend | HTML, CSS, vanilla JavaScript |
| Model storage | Pickle |

## Project Structure

```
car-price-predictor/
├── app.py                  # Flask application
├── car_price_model.pkl     # Trained model and label encoders
├── Ml_model.ipynb          # Data analysis, training and evaluation notebook
├── templates/
│   └── index.html          # Web interface
├── static/
│   └── style.css           # Styling
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/rohitkumarprajapati472-lab/CarpriceIQ.git
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install the dependencies**

   ```bash
   pip install flask numpy scikit-learn pandas
   ```

   > The model file was saved with pickle, so use a scikit-learn version close to the one used for training. If you see a version warning, re-run the notebook to regenerate `car_price_model.pkl`.

4. **Run the app**

   ```bash
   python app.py
   ```

5. **Open your browser** and go to `http://127.0.0.1:5000`

## How to Use

1. Select the **brand** and type the **model** name.
2. Enter the **manufacturing year** and **kilometres driven**.
3. Choose the **fuel type**, **owner type** and **number of seats**.
4. Click **Get price estimate**.

**Example input**

| Field | Value |
| --- | --- |
| Brand | Tata |
| Model | Punch |
| Year | 2023 |
| KM driven | 15000 |
| Fuel | Petrol |
| Owner | First Owner |
| Seats | 5 |

Expected output: about **₹ 855,784**.

## Model Details

**Dataset:** 12,000 used-car listings (`car_ML_model.csv`).

**Input features (7):**

| Feature | Type |
| --- | --- |
| Brand | Categorical (label encoded) |
| Model | Categorical (label encoded) |
| Year | Numeric |
| KM driven | Numeric |
| Fuel type | Categorical (label encoded) |
| Owner type | Categorical (label encoded) |
| Seats | Numeric |

**Target:** Selling price

**Preprocessing:** missing `KM_Driven` values are filled with the median, and categorical columns are converted with `LabelEncoder`.

**Training:** 80/20 train-test split (`random_state=42`).

**Deployed model:** `RandomForestRegressor` with 200 trees (`n_estimators=200`, `random_state=42`). The model and all four encoders are saved together in `car_price_model.pkl`.

### Feature importance

| Feature | Importance |
| --- | --- |
| Year | 69.9% |
| KM driven | 23.4% |
| Model | 2.5% |
| Brand | 1.3% |
| Seats | 1.2% |
| Owner type | 0.9% |
| Fuel type | 0.9% |

The age of the car and the distance it has been driven account for most of the predicted price.

## Model Performance

Results on the 2,400-row test set:

| Model | MAE (₹) | R² Score |
| --- | --- | --- |
| Random Forest (deployed) | 57,011 | 0.867 |
| Custom Multiple Linear Regression | 53,492 | 0.885 |

The Random Forest explains about 87% of the variation in car prices, with an average error of roughly ₹57,000.

## Future Improvements

- Replace the free-text model field with a dropdown filtered by the selected brand
- Add more fuel types, such as Electric and LPG
- Add more features, such as transmission, engine size and mileage
- Retrain on a larger and more recent dataset
- Deploy to a cloud platform such as Render or Railway

## Author

**Your Name**
GitHub: [@your-username](https://github.com/rohitkumarprajapati472-lab/CarpriceIQ.git)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

⭐ If you found this project useful, consider giving it a star.