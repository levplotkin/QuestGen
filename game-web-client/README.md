# Game Web Client

Web interface for players to interact with QuestGen game sessions.

## 🚀 Features

- **Interactive Lobby**: View and join active game sessions
- **Player Dashboard**: Two-panel interface for game interaction
- **Real-time Chat**: Built-in chat functionality
- **Game History**: Track session progress and events

## 🛠️ Prerequisites

- Python 3.12
- uv installed
- pre-commit installed and initialized
- Running instance of [game-session-service](../game-session-service/README.md)

## 🚀 Quick Start

1. Install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate
   uv sync
   ```

2. Configure environment variables (create a `.env` file if needed):
   ```
   BACKEND_URL=http://localhost:8000
   ```

3. Run the application:
   ```bash
   make start
   ```

4. Open your browser to `http://localhost:8502

## 🏗️ Project Structure

```
game-web-client/
├── main.py            # Main Streamlit application
├── Makefile           # Build and run commands
├── pyproject.toml     # Project configuration
├── README.md          # Project documentation
└── ...
```
