import requests


def check_chromium_revision():
    old_revision = requests.get("https://storage.googleapis.com/wpt-versions/pinned_chromium_revision")
    new_revision = requests.get("https://storage.googleapis.com/wpt-versions/pinned_chromium_revision_NEW")
    if old_revision.text != new_revision.text:
        with open("tools/wpt/pinned_chromium_revision.txt", "w") as f:
            f.write(f"{new_revision.text}\n")


if __name__ == "__main__":
    check_chromium_revision()