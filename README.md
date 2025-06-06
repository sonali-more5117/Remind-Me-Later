Remind-Me-Later API
📝 Overview
A simple yet powerful reminder management API that allows users to:

Create reminders with specific dates/times

Set notification preferences (SMS/Email)

Store reminder messages securely

🚀 Features
RESTful API endpoints

JSON payload support

Data validation

Future-proof architecture for additional notification methods

Easy integration with frontend applications

🛠️ Technology Stack
Backend: Django REST Framework

Database: SQLite (default) / PostgreSQL (production-ready)

Authentication: None (can be added)

API Documentation: Automatic OpenAPI schema

🔧 Installation
Prerequisites
Python 3.8+

pip package manager

Setup
bash
# Clone the repository
git clone https://github.com/yourusername/remind-me-later.git
cd remind-me-later

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
🌐 API Endpoints
Base URL
http://localhost:8000/api/

Available Endpoints
Endpoint	Method	Description
/reminders/	POST	Create new reminder
/reminders/{id}/	GET	Retrieve specific reminder
/reminders/	GET	List all reminders (optional)
📨 Request/Response Examples
Create Reminder (POST /api/reminders/)
Request:

json
{
  "date": "2023-12-25",
  "time": "15:30:00",
  "message": "Christmas Party",
  "notification_method": "EMAIL"
}
Success Response (201 Created):

json
{
  "id": 1,
  "date": "2023-12-25",
  "time": "15:30:00",
  "message": "Christmas Party",
  "notification_method": "EMAIL"
}
🗃️ Database Schema
python
class Reminder(models.Model):
    NOTIFICATION_METHODS = [
        ('SMS', 'SMS'),
        ('EMAIL', 'Email'),
    ]
    
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    notification_method = models.CharField(max_length=5, choices=NOTIFICATION_METHODS)
    created_at = models.DateTimeField(auto_now_add=True)
