# ZERO 3.0 — Quick run guide

## Requirements
- Python 3.8+ (recommended)
- Chrome installed (for TTS via Selenium). A matching chromedriver is included at `DATA/ZERO_DRIVERS/chromedriver.exe`.

## Quick start (Windows)
1. Open a Command Prompt at the project root (`R:\Projects\3_Advanced_AI_Assistant\ZERO_3.0`).
2. Run the setup script (creates a venv and installs packages):
   - `setup_env.bat`
3. Activate the environment:
   - `call .venv\Scripts\activate`
4. Run the UI:
   - `python USER_INTERFACE\ui.py`  (click the mic GIF to start the assistant)

Alternatives:
- Run the core assistant directly (console): `python MAIN\main.py`

## Notes & Troubleshooting
- If `pyaudio` fails to install with pip, the setup script attempts to use `pipwin` to fetch a compatible wheel.
- If Selenium raises version errors, update `DATA/ZERO_DRIVERS/chromedriver.exe` to match your Chrome version or install `webdriver-manager`.
- Ensure microphone permissions are enabled in Windows settings.

## Files added by automation
- `requirements.txt` — detected dependencies
- `setup_env.bat`, `run_ui.bat`, `run_main.bat` — convenience scripts
- `README.md` — this file

If you'd like, I can also add a small Powershell script, or create a `requirements-dev.txt` pinning versions. Just tell me which you'd prefer.