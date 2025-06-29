import os
import uuid
from typing import Any, Dict, List

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

load_dotenv()


PORT = int(os.getenv("PORT"))


app = FastAPI()


game_sessions: Dict[str, Dict[str, Any]] = {}


class GameSession(BaseModel):
    session_id: str
    game_template: str
    status: str


class CreateGameSessionRequest(BaseModel):
    game_template: str
    user_prompt: str = ""


@app.get("/sessions", response_model=List[GameSession])
async def get_game_sessions():
    """
    Retrieve a list of all active game sessions.
    """
    return list(game_sessions.values())


@app.post("/sessions", response_model=GameSession, status_code=201)
async def create_game_session(request: CreateGameSessionRequest):
    """
    Create a new game session.
    A real implementation would use the user_prompt to generate a new game or use the game_template.
    """
    session_id = str(uuid.uuid4())
    new_session = GameSession(
        session_id=session_id, game_template=request.game_template, status="active"
    )
    game_sessions[session_id] = new_session.model_dump()
    return new_session


@app.get("/sessions/{session_id}", response_model=GameSession)
async def get_game_session_details(session_id: str):
    """
    Get details for a specific game session.
    """
    if session_id not in game_sessions:
        raise HTTPException(status_code=404, detail="Game session not found")
    return game_sessions[session_id]


# Example of a pre-existing game session for demonstration
initial_session_id = str(uuid.uuid4())
game_sessions[initial_session_id] = {
    "session_id": initial_session_id,
    "game_template": "default_template",
    "status": "active",
}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)
