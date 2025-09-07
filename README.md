# Django Simple Blog

A simple blog application built with **Django** and **Django Templates**.  
It allows users to read posts, add comments, and save posts for later using sessions.

---

## 🚀 Features
- **Homepage**: shows the latest 3 posts.
- **All Posts Page**: lists all posts ordered by newest first.
- **Single Post Page**:
  - View full blog post by slug.
  - Displays tags.
  - Shows comments (newest first).
  - Add a new comment via form.
  - Save/unsave a post for later.
- **Read Later Page**:
  - Uses Django sessions to store posts for later reading.
  - Displays saved posts or a message if empty.

---

## 🛠 Tech Stack
- **Backend**: Django (Python)
- **Database**: SQLite (default)
- **Frontend**: Django Templates (HTML, CSS)
- **Other**: Django Forms, Sessions

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/django-simple-blog.git
   cd django-simple-blog
# Django Simple Blog

A simple blog application built with **Django** and **Django Templates**.  
It allows users to read posts, add comments, and save posts for later using sessions.

---

## 🚀 Features
- **Homepage**: shows the latest 3 posts.
- **All Posts Page**: lists all posts ordered by newest first.
- **Single Post Page**:
  - View full blog post by slug.
  - Displays tags.
  - Shows comments (newest first).
  - Add a new comment via form.
  - Save/unsave a post for later.
- **Read Later Page**:
  - Uses Django sessions to store posts for later reading.
  - Displays saved posts or a message if empty.

---

## 🛠 Tech Stack
- **Backend**: Django (Python)
- **Database**: SQLite (default)
- **Frontend**: Django Templates (HTML, CSS)
- **Other**: Django Forms, Sessions

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/django-simple-blog.git
   cd django-simple-blog
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Linux/Mac
   source venv/bin/activate
3. **Install dependencies**
   ```bash
    pip install -r requirements.txt
4. **Apply migrations**
   ```bash
   python manage.py migrate
5. **Run the development server**
   ```bash
   python manage.py runserver
6. **Open your browser and go to:***
   ```bash
   http://127.0.0.1:8000/
## 📸 Screenshots
Here are some screenshots of the app:

**Homepage**
<img width="1830" height="893" alt="1" src="https://github.com/user-attachments/assets/d4b06973-01a8-4c6c-88b8-a040fd0f9d60" />

**All Posts**
<img width="1829" height="896" alt="2" src="https://github.com/user-attachments/assets/d35c342a-fc7e-4725-af96-ba92cef7bace" />

**Single Post**
<img width="1828" height="889" alt="3" src="https://github.com/user-attachments/assets/dfe92708-dfbc-4ee3-a5f4-cd34ddf3091c" />

**Added to read Later**
<img width="1828" height="895" alt="4" src="https://github.com/user-attachments/assets/8e784934-39b1-44f5-ac9f-bc27c0ca811d" />

**Read later list**
<img width="1846" height="887" alt="5" src="https://github.com/user-attachments/assets/d13d5ab3-603a-4d02-80f0-acd44c5e7cad" />

**Comment Section**
<img width="1645" height="883" alt="6" src="https://github.com/user-attachments/assets/d6f058bb-2024-407b-bc38-663b36106261" />

**Admin Panel**
<img width="1851" height="891" alt="7" src="https://github.com/user-attachments/assets/ac437568-2733-4d22-a908-77c32de85253" />
<img width="1842" height="896" alt="8" src="https://github.com/user-attachments/assets/e1b36840-e533-4dec-abb8-3f09ea663431" />
<img width="1845" height="890" alt="9" src="https://github.com/user-attachments/assets/72835558-e141-4715-9055-fa5884972835" />

## 📂 Project Structure
```
my_site/
│
├── blog/
│   ├── migrations/
│   ├── templates/blog/
│   │   ├── index.html
│   │   ├── all-posts.html
│   │   ├── post-detail.html
│   │   └── stored-posts.html
│   ├── static/blog/
│   │   ├── images
│   │       ├── logo.png
│   │   ├── index.css
│   │   ├── all-posts.css
│   │   ├── post-detail.css
│   │   └── stored-posts.css
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── my_site/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
│   └── app.css
│
├── templates/
│   ├── 404.html
│   └── base.html
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```
## 📝 License
This project is open-source and available under the MIT License.
