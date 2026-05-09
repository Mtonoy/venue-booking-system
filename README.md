# Venue Booking System

A simple and modern Venue Booking System built using:

- HTML
- CSS
- JavaScript
- Python Flask
- SQLite

This web application allows users to:

- Submit venue booking requests
- View booking dashboard
- Approve or reject requests
- Detect booking conflicts
- View analytics reports with charts

---

# Features

## Venue Booking Form
Users can:

- Enter event details
- Select venue
- Choose start and end date/time
- Add organizer information
- Add special requirements

---

## Dashboard
Dashboard displays:

- All booking requests
- Booking status
- Conflict information
- Open request details

---

## Approval / Reject System
Admin can:

- Approve requests
- Reject requests
- View booking details
- See conflict warnings

---

## Conflict Detection
The system automatically detects conflicts when:

- Same venue
- Overlapping date/time

Conflict message is displayed in approval page.

---

## Analytics Dashboard
Analytics page includes:

- Total bookings
- Approved bookings
- Rejected bookings
- Pending bookings
- Charts using Chart.js

---

# Technologies Used

## Frontend
- HTML5
- CSS3
- JavaScript

## Backend
- Python Flask

## Database
- SQLite

## Charts
- Chart.js

---

# Project Structure

```text
venue-booking-system/
│
├── app.py
├── create_db.py
├── database.db
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── approval.html
│   └── analytics.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── app.js

# Installation Guide

Follow these steps to run the Venue Booking System on your computer.

---

## Step 1 — Install Python

Download Python from:

https://www.python.org/downloads/

IMPORTANT:

During installation, enable:

```text
Add Python to PATH
```

Then click:

```text
Install Now
```

---

## Step 2 — Download or Clone Project

### Option 1 — Clone Using Git

```bash
git clone https://github.com/your-username/venue-booking-system.git
```

### Option 2 — Download ZIP

- Download project ZIP
- Extract the folder

---

## Step 3 — Open Project in VS Code

Open Visual Studio Code.

Click:

```text
File → Open Folder
```

Select:

```text
venue-booking-system
```

---

## Step 4 — Install Flask

Open terminal inside VS Code.

Run:

```bash
pip install flask
```

OR install using requirements file:

```bash
pip install -r requirements.txt
```

---

## Step 5 — Create Database

Run:

```bash
python create_db.py
```

This automatically creates:

```text
database.db
```

---

## Step 6 — Run Application

Start Flask server:

```bash
python app.py
```

You should see:

```text
* Running on http://127.0.0.1:5000
```

---

## Step 7 — Open in Browser

Open:

```text
http://127.0.0.1:5000
```

Your Venue Booking System is now running successfully.