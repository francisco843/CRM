# CRM GitHub

Local web CRM, cross-platform, and ready to upload to GitHub. It runs on Python + Flask + SQLite, so it behaves the same on macOS, Windows, and Linux as long as Python 3 is installed.

## Included features

- Dashboard with pipeline metrics, tasks, and recent activity.
- Full CRUD for companies, contacts, deals, and tasks.
- Global search across modules.
- Local SQLite database.
- Internal activity log.
- `scripts/` folder with automatic execution on server startup.
- Demo data and example addons included.

## Structure

```text
CRM Github/
├── app.py
├── crm/
│   ├── __init__.py
│   ├── addons.py
│   ├── db.py
│   ├── routes.py
│   ├── static/
│   └── templates/
├── scripts/
│   ├── 01_demo_seed.py
│   └── 02_overdue_tasks.py
├── tests/
├── requirements.txt
└── README.md
```

## Prerequisites

The CRM requires:

- Python 3.11 or newer
- `venv` support
- `pip`

### Install Python

macOS with Homebrew:

```bash
brew install python
```

Ubuntu / Debian:

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip
```

Windows PowerShell with `winget`:

```powershell
winget install -e --id Python.Python.3.12
```

## Installation

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the local server

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Scripts / Addons

Every time you run the web server, the CRM scans the `scripts/` folder and executes all `.py` files in alphabetical order.

### Addon contract

Supported patterns:

- Top-level executable code.
- `if __name__ == "__main__": ...`
- `run(context)`
- `main(context)`
- `main()`

The `context` object exposes:

- `project_root`
- `db_path`
- `query_all(sql, params=())`
- `query_one(sql, params=())`
- `execute(sql, params=())`
- `executemany(sql, rows)`
- `get_setting(key, default=None)`
- `set_setting(key, value)`
- `register_activity(entity_type, entity_id, action, summary)`
- `log(message)`

### Minimal example

```python
def run(context):
    context["log"]("My addon ran when the CRM started")
```

### Recommendation

Make your addons idempotent. Since they run on every startup, they should validate state before inserting or updating records.

## Database

The SQLite database is created automatically at:

```text
instance/crm.sqlite3
```

## Run tests

```bash
python -m unittest discover -s tests
```

## Upload to GitHub

```bash
git init
git add .
git commit -m "Initial CRM GitHub"
```

Then connect the remote and run `git push`.
