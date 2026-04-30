# 🚀 AI App Compiler

An end-to-end backend system that converts a natural language app idea into a structured application blueprint using a multi-stage pipeline.

---

## 🧠 Overview

AI App Compiler takes a simple prompt like:

> "Build a CRM with login and dashboard"

and transforms it into:

- Structured intent
- System design
- Application schema
- Validation + repair
- Metrics tracking

This project simulates a **compiler-like pipeline for application generation**.

---

## ⚙️ Pipeline Architecture

```bash
User Prompt
↓
Intent Extraction
↓
System Design
↓
Schema Generation
↓
Validation
↓
Repair (if needed)
↓
Final Output
```

---

## 🧩 Features

- 🔍 **Intent Extraction**
  - Identifies features, roles, entities

- 🏗️ **System Design**
  - Generates architecture, modules, user flows

- 🗂️ **Schema Generation**
  - UI schema
  - API schema
  - Database schema
  - Auth rules

- ✅ **Validation Layer**
  - Ensures required keys exist

- 🔧 **Auto Repair System**
  - Fixes incomplete or broken schemas

- 📊 **Metrics Tracking**
  - Total requests
  - Valid outputs
  - Invalid outputs
  - Repairs triggered

- 🌐 **FastAPI Backend**
  - Interactive Swagger UI (`/docs`)

---

## 🛠️ Tech Stack

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn

---

## 📂 Project Structure

```
ai-app-compiler/
│
├── app/
│   ├── main.py
│   │
│   ├── pipeline/
│   │   ├── intent.py
│   │   ├── design.py
│   │   ├── schema.py
│   │   ├── validator.py
│   │   └── repair.py
│   │
│   └── utils/
│       ├── llm.py
│       └── metrics.py
```

---

## 🚀 How to Run

### 1️⃣ Clone repo

```bash
git clone https://github.com/DoyelMishra15/ai-app-compiler.git
cd ai-app-compiler
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install fastapi uvicorn pydantic
```

### 4️⃣ Run server

```bash
uvicorn app.main:app --reload --port 8000
```

---

## 🌐 API Endpoints

### 🏠 Home
`GET /`

---

### ⚡ Generate App Blueprint
`POST /generate`

**Request:**
```json
{
  "prompt": "Build a CRM with login and dashboard"
}
```

**Response:**
```json
{
  "intent": {},
  "design": {},
  "schema": {},
  "valid": true
}
```

---

### 📊 Metrics
`GET /metrics`

**Example:**
```json
{
  "total_requests": 3,
  "valid_outputs": 3,
  "invalid_outputs": 0,
  "repairs_triggered": 0
}
```

---

## 🧠 Key Concept

This project mimics a compiler pipeline:

- **Input** → Natural Language
- **Output** → Structured System Design

It demonstrates:

- System thinking
- Modular architecture
- Validation & fault tolerance
- Observability via metrics

---

## 🔮 Future Improvements

- Integrate real LLM (OpenAI / Gemini)
- Generate actual frontend/backend code
- Add database integration
- Deploy on cloud (AWS / GCP)

---

## 👩‍💻 Author

**Doyel Mishra**

---

## ⭐ Why This Project Matters

This is not just an API — it demonstrates:

- Pipeline architecture
- Structured transformations
- Backend system design
- Real-world engineering thinking
