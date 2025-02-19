# Unbound Hackathon

## 🚀 Project Overview
This project provides an AI proxy service that allows users to interact with various AI models via a chat interface. The backend is built with **Django**, the frontend with **React (npm)**, and the database uses **SQLite3**.

### Backend Repo :
``` 
https://github.com/Hariish-A/Unbound_chatapp_backend 
```
### Frontend Repo : 
```
https://github.com/Hariish-A/Unbound-Coding-Challenge
```
## 📌 Features & Milestones
### ✅ Milestone 1: Models Endpoint
- **Endpoint:** `GET /models`
- **Behavior:** Fetches and returns a list of supported AI models from the database.

![image](https://github.com/user-attachments/assets/b5d8beaa-3593-4f2d-bff8-bbcb122463fe)


### ✅ Milestone 2: Chat Completions Endpoint
- **Endpoint:** `POST /v1/chat/completions`
- **Validates** provider & model from DB.
- **Routes requests** to a stub LLM returning predefined responses.

  ![image](https://github.com/user-attachments/assets/8ceb5907-017c-4afa-a74a-cfb07068ce6e)
  ![image](https://github.com/user-attachments/assets/09a5b364-9309-428b-b4fc-5a8917824d57)



### ✅ Milestone 3: Prompt Interference & Regex-Based Routing
- Stores regex rules in **SQLite3** to define routing policies.
- If a prompt matches a regex rule, it is redirected to the configured model.

  ![image](https://github.com/user-attachments/assets/60b80fd9-60e4-40fa-bbb7-7055e0325013)


  

### ✅ Milestone 4: Simple Chat UI
- Built with **React**.
- Lists available models.
- Allows provider & model selection.
- Sends prompts & displays responses.

  ![image](https://github.com/user-attachments/assets/d69f4a25-b6ad-40a3-ab08-76bdd8acf93d)


### ✅ Milestone 5: Admin Portal for Regex Policies
- Separate admin interface built with **Django Admin**.
- **CRUD operations** for regex rules.

  ![image](https://github.com/user-attachments/assets/4876c025-5a41-4c7a-927b-07564ff8034f)


### ✅ Milestone 6: File Upload Support in Chat Portal
- Implemented using **React Toastify** for notifications.
- Backend handles file processing & returns confirmation.
  
  ![image](https://github.com/user-attachments/assets/974f1799-ac9f-48c2-acc1-ead038f590c6)


### ✅ Milestone 7: Special Routing for File Uploads
- Admin can configure **file-based routing** via **Django Admin**.
  
![image](https://github.com/user-attachments/assets/534b6576-68be-4660-8a02-5137552db00e)


## 🔧 Setup Instructions
### Prerequisites
- **Node.js & npm** (for frontend)
- **Python & Django** (for backend)
- **SQLite3** (for database)

### Installation
#### 1️⃣ Clone Repository
```bash
 git clone https://github.com/your-repo/chat-ai-proxy.git
 cd chat-ai-proxy
```
#### 2️⃣ Backend Setup (Django)
```bash
 cd backend
 python -m venv venv
 source venv/bin/activate  # MacOS/Linux
 venv\Scripts\activate  # Windows
 pip install -r requirements.txt
 python manage.py migrate
 python manage.py runserver
```
#### 3️⃣ Frontend Setup (React)
```bash
 cd frontend
 npm install
 npm start
```

## 🎨 Design & Architecture
### Stack
- **Backend:** Django (Django Rest Framework)
- **Frontend:** React (npm)
- **Database:** SQLite3

### Folder Structure
#### Frontend
```
/unbound-chat-ui
├── public/
├── src/
│   ├── components/
│   ├── context/
│   ├── hooks/
│   ├── pages/
│   ├── services/
│   ├── styles/
└── tsconfig.json
```

#### Backend
```
/chatapp_backend
├── apis/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
├── chatapp_backend/
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
└── manage.py
```

## 📌 API Endpoints
### ✅ Fetch Models
- `GET /models`
- Returns available models from DB.

### ✅ Chat Completion
- `POST /v1/chat/completions`
- Validates & routes request.

### ✅ Regex-Based Routing Management
- `POST /admin/regex-rules`
- CRUD operations for routing policies.

### ✅ File Upload
- `POST /upload`
- Routes file processing request.

### ✅ API Documentation
- Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)


---
🚀 **Developed by Hariish**

