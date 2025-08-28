# Notelet 📝

> ⚠️ **Notice**: This repository powers the live app at [notelet.vercel.app](https://notelet.vercel.app).  
> Changes here may directly impact the deployed version.

---

## 📖 About

**Notelet** is a full-stack note-taking application designed to create, update, and manage notes with **rich text content**.  
It is lightweight yet powerful, built to demonstrate clean CRUD operations and secure user authentication.

---

## ✨ Features

- 🔑 **Authentication with OTP** (register & login using email verification)  
- 📝 **Rich Text Notes** (store formatted content as HTML)  
- 📂 **CRUD Operations**  
  - Create new notes  
  - Read individual notes by ID  
  - Update existing notes  
  - Delete notes securely  
- 📜 **List API** for fetching all notes of a logged-in user (newest first)  
- 🔒 **Token-based Authentication** to secure note operations  
- 📨 **Email Utility** for sending verification codes or notifications (requires SMTP credentials in `.env`)  

---

## 🚀 Tech Stack

- **Backend**: Django + Django REST Framework (DRF)  
- **Frontend**: Deployed on [Vercel](https://vercel.app)  
- **Database**: PostgreSQL / SQLite (configurable)  
- **Auth**: Django’s Token Authentication  

---

## 📌 Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/notelet.git
    cd notelet
    ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv env
   source env/bin/activate   # (Linux/Mac)
   env\Scripts\activate      # (Windows)

   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add required variables:

   ```env
    SECRET_KEY = <some secret value>
    DEBUG = <True/False>

    ALLOWED_ORIGINS = <CORS allow origin>

    DATABASE_CONNECTION_STRING = <sql connecting string>

    OTP_LENGTH = 6

    EMAIL_HOST = <smtp host>
    EMAIL_PORT = 587
    EMAIL_HOST_USER = <sender email>
    EMAIL_HOST_PASSWORD = <sender email password>

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the server:

   ```bash
   python manage.py runserver
   ```

---

## 🛠 API Overview

| Endpoint         | Method | Auth Required | Description                     |
| ---------------- | ------ | ------------- | ------------------------------- |
| `/auth/register` | POST   | ❌             | Register with email + OTP       |
| `/auth/login`    | POST   | ❌             | Login with email + password     |
| `/notes/create`  | POST   | ✅             | Create a new note               |
| `/notes/read`    | POST   | ❌             | Fetch a note by ID              |
| `/notes/update`  | POST   | ✅             | Update an existing note         |
| `/notes/delete`  | POST   | ✅             | Delete a note                   |
| `/notes/list`    | GET    | ✅             | Fetch all notes of current user |

---

## 📝 Notes

* The **`content` field** stores notes in **HTML (rich text)** format.
* The backend enforces that each user can only access their own notes.
* This repository is a **backend + API reference** for the live app hosted on Vercel.

---

## 📩 Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

---

## 📜 License

[MIT](LICENSE) © 2025 Notelet