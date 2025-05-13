# Activity Market Monitor

This project was developed as a capstone project during **The 100 Days of Code: The Complete Python Pro Bootcamp** course by **Angela Yu**.

It combines two main functionalities: tracking daily exercise and monitoring stock price changes to potentially send alerts, utilizing external APIs and services.

## Features

* **Workout Tracker:**
    * Allows the user to input natural language descriptions of exercises performed.
    * Uses the Nutritionix API to get detailed calorie and duration information for the exercise.
    * Sends the exercise details (Date, Time, Exercise, Duration, Calories) to a Google Sheet via the Sheety API.
* **Stock Price Alert:**
    * Fetches daily closing prices for a specified stock (default: TSLA) using the Alpha Vantage API.
    * Calculates the percentage change in the closing price between the two most recent days.
    * If the price change (up or down) is greater than a 5% threshold, it triggers a news alert (requires a separate `news` module).

## Prerequisites

Before running the project, ensure you have the following installed and set up:

* **Python 3.x**
* **Required Python Libraries:**
    * `requests`
    * `pandas`
    * `python-dotenv`
    You can install them using pip:
    ```bash
    pip install requests pandas python-dotenv
    ```
* **API Keys and Accounts:**
    * **Nutritionix API:** You need an API ID (`API_ID`) and API Key (`API_KEY`). Obtain these from the Nutritionix API website.
    * **Alpha Vantage API:** You need an API Key (`API_KEY_PRICE`). Obtain this from the Alpha Vantage API website.
    * **Google Account & Google Sheet:** A Google account and a Google Sheet to store your workout data. The sheet should have columns named exactly `Date`, `Time`, `Exercise`, `Duration`, and `Calories` (case-sensitive).
    * **Sheety Account & Project:** A Sheety account linked to your Google Sheet. Configure a project in Sheety for your sheet and set up Bearer Token authentication. Note down your Sheety POST URL (`SHEETY_POST_URL`) and your Bearer Token (`SHEETY_BEARER_TOKEN`).
    * **(Optional) News Module:** A Python module named `news.py` with a function `new_sender(change)` if you intend to use the stock alert feature to send notifications. (Note: This module is not included in the provided code snippets).

## Setup

1.  **Clone the repository (or download your project files):**
    ```bash
    git clone <your_repository_url>
    cd project_capstone
    ```
2.  **Create a `.env` file:** In the root directory of your project, create a file named exactly `.env`. This file will store your sensitive API keys and URLs.
    ```dotenv
    # .env file

    # Nutritionix API Keys
    API_ID=YOUR_NUTRITIONIX_APP_ID
    API_KEY=YOUR_NUTRITIONIX_API_KEY

    # Alpha Vantage API Key
    API_KEY_PRICE=YOUR_ALPHA_VANTAGE_API_KEY

    # Sheety API Details
    SHEETY_POST_URL=YOUR_SHEETY_POST_URL
    SHEETY_BEARER_TOKEN=YOUR_SHEETY_BEARER_TOKEN

    # Stock Symbol (Optional, default is TSLA)
    # STOCK=TSLA
    # COMPANY_NAME=Tesla Inc
    ```
    Replace the placeholder values (`YOUR_...`) with your actual keys, URLs, and token.

3.  **Configure Sheety:** Ensure your Sheety project is correctly linked to your Google Sheet and Bearer Token authentication is configured. Make sure the Object name in Sheety matches the top-level key used in your POST payload (`workout` in the current code) and that the Sheety API can access and edit your sheet.

4.  **Add `.env` to `.gitignore`:** To prevent accidentally committing your `.env` file, create or open the `.gitignore` file in your project's root and add the following line:
    ```gitignore
    /.env
    ```
    Commit this `.gitignore` file to your repository.

## How to Run

Ensure all prerequisites are met and the `.env` file is correctly set up.

To run the main script:

```bash
python main.py
