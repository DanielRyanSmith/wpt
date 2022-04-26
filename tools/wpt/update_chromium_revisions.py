import os
import sys
import json
import requests

from .utils import get


def build_url_string(platform):
    return f"https://storage.googleapis.com/chromium-browser-snapshots/{platform}/LAST_CHANGE"


def main():
    revisions = None
    with open("tools/wpt/latest_chromium_revisions.json", "r") as f:
        revisions = json.load(f)
    with open("tools/wpt/latest_chromium_revisions.json", "w") as f:
        for platform in ["Linux_x64", "Mac", "Win"]:
            try:
                new_revision = get(build_url_string(platform)).text.strip()
            except requests.RequestException:
                continue
            revisions[platform] = new_revision
        f.write(f"{json.dumps(revisions)}\n")


if __name__ == "__main__":
    main()
