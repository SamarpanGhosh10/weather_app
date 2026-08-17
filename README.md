#  Weather App

A simple weather application built with Python that uses the OpenWeather API to fetch and display real-time weather information for a city.

##  Features

* Search weather by city name
* Displays current temperature
* Displays feels-like temperature
* Displays humidity
* Displays weather condition
* Displays wind speed
* Handles invalid city/API responses
* Keeps the API key secure using environment variables

##  Technologies Used

* Python
* Requests
* OpenWeather API
* python-dotenv
* Git & GitHub


## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/weather_app.git
cd weather_app
```

### 2. Install dependencies

```bash
pip install requests python-dotenv
```

### 3. Create a `.env` file

Create a file named `.env` in the project folder:

```text
API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your OpenWeather API key.

### 4. Run the application

```bash
python weather_app.py
```

## 💻 Example

```text
Enter city: Kolkata

Weather in Kolkata
Temperature: 26.97 °C
Feels like: 26.04 °C
Humidity: 19 %
Condition: overcast clouds
Wind speed: 4.63 m/s
```

## 🔐 API Key Security

The API key is stored in a `.env` file instead of being directly written in the Python source code.

The `.env` file is included in `.gitignore` so that the API key is not uploaded to GitHub.

## 📚 What I Learned

This project helped me learn:

* How APIs work
* Sending HTTP requests using Python
* Working with JSON data
* Extracting data from nested dictionaries
* Handling API errors
* Using environment variables
* Protecting API keys
* Using Git and GitHub

## 🔮 Future Improvements

* Add a graphical user interface
* Add weather icons
* Add 5-day weather forecast
* Add sunrise and sunset information
* Improve error handling
* Add loading indicators
* Improve the overall UI/UX


Built as a Python learning project to practice working with APIs and GitHub.
