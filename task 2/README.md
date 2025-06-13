# 📄 CodTech Internship – Task 2: Automated Report Generation

## 📝 Objective
To create an automated system that reads data from a public API, processes and analyzes it, and then generates a **formatted PDF report** using Python libraries like **FPDF** and **matplotlib**.

---

## 📊 Description
- Fetched user data from the API: [`https://jsonplaceholder.typicode.com/users`](https://jsonplaceholder.typicode.com/users)
- Simulated the dataset by **expanding it to 30 users** for realistic analysis
- Randomized city distribution to visualize **user count per city**
- Generated a **bar chart** using `matplotlib`
- Created a professional **PDF report** using `FPDF`, which includes:
  - Summary table (Name, Username, Email, City, Company)
  - Embedded chart image
  - Footer with student & internship info

---

## 🛠 Technologies Used
- Python
- `requests`
- `pandas`
- `matplotlib`
- `fpdf`

---

## 📂 Files Included
- `codtech_task2.py` – Main script
- `bar_chart.png` – Generated chart for PDF
- `User_Report.pdf` – Final PDF report
- `README.md` – Documentation

---

## ▶️ How to Run

1. **Install dependencies:**
   ```bash
   pip install requests pandas matplotlib fpdf