# 🎉 Creative Studio - Event Management Platform

A full-featured event management web application built with Django. Users can browse event packages, book services, and manage their bookings. Admins have complete control over users, services, and bookings with a custom admin panel.

## 🚀 Live Demo

[Coming Soon](#)

## ✨ Features

### 👥 User Features
- User registration & login (secure password hashing)
- Browse event packages with pricing
- Book packages with event date & guest count
- View all bookings in "My Bookings" dashboard
- Cancel pending bookings
- Toast notifications for success/error messages

### 👑 Admin Features (Custom Admin Panel)
- **Admin Dashboard** - Live stats (users, bookings, revenue)
- **User Management** - Add, edit, delete users
- **Service Management** - Add, edit, delete event packages
- **Booking Management** - View all bookings, update status (pending/confirmed/cancelled/completed)
- **Export Reports** - Download bookings as CSV

### 🎨 Design
- Modern purple/orange gradient theme
- Responsive design (mobile-friendly)
- Glassmorphism effects
- Smooth animations & hover effects

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Backend | Django (Python) |
| Database | SQLite3 |
| Frontend | HTML, CSS, JavaScript |
| Authentication | Session-based |
| Deployment | Ready for PythonAnywhere/Render |

## 📦 Packages & Pricing

| Package | Price | Description |
|---------|-------|-------------|
| Basic Event Package | $499 | Venue booking + vendor coordination + basic setup |
| Premium Event Package | $1299 | Full planning + decor + catering + on-site coordination |
| Wedding Planning Bundle | $2499 | Complete wedding planning (ceremony + reception + rehearsal) |
| Corporate Event Package | $1899 | Conference/seminar planning + AV setup + speaker coordination |
| Birthday Party Package | $799 | Theme design + decor + cake + entertainment + photography |
| Virtual Event Setup | $349 | Zoom/streaming setup + registration page + attendee management |

## 📁 Project Structure

EventManagementSite/
├── myapp/ # Main app (user facing)
│ ├── models.py # User, Product, Booking models
│ ├── views.py # User views (login, register, booking)
│ └── urls.py # User URLs
├── myadmin/ # Admin app
│ ├── views.py # Admin views (dashboard, CRUD)
│ └── urls.py # Admin URLs
├── proj1/ # Project settings
├── templates/ # HTML templates
├── static/ # CSS, images, JS
└── db.sqlite3 # Database


## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Step 1: Clone the Repository
```bash
git clone https://github.com/martinsajan/EventManagementSite.git
cd EventManagementSite

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install django

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

  Access the Website

User Site: http://127.0.0.1:8000/home/

Admin Login: http://127.0.0.1:8000/myadmin/

Admin Credentials: Email: admin@example.com | Password: admin123

  🔧 Future Enhancements
Payment gateway integration (Stripe/Razorpay)

Email notifications (booking confirmation)

Event calendar view

User reviews & ratings

WhatsApp integration

Deploy to production

  👨‍💻 Author
Martin Sajan

GitHub: @martinsajan

  🙏 Acknowledgments
Django documentation

Tooplate for design inspiration

  📄 License
This project is open source and available under the MIT License.

⭐ Star this repository if you found it helpful!