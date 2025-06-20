# 🌍 Country Comparison Report

A lightweight Python Flask web application that allows users to compare two countries based on key statistics like population, GDP, literacy rate, area, and capital city — all fetched from a static CSV file.

> ✅ Fully offline  
> ✅ No JavaScript  
> ✅ Ideal for education, travel, and research use cases

---

## 🚀 Features

- Select two countries from a dropdown form
- Displays a side-by-side comparison of:
  - Population
  - GDP (in USD)
  - Literacy Rate (%)
  - Area (sq km)
  - Capital
- Pure HTML + Python (no JS or database)
- Easy to extend with more countries

---

## 🧰 Technologies Used

| Technology | Purpose                        |
|------------|--------------------------------|
| Python     | Backend and data processing    |
| Flask      | Web framework                  |
| CSV        | Data source (country stats)    |
| HTML/CSS   | Frontend user interface        |

---

## 📁 Project Structure
```
country\_comparison\_report/
├── main.py               # Flask backend
├── countries.csv         # Country data (static file)
├── templates/
│   ├── index.html        # Country selection form
│   └── result.html       # Result display page

```
## 🛠️ How to Run

### 1. Install Flask

```bash
pip install flask
````

### 2. Run the App

```bash
python main.py
```

### 3. Open in Browser

```
http://127.0.0.1:5000
```

---

## 🗃️ CSV Format

```csv
Country,Population,GDP (in USD),Literacy Rate (%),Area (sq km),Capital
India,1400000000,3170000000000,74.4,3287263,New Delhi
United States,331000000,21400000000000,99,9833517,Washington D.C.
...
```

Edit `countries.csv` to add or remove countries as needed.

---

## 📌 Future Improvements

* Highlight larger values (e.g., higher GDP)
* Export results to PDF
* Add charts with Python
* Deploy online (Replit, Render, etc.)

---

## 🙋 Author

Created by **Bhubalan Srinivasan** as a portfolio project to demonstrate Python, Flask, and CSV data processing.

---

## 📜 License

This project is licensed under the MIT License.

```

Let me know if you want this written into a file or zipped with your project.
```
