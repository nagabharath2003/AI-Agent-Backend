# AI Agent Backend — FastAPI POC

**Short summary:**  
A small Proof-of-Concept backend that implements the "brain" of an AI agent. It receives a natural-language prompt at a single endpoint and routes it to one of two tools:

- **Memory Tool** — stores and retrieves key/value pairs (database CRUD)
- **Calculator Tool** — evaluates simple math expressions

This repo demonstrates:
- FastAPI for the API
- A DB-backed Memory store (MySQL / SQLite)
- Rule-based intent detection & parsing (simple agent router)
- Pydantic request validation
- Tests (manual via Swagger / Postman, automated via pytest)

---


## Project layout

ai_agent/
├── main.py # FastAPI entry point (agent router)
├── database.py # DB connection + create_table() logic (context manager)
│── memory.py # tool_save_memory, tool_get_memory
│── calculator.py # tool_calculate
├── models.py # Pydantic models
├── utils.py # prompt parsing helpers
├── create_table.sql # SQL to create memory table (optional)
├── test_main.py # pytest tests (optional)
├── requirements.txt
└── README.md

## 🧩 Features Implemented

### 🧮 Calculator Tool
- Evaluates mathematical expressions safely.  
- Example: `"calculate 5 + 10"` → **Result: 15**

### 💾 Memory Tool
- Stores and retrieves information in the database.
- Example:
  - `"remember my city is Khammam"` → saves the value.
  - `"what is my city"` → fetches and returns "Khammam".

### 🧠 Agent Brain (Router)
- Analyzes the input text (prompt) and decides which tool to use:
  - `"calculate"` or `"what is"` → **Calculator**
  - `"remember"` or `"save"` → **Save to Memory**
  - `"what is my"` or `"recall"` → **Read from Memory**

---

## 🧰 Tech Stack

| Component | Technology Used |
|------------|----------------|
| **Language** | Python 3.10+ |
| **Framework** | FastAPI |
| **Database** | MySQL (or SQLite) |
| **Validation** | Pydantic |
| **Testing** | Swagger UI / Postman / Pytest |
| **ORM Style** | Raw SQL (lightweight CRUD) |


