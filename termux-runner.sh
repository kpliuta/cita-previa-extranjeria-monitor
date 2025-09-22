#!/bin/sh

TERMUX_WEB_SCRAPER_VERSION="0.1.0"

# Exit immediately if a command exits with a non-zero status.
set -e

# Check if git is installed
if ! command -v git >/dev/null 2>&1; then
    echo "Error: git is not installed. Please install it and try again."
    exit 1
fi

# Get the absolute path to the scenario directory.
WORK_DIR=$(realpath "$(dirname "$0")")

# Clone the termux-web-scraper repository.
if [ ! -d "$WORK_DIR/termux-web-scraper" ]; then
  echo "Cloning termux-web-scraper..."
  git clone https://github.com/kpliuta/termux-web-scraper.git "$WORK_DIR/termux-web-scraper"
  git -C "$WORK_DIR/termux-web-scraper" checkout "$TERMUX_WEB_SCRAPER_VERSION"
fi

# Execute the scraper script in a loop with a 3 hour timeout.
"$WORK_DIR/termux-web-scraper/scripts/run.sh" \
    --work-dir "$WORK_DIR" \
    --scenario-file src/main.py \
    --upgrade \
    --loop \
    --loop-timeout 10800 \
    --loop-error-ignore \
    --output-dir /sdcard/cita-previa-extranjeria-monitor:/mnt/cita-previa-extranjeria-monitor
