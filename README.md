# Data Redundancy Removal & Leak Prevention System 

A Lightweight, robust backend and web-based system designed to maintain database integrity and efficiency. This project was developed as part of the **CodeAlpha Intership** (Task 1).

## Features 
- **Data Redundancy Prevention:**Uses SHA-256 cryptographic hashing to fingerprint incoming data and block duplicate records before they hit the database.
- **False Positive Filtering:** A validation layer that catches and discards invalid data inputs (e.g., empty inputs, generic placeholder test terms, or text that is too short).
- **Interactive Web UI:** Built with Streamlit to provide an intuitive, modern user interface for real-time testing.
- **Modular Clean Architecture:** Separated cleanly into independent modules for database handling (`database.py`), data validation (`filters.py`), and the user interface (`app.py`).

## 🛠️ Tech Stack
- **Language:** Python 3.13
- **Database:** SQLite3
- **Frontend Framework:** Streamlit
- **Libraries Used:** `hashlib`, `sqlite3`

## 📦 Project Structure
```text
Internship_Task1/
│
├── app.py          # Streamlit Web User Interface
├── database.py     # SQLite DB connections and SQL executions
├── filters.py      # Business logic (SHA-256 Hashing & Data Validation)
└── storage.db      # Local SQLite database file (auto-generated)
