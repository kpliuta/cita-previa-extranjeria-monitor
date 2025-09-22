# Cita Previa Extranjeria Monitor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A web scraper that automates the soul-crushing process of checking for appointments (cita previa) at the Spanish immigration office (extranjería).

If you've ever tried to book an appointment, you know the drill: endless refreshing, cryptic error messages, and the sinking feeling that you might be clicking your way into oblivion. This script is your friendly neighborhood robot, tirelessly checking for you so you can reclaim your sanity.

This script is designed to be run in two primary environments:
1.  On an Android device using **Termux** and the `termux-web-scraper` framework.
2.  On a standard desktop environment as a Python Selenium script.

## Features

*   **Automated Checking:** Runs on a loop to constantly check for available appointment slots.
*   **Telegram Notifications:** Sends you an immediate alert via Telegram the moment a potential slot is found.
*   **Configurable:** Easily configure your province, office, procedure type, and personal details via a `.env` file.
*   **Human-like Behavior:** Uses randomized delays and user agents to avoid being blocked.

## How it Works

The scraper uses Selenium to automate a Firefox browser to navigate the labyrinthine government website.

1.  **Launch:** The script starts a new Firefox browser session.
2.  **Navigate & Fill:** It navigates to the appointment website and automatically fills in your province, office, procedure, and personal details from your configuration.
3.  **Check for Availability:** It proceeds to the final page and checks for the dreaded "En este momento no hay citas disponibles" message.
4.  **ALERT!:** If that message is *not* found, it assumes a slot may be available. It immediately saves a screenshot and sends an alert to your Telegram bot.

## Prerequisites

Before you can use the Termux Web Scraper, you need to have the following installed on your Android device:

*   **Termux:** You can download Termux from the [F-Droid](https://f-droid.org/en/packages/com.termux/) or [Google Play](https://play.google.com/store/apps/details?id=com.termux) store.
*   **Git:** You can install Git in Termux by running `pkg install git`.

You also need to:

*   **Disable Battery Optimization:** Disable battery optimization for Termux to prevent it from being killed by the Android system.
*   **Acquire a Wakelock:** Acquire a wakelock in Termux to prevent the device from sleeping while your scraper is running.
*   **Address Phantom Process Killing (Android 12+):** On Android 12 and newer, you may need to disable phantom process killing to prevent Termux from being killed. You can do this by running the following command in an ADB shell:
    ```bash
    ./adb shell "settings put global settings_enable_monitor_phantom_procs false"
    ```

## Getting Started

### Termux Environment
1.  Get started by launching Termux on your Android device and cloning the repository:
    ```bash
    git clone https://github.com/kpliuta/cita-previa-extranjeria-monitor.git
    ```

2.  Then, navigate to a project and edit `.env` with your credentials and settings:
    ```bash
    cd cita-previa-extranjeria-monitor
    nano src/.env
    ```

3.  Finally, start the runner script:
    ```bash
    ./termux-runner.sh
    ```
    
### Desktop Environment
To run the scraper on a desktop machine, simply execute the `main.py` script, specifying unique ID for the session:
```bash
SCRAPER_SESSION_ID=session_id poetry run python src/main.py
```

## Configuration

The following environment variables must be set in the `src/.env` file:

### Core Parameters
*   `SCRAPER_OUTPUT_DIR`: Absolute path to a directory for storing state files and screenshots.
*   `TELEGRAM_API_URL`: The Telegram Bot API URL (default: `https://api.telegram.org`).
*   `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
*   `TELEGRAM_CHAT_ID`: The ID of the Telegram chat where alerts will be sent.

### User Parameters
*   `PROVINCE`: The province to search in (default: `Madrid`).
*   `OFFICE`: The specific office (oficina) name.
*   `PROCEDURE`: The specific procedure (trámite) you are applying for.
*   `NIE`: Your NIE number (Número de Identificación de Extranjero).
*   `FULL_NAME`: Your full name as it should appear on the application.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
