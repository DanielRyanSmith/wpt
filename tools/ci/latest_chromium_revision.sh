#!/bin/bash

SCRIPT_DIR=$(cd $(dirname "$0") && pwd -P)
WPT_ROOT=$SCRIPT_DIR/../..

main () {
    curl -s -S -f -o ${WPT_ROOT}/tools/latest_chromium_revision_linux https://storage.googleapis.com/chromium-browser-snapshots/Linux_x64/LAST_CHANGE
}

main
