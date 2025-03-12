# **SOMO Library Management System (LMS)**

## **📌 Project Overview**
SOMO Library Management System (LMS) is a **scalable, efficient, and user-friendly** web application designed to streamline **library operations**. It enables **admins, librarians, and members** to manage books, track borrowing history, process reservations, handle overdue notifications, and generate reports.

## **🚀 Features**
- **User Roles & Authentication**: Admin, Librarian, and Member access control with approval-based membership.
- **Book Catalog Management**: Add, edit, remove, and search books with genres and availability tracking.
- **Borrowing & Returns**: Members can borrow and return books with automated due date tracking.
- **Reservations & Waitlists**: Members can reserve unavailable books and get notified upon availability.
- **Overdue Notifications & Fines**: Automated alerts and penalty tracking for late returns.
- **Reporting & Analytics**: Track book circulation, overdue statistics, and user activity.

## **🛠️ Tech Stack**
### **Backend:**
- **Django (MVT Architecture)**
- **PostgreSQL** (Database)
- **Celery + Redis** (Task Queue for notifications)
- **Django Authentication** (Built-in authentication system)

### **Frontend:**
- **Django Templates** (MVT-based UI rendering)
- **Bootstrap CSS** (Responsive design)
- **Javascript** (For interactivity without APIs)

### **Deployment & DevOps:**
- **AWS/GCP** (Cloud hosting)
- **Nginx** (Reverse proxy)
- **GitHub Actions** (CI/CD pipeline)

## **📂 Project Structure**
```
SOMO_LMS/
│── apps/
│   │── core/             # Core app (models, views, templates)
│   │── events/           # Events app (models, views, templates)
│   │── librarians/       # Librarians app (models, views, templates)
│   │── members/          # Members app (models, views, templates)
│   │── reservations/     # Book reservation app (models, views, templates)
│   │── notifications     # Notifications app (models, views, templates)
|   │── books/            # Books app (models, views, templates)
|   │── users/            # User authentication & management
|   │── transactions/     # Borrowing & reservations
│   │── utils # utility functions
│── somo_lms/         # Django Project Root
│   ├── settings   # Configuration
|       |── base.py
|       |── dev.py
|       |── prod.py
│   ├── urls.py      # URL Routing
│   ├── wsgi.py      # WSGI Application
│── static/          # CSS, JavaScript, Images
│── manage.py        # Django CLI tool
│── README.md        # Readme file
│── .gitignore       # gitignore file
│── LICENSE          # Application license
│── .env             # Application environment variables
```

## **⚙️ Installation & Setup**
### **1. Clone the Repository**
```bash
$ git clone https://github.com/yourusername/somo-lms.git
$ cd somo-lms
```
### **2. Setup Virtual Environment & Install Dependencies**
```bash
$ python3 -m venv venv
$ source venv/bin/activate  # On Windows use `venv\Scripts\activate`
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

## **🛡️ Security & Best Practices**
- Use **environment variables** (`.env`) for sensitive data.
- Implement **role-based access control (RBAC)**.
- Enable **HTTPS & secure authentication**.

## **📌 Future Enhancements**
- Mobile app integration.
- AI-powered book recommendations.
- Multi-library branch support.

## **📧 Contact & Contributions**
- **Maintainer**: [Lynn Chelangat]
- **Email**: ["lynnkelly005@gmail.com"]
- **Contributions**: Feel free to fork and submit pull requests!
