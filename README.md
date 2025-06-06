# ⏰ Remind-Me-Later API

A simple yet powerful Django REST API that allows users to create reminders with specific dates, times, messages, and notification methods like **Email** or **SMS** (expandable in the future).

---

## 📝 Overview

**Remind-Me-Later** is designed to be the backend for a reminder management system. It enables frontend apps or users to:

- Create reminders
- Set notification preferences (SMS/Email)
- Store and retrieve scheduled reminder messages

---

## 🚀 Features

- ✅ RESTful API endpoints
- ✅ JSON-based request/response
- ✅ Input validation
- ✅ Modular and future-ready architecture
- ✅ Easy frontend integration
- 🚫 No authentication (can be added)

---

## 🛠️ Tech Stack

- **Backend**: Django REST Framework
- **Database**: SQLite (dev) / PostgreSQL (production-ready)
- **Documentation**: Auto-generated OpenAPI schema
- **Language**: Python 3.8+

---

## 🔧 Installation

### Prerequisites

- Python 3.8 or above
- `pip` package manager

### Setup Steps

```bash
# 1. Clone the repository
git clone https://github.com/sonali-more5117/Remind-Me-Later-.git
cd remind-me-later

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install fastapi uvicorn
uvicorn main:app --reload

# 4. Run migrations
python manage.py migrate

# 5. Start development server
python manage.py runserver

# 6. Output
![image](https://github.com/user-attachments/assets/baa848ed-fab8-4633-aef0-c0940ade9ef1)
![image](https://github.com/user-attachments/assets/46a79f0b-8f51-471d-aef9-dd7eef1414c7)



