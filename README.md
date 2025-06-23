# House-Price-Predictor
House Price Prediction
🏡 House Price Prediction App

This project is a Streamlit-based web app that predicts house prices based on property features such as area income, number of rooms, and local population statistics. The model is trained using Linear Regression on a real-world dataset from Kaggle.

📂 Project Structure

app.py: Streamlit web app

train_model.py: Script to train and save the machine learning model

housing.csv: Dataset file (downloaded from Kaggle)

model.joblib: Saved regression model (generated after training)

README.md: Project documentation

📦 Features

Interactive user interface using Streamlit

Predicts house prices from five numeric inputs

Uses a machine learning pipeline with scaling and regression

Displays predicted price in USD

📈 Features Used for Prediction

Avg. Area Income

Avg. Area House Age

Avg. Area Number of Rooms

Avg. Area Number of Bedrooms

Area Population

📊 Dataset

Dataset used: "Housing Prices Dataset" from Kaggle
Link: https://www.kaggle.com/datasets/yasserh/housing-prices-dataset
You need to download this file, rename it to housing.csv, and place it in the project folder.

🚀 Setup & Usage

Clone the repository and navigate to the project directory

Install requirements using pip install -r requirements.txt

Run train_model.py to train and save the model

Launch the web app with streamlit run app.py

🧪 Example Output

💰 Estimated House Price: $421,903.57

💻 Tech Stack

Python

Pandas and Scikit-learn for modeling

Streamlit for the web interface

Joblib for saving the model

🧠 Future Improvements

Add support for Gradient Boosting or XGBoost

Visualize feature importances and distributions

Deploy the app using Streamlit Cloud or Hugging Face Spaces

📬 Contact

For questions or support, reach out via email or GitHub.
Email: hafizumair07.hm@gmail.com

GitHub: github.com/Mohammed-Umair30 
