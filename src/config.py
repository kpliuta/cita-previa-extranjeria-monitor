"""
Loads the configuration from the .env file and makes it available to the application.
"""
import os
from typing import Optional

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_env_var(name: str, default: Optional[str] = None) -> str:
    """
    Gets an environment variable, raising an error if it's not set and no default is provided.

    Args:
        name: The name of the environment variable.
        default: The default value to return if the environment variable is not set.

    Returns:
        The value of the environment variable.

    Raises:
        ValueError: If the environment variable is not set and no default is provided.
    """
    value = os.getenv(name)
    if value is None:
        if default is not None:
            return default
        raise ValueError(f"Environment variable {name} is not set and no default was provided.")
    return value


# --- Core Parameters ---

# Output directory for scraper data
SCRAPER_OUTPUT_DIR: str = get_env_var("SCRAPER_OUTPUT_DIR", "/mnt/cita-previa-extranjeria-monitor")

# Telegram API URL
TELEGRAM_API_URL: str = get_env_var("TELEGRAM_API_URL")

# Telegram Bot Token
TELEGRAM_BOT_TOKEN: str = get_env_var("TELEGRAM_BOT_TOKEN")

# Telegram Chat ID
TELEGRAM_CHAT_ID: str = get_env_var("TELEGRAM_CHAT_ID")

# --- User Parameters ---

# Province to search for appointments
PROVINCE: str = get_env_var("PROVINCE")

# Office to search for appointments
OFFICE: str = get_env_var("OFFICE")

# Procedure to search for appointments
PROCEDURE: str = get_env_var("PROCEDURE")

# NIE
NIE: str = get_env_var("NIE")

# Full name
FULL_NAME: str = get_env_var("FULL_NAME")
