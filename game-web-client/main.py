import pandas as pd
import requests
import streamlit as st

BACKEND_URL = "http://127.0.0.1:8000"


def get_sessions():
    """Fetches all game sessions from the backend."""
    try:
        response = requests.get(f"{BACKEND_URL}/sessions")
        response.raise_for_status()  # Raises an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to backend: {e}")
        return []


def create_session(game_template: str, user_prompt: str = ""):
    """Creates a new game session via the backend."""
    try:
        payload = {"game_template": game_template, "user_prompt": user_prompt}
        response = requests.post(f"{BACKEND_URL}/sessions", json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error creating session: {e}")
        return None


def main():
    """
    Main function to run the Streamlit UI.
    """
    st.set_page_config(page_title="Game Lobby", layout="wide")

    st.title("Game Sessions Lobby")

    # --- Create New Session Form ---
    with st.expander("Create a New Game Session", expanded=False):
        with st.form("create_session_form"):
            st.write("Create a session from a template or with a custom prompt.")

            creation_type = st.radio(
                "Creation Type", ("Use a Game Template", "Use a Custom Prompt")
            )

            game_template_input = st.selectbox(
                "Game Template",
                ["default_template", "template_a", "template_b"],
                disabled=(creation_type == "Use a Custom Prompt"),
            )

            user_prompt_input = st.text_area(
                "Custom Prompt",
                "Describe the game you want to create...",
                disabled=(creation_type == "Use a Game Template"),
            )

            submitted = st.form_submit_button("Create Session")
            if submitted:
                if creation_type == "Use a Game Template":
                    new_session = create_session(game_template=game_template_input)
                else:
                    new_session = create_session(
                        game_template="custom", user_prompt=user_prompt_input
                    )

                if new_session:
                    st.success(
                        f"Successfully created session ID: {new_session['session_id']}"
                    )
                else:
                    st.error("Failed to create session.")

    # --- Display Existing Sessions ---
    st.header("Available Sessions")

    sessions = get_sessions()

    if not sessions:
        st.info("No active game sessions found. Create one above!")
    else:
        session_data = {
            "Session ID": [s["session_id"] for s in sessions],
            "Game Template": [s["game_template"] for s in sessions],
            "Status": [s["status"] for s in sessions],
            "Actions": [s["session_id"] for s in sessions],  # Used for button keys
        }
        df = pd.DataFrame(session_data)

        col_defs = {
            "Session ID": st.column_config.TextColumn(width="large"),
            "Game Template": st.column_config.TextColumn(),
            "Status": st.column_config.TextColumn(),
            "Actions": st.column_config.Column(label="Actions"),
        }

        st.dataframe(
            df, use_container_width=True, hide_index=True, column_config=col_defs
        )

        st.write("---")
        for session_id in df["Actions"]:
            cols = st.columns((3, 1, 1, 5))
            cols[0].text(f"Actions for {session_id[:8]}...")

            if cols[1].button("Join", key=f"join_{session_id}"):
                st.toast(f"Joining session {session_id[:8]}...")

            if cols[2].button("Details", key=f"details_{session_id}"):
                st.toast(f"Showing details for {session_id[:8]}...")
                try:
                    res = requests.get(f"{BACKEND_URL}/sessions/{session_id}")
                    res.raise_for_status()
                    st.json(res.json())
                except requests.exceptions.RequestException as e:
                    st.error(f"Could not get details: {e}")


# Main entry point
if __name__ == "__main__":
    main()
