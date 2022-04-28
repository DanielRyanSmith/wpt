import json
import requests

from .utils import get

PLATFORM_INFO = [("Linux_x64", "linux"), ("Mac", 'mac'), ("Win", "win"), ("Win_x64", "win")]
SNAPSHOTS_PATH = "https://storage.googleapis.com/chromium-browser-snapshots/"


def main():
    revisions = None
    # Load existing pinned revisions.
    with open("tools/wpt/latest_chromium_revisions.json", "r") as f:
        revisions = json.load(f)
    with open("tools/wpt/latest_chromium_revisions.json", "w") as f:
        for platform, file_suffix in PLATFORM_INFO:
            filename = f"chrome-{file_suffix}.zip"
            try:
                # Check for latest revision.
                url = f"{SNAPSHOTS_PATH}{platform}/LAST_CHANGE"
                new_revision = get(url).text.strip()

                # Check the status without downloading the content (this is a streaming request).
                url = f"{SNAPSHOTS_PATH}{platform}/{new_revision}/{filename}"
                get(url)
            except requests.RequestException:
                # Try other platforms without saving info if a request error occurs.
                continue
            # replace old revision with the new one if successful.
            revisions[platform] = new_revision
        f.write(f"{json.dumps(revisions)}\n")


if __name__ == "__main__":
    main()
