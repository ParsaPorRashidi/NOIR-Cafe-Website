<div align="center">

  <p align="center">
    <img src="" alt="Bot Banner" width="900">
  </p>
  
  <h1>☕ Cafe Platform / Website</h1>


---

  ### QRcode , Smart Menu , Dedicated Admin Panel , Waiter Call

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.14+-1E120D.svg?style=flat&logo=python&logoColor=white" alt="Python Version"></a>
  <a href="https://www.djangoproject.com/"><img src="https://img.shields.io/badge/Django-6.0+-%232d3a22.svg?style=flat&logo=django&logoColor=white" alt="Django Version"></a>
  <a href="https://www.django-rest-framework.org/"><img src="https://img.shields.io/badge/DRF-3.15+-1E120D.svg?style=flat" alt="DRF Version"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-%232d3a22.svg?style=flat" alt="License"></a>
</p>

<p align="center">
  <a href="#support"><img src="https://img.shields.io/badge/Support-%232d3a22.svg?style=flat" alt="Support"></a>
  <a href="#tests"><img src="https://img.shields.io/badge/Tested-%232d3a22.svg?style=flat" alt="Tested"></a>
</p>
  
  <p>
    <p align="center">
      <a href="#english">English</a> •
      <a href="#persian">فارسی</a>
    </p>

</div>


---

<div id="english">

## 🇬🇧 English Description

A professional, cost-effective, single-page web application (SPA) designed for modern cafes to digitize their services with minimal cost. This platform offers a seamless experience for customers to explore the cafe, browse the digital menu, call a waiter instantly, and discover music, while providing owners with a robust Django administration panel.

### ✨ Features

#### 🧑‍🍳 Customer-Facing Features (Single Page)
* **Cafe Introduction:** Beautiful showcase of the cafe's environment, contact details, and working hours.
* **Digital Menu:** Elegant, responsive menu displaying items, prices, and descriptions.
* **🛎️ Smart Waiter Calling System:** Customers can request a waiter with a single click by selecting their table/seat number. Notifications are sent instantly to the admin panel.
* **🎵 Integrated Music Player:** A dedicated section where customers can see the playlist, search for their favorite tracks, and download them.
* **📅 Event Board:** Keeps customers updated on upcoming cafe events (live music, sports screenings, poetry nights, etc.).

#### 👨‍💻 Dedicated Admin Panel (Django Admin & Custom Dashboard)
* **Real-time Request Tracking:** Monitor and manage active "Call Waiter" requests organized by table numbers.
* **Menu Management:** Easily add, update, or remove menu categories and items.
* **Event Planner:** Create and manage scheduled cafe events.
* **Track & Playlist Control:** Update the available music tracks and site configurations effortlessly.

### 🚀 Tech Stack
* **Backend:** Python, Django Web Framework
* **Frontend:** HTML5, CSS3, JavaScript (Single Page Architecture)
* **Database:** SQLite (Default / Development) or PostgreSQL/MySQL (Production)

### 🛠️ Installation & Setup Guide

Follow these steps to set up and run the project locally on your machine:

#### 1. Prerequisites
Ensure you have the following installed:
* [Python 3.14+](https://www.python.org/)
* [Git](https://git-scm.com/)

#### 2. Clone the Repository
```bash
git clone [https://github.com/YourUsername/YourProjectName.git](https://github.com/YourUsername/YourProjectName.git)

cd YourProjectName
```

3. Create and Activate a Virtual Environment
```Bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```
4. Install Dependencies
```Bash
pip install -r requirements.txt
```
5. Environment Configurations
Create a .env file in the project's root directory (or rename .env.example) and configure your variables:
```Code snippet
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```
6. Database Migrations
Apply the migrations to set up your database schema:

```Bash
python manage.py migrate
```
7. Create a Superuser (Admin)
Create an administrative account to access the backend panel:

```Bash
python manage.py createsuperuser
```
8. Run the Development Server
```Bash
python manage.py runserver
```
Open your browser and navigate to http://127.0.0.1:8000/ to view the website. Access the admin dashboard at http://127.0.0.1:8000/admin/.

<div id="persian">

## 🇮🇷 توضیحات فارسی
یک وب‌اپلیکیشن تک‌صفحه‌ای (SPA) و اقتصادی، طراحی شده برای کافه‌هایی که می‌خواهند با کمترین هزینه، فرآیندهای خود را دیجیتالی کنند و تجربه متفاوتی به مشتریان ارائه دهند. این سیستم شامل بخش معرفی کافه، منوی دیجیتال، سیستم هوشمند فراخوانی گارسون و یک پنل مدیریت قدرتمند بر پایه جنگو است.

### ✨ امکانات و ویژگی‌ها
#### 🧑‍🤝‍🧑 بخش مشتریان (تک‌صفحه‌ای)
* معرفی کافه: نمایش جذاب محیط کافه، اطلاعات تماس و ساعات کاری.

* منوی دیجیتال: دسترسی سریع و واکنش‌گرا به منوی کافه همراه با قیمت‌ها و توضیحات.

* 🛎️ سیستم فراخوانی گارسون: امکان درخواست گارسون تنها با یک کلیک. مشتری میز و صندلی خود را انتخاب کرده و درخواست به‌صورت آنی به پنل مدیریت ارسال می‌شود.

* 🎵 موزیک پلیر اختصاصی: بخشی جذاب برای مشاهده لیست آهنگ‌های کافه، با امکان جستجو و دانلود آهنگ‌ها توسط مشتریان.

* 📅 رویدادها (Events): اطلاع‌رسانی درباره رویدادهای پیش‌روی کافه (مثل پخش مسابقات، موسیقی زنده و...).

#### 👨‍💻 پنل مدیریت اختصاصی 
مدیریت زنده درخواست‌ها: مشاهده و کنترل درخواست‌های «فراخوانی گارسون» به تفکیک شماره میز و صندلی.

مدیریت منو: افزودن، ویرایش یا حذف دسته‌بندی‌ها و آیتم‌های منو.

مدیریت رویدادها: ثبت، ویرایش و حذف ایونت‌های کافه.

مدیریت لیست موزیک‌ها: به‌روزرسانی آسان فایل‌های صوتی و اطلاعات آهنگ‌ها.

#### 🚀 تکنولوژی‌های استفاده شده
بک‌اند: Python, Django Framework

فرانت‌اند: HTML5, CSS3, JavaScript

دیتابیس: SQLite (پیش‌فرض توسعه) / قابلیت اتصال به PostgreSQL و MySQL

#### 🛠️ آموزش نصب و راه‌اندازی (محیط لوکال)
برای اجرای پروژه روی سیستم خود، مراحل زیر را به ترتیب دنبال کنید:

1. پیش‌نیازها
مطمئن شوید که ابزارهای زیر روی سیستم شما نصب هستند:

* [Python 3.14+](https://www.python.org/)
* [Git](https://git-scm.com/)

2. دریافت پروژه (Clone)
```Bash
git clone [https://github.com/YourUsername/YourProjectName.git](https://github.com/YourUsername/YourProjectName.git)
cd YourProjectName
```
3. ساخت و فعال‌سازی محیط مجازی (Virtual Environment)
```Bash
# ویندوز
python -m venv venv
venv\Scripts\activate

# لینوکس / مک
python3 -m venv venv
source venv/bin/activate
```
4. نصب پکیج‌های مورد نیاز
```Bash
pip install -r requirements.txt
```
5. تنظیمات فایل محیطی
یک فایل به نام .env در مسیر اصلی پروژه ایجاد کرده و متغیرهای جنگو را تنظیم کنید:

```Code snippet
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```
6. اعمال Migrationها روی دیتابیس
```Bash
python manage.py migrate
```
7. ساخت حساب کاربری ادمین (Superuser)
```Bash
python manage.py createsuperuser
```
8. اجرای سرور توسعه
```Bash
python manage.py runserver
```
پروژه در آدرس http://127.0.0.1:8000/ آماده استفاده است. برای ورود به پنل مدیریت نیز می‌توانید به مسیر http://127.0.0.1:8000/admin/ مراجعه کنید.

#### 📄 License / لایسنس
This project is licensed under the MIT License - see the LICENSE file for details.

این پروژه تحت لایسنس MIT منتشر شده است و استفاده تجاری یا شخصی از آن کاملاً آزاد است.

