#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3 is required to run CRM GitHub."
  exit 1
fi

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate
python -m pip install -r requirements.txt

HOST="${HOST:-127.0.0.1}"
PORT="${PORT:-5000}"

echo "Starting CRM GitHub on http://${HOST}:${PORT}"
exec python app.py
