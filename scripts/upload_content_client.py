from __future__ import annotations

import argparse
import base64
import json
from pathlib import Path
from urllib import request


DEFAULT_API_URL = "https://content-receiver.replit.app/api/upload-content"
DEFAULT_SOURCE_DIR = Path("~/Desktop").expanduser()


def upload_file(url: str, source_file: Path, filename: str) -> None:
    payload = {
        "filename": filename,
        "content_base64": base64.b64encode(source_file.read_bytes()).decode("ascii"),
    }

    body = json.dumps(payload).encode("utf-8")
    req = request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with request.urlopen(req) as response:
        print(f"{filename}: {response.read().decode('utf-8')}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Upload all files from a local folder, including subfolders, to the upload-content API."
    )
    parser.add_argument(
        "--url",
        default=DEFAULT_API_URL,
        help="Target upload-content API URL.",
    )
    parser.add_argument(
        "--folder",
        default=str(DEFAULT_SOURCE_DIR),
        help="Local folder whose files will be uploaded recursively.",
    )
    args = parser.parse_args()

    source_dir = Path(args.folder).expanduser()
    if not source_dir.exists():
        raise SystemExit(f"Folder does not exist: {source_dir}")
    if not source_dir.is_dir():
        raise SystemExit(f"Path is not a folder: {source_dir}")

    source_files = sorted(path for path in source_dir.rglob("*") if path.is_file())
    if not source_files:
        raise SystemExit(f"No files found in folder: {source_dir}")

    for source_file in source_files:
        upload_file(
            args.url,
            source_file,
            source_file.relative_to(source_dir).as_posix(),
        )


if __name__ == "__main__":
    main()
