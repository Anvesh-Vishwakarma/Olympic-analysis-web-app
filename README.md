# 🏅 Olympic Data Analysis Dashboard

An interactive **Streamlit-based data analytics dashboard** that provides deep insights into **Olympic Games history**, including medal tallies, country-wise performance, athlete statistics, and participation trends across years.

This project uses **Python, Pandas, Streamlit, Plotly, Seaborn, and Matplotlib** to transform raw Olympic data into meaningful visual analytics.

---

## 📌 Dataset Information
* athlete_events.csv
  * Contains athlete-level Olympic data from 1896 to 2016

* noc_regions.csv
  * Maps National Olympic Committees (NOC) to regions/countries

## 📊 Features

- 🥇 **Medal Tally Analysis**
  - Overall medal tally
  - Year-wise medal distribution
  - Country-wise medal performance

- 🌍 **Overall Olympic Analysis**
  - Total editions, cities, sports, events, athletes, and countries
  - Participating nations over time
  - Events conducted across Olympic years
  - Sport-wise event heatmap
  - Top athletes across sports

- 🏳️ **Country-wise Analysis**
  - Medal trends over years
  - Best performing sports
  - Top athletes from selected country

- 🧑‍🤝‍🧑 **Athlete-wise Analysis**
  - Age distribution of medal winners
  - Gender participation trends over time

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Framework:** Streamlit  
- **Data Processing:** Pandas, NumPy  
- **Visualization:** Plotly, Matplotlib, Seaborn  
- **Scientific Computing:** SciPy  

---

## 📁 Project Structure

```
├── app.py                 # Main Streamlit application
├── helper.py              # Data aggregation & analytics functions
├── preprocessor.py        # Data cleaning & preprocessing
├── athlete_events.csv     # Olympic athletes dataset
├── noc_regions.csv        # Country-region mapping
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## How to run 
### 1. CLone the Repository
```
```

### 2️. Create a Virtual Environment (Recommended)
```
python -m venv venv
```
Activate Virtual Enviornment
```
venv/Scripts/activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4️. Run the Streamlit App
```
streamlit run app.py
```

