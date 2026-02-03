# Renewable Energy Consumption Predictor

A machine learning web application that analyzes and predicts renewable energy consumption trends by country using historical data from 1960 to 2023.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Data Schema](#data-schema)
- [How It Works](#how-it-works)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

## Overview

This project provides an interactive web interface to explore historical renewable energy consumption data and generate future predictions using linear regression. Users can select any country from the OECD dataset and visualize both historical trends and predicted future values.

## Dataset

The data used in this project comes from the OECD (Organisation for Economic Co-operation and Development) and is available on Kaggle:

**Source:** [Renewable Energy 1960-2023](https://www.kaggle.com/datasets/imtkaggleteam/renewable-energy-1960-2023)

### Dataset Highlights

- **Records:** ~15,900 rows
- **Time Range:** 1960 - 2023
- **Coverage:** 100+ countries and regions worldwide
- **Measurement Unit:** KTOE (Kilotons of Oil Equivalent)
- **Frequency:** Annual data

## Features

- **Country Selection:** Choose from 100+ countries and regional aggregates (EU28, G20, OECD, etc.)
- **Interactive Predictions:** Specify 1-20 years into the future for predictions
- **Data Visualization:** Altair-powered charts showing historical data and predicted trends
- **Model Transparency:** View model coefficients, training data size, and year ranges
- **Responsive UI:** Clean Streamlit interface with real-time updates

## Project Structure

```
renewable_energy/
├── main.py                      # Streamlit web application entry point
├── requirements.txt             # Python dependencies
├── CLAUDE.md                    # Development guidelines
├── README.md                    # Project documentation
├── ml_model_config/             # Machine learning model module
│   ├── __init__.py
│   └── model.py                 # Linear regression training and prediction
├── ml_model_data_cleanup/       # Data preprocessing module
│   ├── __init__.py
│   └── data_loader.py           # CSV loading and filtering functions
├── raw_data/
│   └── renewable_energy.csv     # OECD renewable energy dataset
└── venv/                        # Python virtual environment
```

## Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd renewable_energy
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Run the Streamlit application:**
   ```bash
   streamlit run main.py
   ```

3. **Open your browser** and navigate to `http://localhost:8501`

4. **Use the application:**
   - Select a country from the dropdown menu
   - Adjust the number of years to predict (1-20)
   - View the interactive chart and prediction table
   - Expand "Model Details" to see regression coefficients

## Technologies

| Technology | Purpose |
|------------|---------|
| **Python 3.9** | Core programming language |
| **Streamlit** | Web application framework |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computations |
| **scikit-learn** | Machine learning (Linear Regression) |
| **Altair** | Interactive data visualization |

## Data Schema

The CSV dataset contains the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `LOCATION` | ISO 3166-1 alpha-3 country code | `USA`, `DEU`, `BRA` |
| `INDICATOR` | Energy type indicator | `RENEWABLE` |
| `SUBJECT` | Category | `TOT` (total) |
| `MEASURE` | Unit of measurement | `KTOE` (kilotons of oil equivalent) |
| `FREQUENCY` | Data frequency | `A` (annual) |
| `TIME` | Year of measurement | `1960` - `2023` |
| `Value` | Energy consumption value | `4436.932` |
| `Flag Codes` | Data quality indicators | (optional) |

### Sample Countries Available

| Code | Country | Code | Country |
|------|---------|------|---------|
| USA | United States | DEU | Germany |
| CHN | China | JPN | Japan |
| BRA | Brazil | IND | India |
| GBR | United Kingdom | FRA | France |
| CAN | Canada | AUS | Australia |

*Plus 90+ additional countries and regional aggregates (EU28, G20, OECD, etc.)*

## How It Works

### 1. Data Loading
The application loads the CSV dataset and extracts unique country codes for the selection dropdown.

### 2. Data Preprocessing
For each selected country, the system:
- Filters records by location and measurement type (KTOE)
- Removes rows with missing values
- Sorts data chronologically

### 3. Model Training
A **Linear Regression** model is trained on the historical data:
- **Features (X):** Year values
- **Target (y):** Energy consumption values (KTOE)

### 4. Prediction
The trained model extrapolates future consumption based on the learned trend:
```
Predicted Value = (coefficient × year) + intercept
```

### 5. Visualization
Results are displayed using an interactive Altair chart that distinguishes between:
- **Historical data:** Actual recorded values
- **Predicted data:** Model-generated forecasts

## Author

**Alejandro Villalobos**
Email: [avillalobosh@ucenfotec.ac.cr](mailto:avillalobosh@ucenfotec.ac.cr)
Institution: Universidad Cenfotec

## Acknowledgments

- **Data Source:** [OECD](https://www.oecd.org/) via [Kaggle](https://www.kaggle.com/datasets/imtkaggleteam/renewable-energy-1960-2023)
- **Dataset Provider:** IMT Kaggle Team
- **Built with:** [Streamlit](https://streamlit.io/), [scikit-learn](https://scikit-learn.org/)
