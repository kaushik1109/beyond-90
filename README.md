# Beyond 90 ⚽

Beyond 90 is a football-focused platform for analysis, opinions, tactical discussions, and stories that go beyond the final whistle.

The project is being built as a full-stack application using FastAPI, PostgreSQL, and modern web technologies. The goal is to create a platform where football fans can publish and explore articles covering matches, transfers, tactics, player performances, and broader football discussions.

## Current Status

🚧 Early Development

The project is currently focused on building the backend API and core infrastructure.

## Tech Stack

### Backend

* FastAPI
* Python
* SQLAlchemy
* PostgreSQL
* Alembic

### Future Plans

* JWT Authentication
* Docker
* React / Next.js Frontend
* Football Data APIs
* Search Functionality
* AI-Powered Football Insights

## Project Structure

```text
beyond90/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   └── main.py
│
├── tests/
├── requirements.txt
└── README.md
```

## Running Locally

### Create and activate a virtual environment

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the development server

```bash
fastapi dev app/main.py
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Vision

Beyond 90 aims to become more than a simple football blog. The long-term goal is to evolve into a football platform featuring:

* Match analysis
* Tactical breakdowns
* Transfer tracking
* Football statistics
* Community discussions
* AI-assisted football insights

## Why "Beyond 90"?

Football conversations don't end when the referee blows the final whistle.

Beyond 90 is built around the idea of exploring the stories, tactics, decisions, and narratives that continue after the 90 minutes are over.
