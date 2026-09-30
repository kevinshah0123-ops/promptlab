# PromptLab

Test and refine AI prompts locally with simulated model responses

PromptLab is a local AI prompt testing workbench that lets engineers experiment with different prompt templates and compare outputs side-by-side using mock LLM responses. Users create prompt templates with variables, generate test cases with sample data, and view simulated AI completions in a clean web interface. The tool helps AI engineers iterate on prompt design without burning API credits, using a rule-based mock engine that simulates realistic language model behavior based on prompt characteristics.

## Features

- Create and save prompt templates with variable placeholders (e.g., {topic}, {tone})
- Generate test cases by filling template variables with sample data
- View simulated AI completions using a rule-based mock engine that varies output by prompt length, keywords, and structure
- Compare multiple prompt variations side-by-side in a split-pane interface
- Track prompt performance metrics (simulated token count, response time, clarity score)
- Browse prompt history with filtering by template name and creation date

## Tech stack

Python, FastAPI, SQLite, Flask, Jinja2, HTML/CSS

## How to run locally
### Prerequisites

- Node.js 18 or newer
- Python 3.10 or newer
### Environment variables


Copy `.env.example` to `.env` in the project root before starting the app.

**Windows**

```bash
copy .env.example .env
```

**macOS / Linux**

```bash
cp .env.example .env
```

Fill in any empty values:

- `DATABASE_URL` — example: `sqlite:///./app.db`
- `SECRET_KEY` — example: `change-me`
- `DEBUG` — example: `true`
Start the **backend** and the **frontend** in **two separate terminals**. Start the backend first. Do **not** run `npm run build` just to try the app — that is a production build step.

### 1. Backend (terminal 1)

```bash
cd .
python -m venv .venv
```

**Windows (PowerShell or Command Prompt)**

```bash
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

**macOS / Linux**

```bash
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Backend API: http://127.0.0.1:8000  
API docs: http://127.0.0.1:8000/docs

Leave this terminal running.

### 2. Frontend (terminal 2)

```bash
cd .
npm install
npm run dev
```

Frontend app: http://localhost:5173

Open the frontend URL in your browser. Keep **both** terminals running while you use the app.

### Optional production build

Only after the app already runs with `npm run dev`:

```bash
cd .
npm run build
```

## Project structure

```
.
├── src/
│   ├── App.jsx
│   ├── index.css
│   └── main.jsx
├── static/
│   └── style.css
├── templates/
│   ├── static/
│   │   └── style.css
│   ├── compare.html
│   ├── editor.html
│   └── index.html
├── .env.example
├── .gitignore
├── database.py
├── index.html
├── main.py
├── mock_llm.py
├── models.py
├── package-lock.json
├── package.json
├── requirements.txt
├── routers.py
├── schemas.py
├── seed_data.py
├── test_mock_llm.py
└── vite.config.js
```

---

Generated with [Alviora AI](https://alvioraai.com).
