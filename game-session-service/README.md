# Game Session Service

Backend service for managing QuestGen game sessions, player interactions, and game state.

## 🚀 Features

- **RESTful API**: HTTP endpoints for game session management
- **WebSocket Support**: Real-time updates for game events
- **Session Persistence**: Store and retrieve game session data

## 🛠️ Prerequisites

- Python 3.12
- uv installed
- pre-commit installed and initialized

## 🚀 Quick Start

1. Install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate
   uv sync
   ```

2. Set up environment variables (create a `.env` file):


3. Start the service:
   ```bash
   make start
   ```

5. API documentation will be available at `http://localhost:8000/docs`

## 🏗️ Project Structure

```
game-session-service/
├── main.py            # Main Streamlit application
├── Makefile           # Build and run commands
├── pyproject.toml     # Project configuration
├── README.md          # Project documentation
└── ...
```

## 📚 API Documentation

Once the service is running, you can access:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🔧 Development

### Environment Setup

1. Create and activate a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate
   ```

2. Install development dependencies:
   ```bash
   uv sync
   ```
