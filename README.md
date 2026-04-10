# Student Result Management System

A robust, premium-designed Django application for managing and viewing student academic results. Features a modern glassmorphic UI, automated grade calculations, and PDF report generation.

## 🚀 Features

- **Premium UI**: Modern dark theme with glassmorphism effects and responsive design.
- **Admin Dashboard**: Manage students, subjects, classes, and declare results with ease.
- **Student Portal**: Dedicated search interface for students to view their performance.
- **Automated Grading**: Logic-driven grade and percentage calculation based on marks.
- **PDF Export**: Generate professional, print-ready grade reports in one click.
- **Secure Auth**: Role-based access control for administrative actions.

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Django 5.x
- **Frontend**: Vanilla CSS (Premium Custom Styles), HTML5, JavaScript
- **Database**: SQLite (Default) / MySQL Compatible
- **PDF Generation**: xhtml2pdf
- **Styling**: Google Fonts (Outfit), FontAwesome, Bootstrap 5 (Utilities)

## 📋 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Xcode83/Student_Result_Management_System.git
cd Student_Result_Management_System
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Admin Account
```bash
python manage.py createsuperuser
```

### 5. Run the Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` to view the application.

## 🔑 Default Admin Credentials
- **Username**: `admin`
- **Password**: `admin123`

## 📖 Usage

1. **Login** as an admin at `/accounts/login/`.
2. **Add a Class**: Define class names and sections.
3. **Add a Subject**: Register subjects with codes.
4. **Add a Student**: Enroll students in the created classes.
5. **Declare Result**: Link a student to a subject and enter marks.
6. **Search**: Use the roll number on the landing page to view/download the report.

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---
Built with ❤️ by [Xcode83](https://github.com/Xcode83)
