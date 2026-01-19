# The Guardian of Justice AI
An automated auditing system built with Python to manage emergency traffic priority and driver trust scores.

## 🚀 Key Features
- **Dynamic Trust Scoring:** Automatically deducts points for false emergency claims.
- **Identity Verification:** Tracks drivers using both Name and License Number.
- **Audit Logging:** Every decision is permanently stored in a secure `.txt` database with UTF-8 support.
- **Safety Lockdown:** System automatically triggers a High Alert and shuts down if a driver's score becomes critical.

## 🛠️ Technology Used
- **Language:** Python 3.x
- **Core Concepts:** Loops, Conditional Logic, File Handling, Unicode Encoding.

## 📂 Project Structure
- `main.py`: The core engine of the AI.
- `audit_report.txt`: The persistent database for audit logs.
- `README.md`: Project documentation.