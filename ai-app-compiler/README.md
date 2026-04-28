# 📁 app/

This is the core application directory of the **AI App Compiler** project. It contains the FastAPI server entry point, the multi-stage compiler pipeline, and shared utility modules.

---

## 📂 Structure

```
app/
│
├── main.py
│
├── pipeline/
│   ├── intent.py
│   ├── design.py
│   ├── schema.py
│   ├── validator.py
│   └── repair.py
│
└── utils/
    ├── llm.py
    └── metrics.py
```

---

## 📄 main.py

The **entry point** of the FastAPI application.

**Responsibilities:**
- Initializes the FastAPI app instance
- Defines API routes (`GET /`, `POST /generate`, `GET /metrics`)
- Orchestrates the full pipeline by calling each stage in sequence
- Returns the final compiled blueprint as a JSON response

---

## 🔩 pipeline/

Contains all the sequential stages of the compiler pipeline. Each file is responsible for one distinct transformation step.

---

### `intent.py` — 🔍 Intent Extraction

**Purpose:** Parses the raw user prompt and extracts structured intent.

**Output includes:**
- App type (e.g., CRM, e-commerce, blog)
- Core features (e.g., login, dashboard, notifications)
- User roles (e.g., admin, user, guest)
- Key entities (e.g., User, Product, Order)

---

### `design.py` — 🏗️ System Design

**Purpose:** Takes the extracted intent and generates a high-level system design.

**Output includes:**
- Application modules
- User flows
- Architecture overview
- Component relationships

---

### `schema.py` — 🗂️ Schema Generation

**Purpose:** Converts the system design into concrete schemas.

**Output includes:**
- **UI Schema** — Pages, components, and layout
- **API Schema** — Endpoints, methods, and payloads
- **Database Schema** — Tables, fields, and relations
- **Auth Rules** — Role-based access control definitions

---

### `validator.py` — ✅ Validation Layer

**Purpose:** Validates the generated schema to ensure structural correctness.

**Checks:**
- All required top-level keys are present
- No empty or null critical fields
- Schema conforms to expected format

**Returns:** `valid: true` or `valid: false` with error details

---

### `repair.py` — 🔧 Auto Repair

**Purpose:** Automatically fixes schemas that fail validation.

**Behavior:**
- Triggered only when `validator.py` returns `valid: false`
- Fills in missing keys with safe defaults
- Re-runs validation after repair
- Increments `repairs_triggered` in metrics

---

## 🛠️ utils/

Shared utility modules used across the pipeline.

---

### `llm.py` — 🤖 LLM Interface

**Purpose:** Abstracts all interactions with the language model.

**Responsibilities:**
- Sends prompts to the LLM (currently simulated / mock)
- Handles response parsing
- Can be swapped to use OpenAI, Gemini, or any other LLM provider with minimal changes

---

### `metrics.py` — 📊 Metrics Tracker

**Purpose:** Tracks runtime statistics for observability.

**Tracks:**
- `total_requests` — Number of `/generate` calls made
- `valid_outputs` — Schemas that passed validation
- `invalid_outputs` — Schemas that failed validation
- `repairs_triggered` — Number of times the repair stage was invoked

**Exposed via:** `GET /metrics`

---

## 🔄 Pipeline Flow

```
main.py receives POST /generate
        │
        ▼
  intent.py → extracts intent from prompt
        │
        ▼
  design.py → generates system design
        │
        ▼
  schema.py → produces UI, API, DB, Auth schemas
        │
        ▼
  validator.py → checks schema integrity
        │
     ┌──┴──┐
   valid  invalid
     │      │
     │   repair.py → fixes and re-validates
     │      │
     └──────┘
        │
        ▼
  metrics.py → updates counters
        │
        ▼
  Final JSON Response
```

---

## 📌 Notes

- Each pipeline stage is **independently importable** and testable
- The `llm.py` module is designed to be **provider-agnostic** — swap in any LLM with minimal refactoring
- `metrics.py` uses **in-memory tracking** (resets on server restart); can be extended to use Redis or a database for persistence

---

## 👩‍💻 Author

**Doyel Mishra**
