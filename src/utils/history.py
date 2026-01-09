import json
import os
from datetime import datetime
from utils.console import clear_screen
from utils.guards import handle_exception, enhance_params

current_dir = os.path.dirname(os.path.abspath(__file__))
HISTORY_PATH = os.path.abspath(os.path.join(current_dir, "..", "..", "data", "history.json"))

def create_history() -> None:
    """Create history if not exists."""
    try:
        with open(HISTORY_PATH, 'x') as f:
            json.dump([], f, indent=4)
        print("Successfully created History JSON.")
    except FileExistsError:
        print("History JSON already exists.")

def clear_history() -> None:
    """Clear the history."""
    if not os.path.exists(HISTORY_PATH):
        print("Can't find history JSON.")
        return
    with open(HISTORY_PATH, 'w') as f:
        json.dump([], f, indent=4)
    print("Successfully cleared history JSON.")

def load_history() -> list:
    """Load history if exists."""
    if os.path.exists(HISTORY_PATH):
        with open(HISTORY_PATH, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []

@handle_exception
@enhance_params
def add_history(content: str,) -> None:
    """Add content to history."""
    data = load_history()
    data.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "content": content,
    })
    with open(HISTORY_PATH, 'w') as f:
        json.dump(data, f, indent=4)
    print(content)

@handle_exception
@enhance_params
def show_history(*, width: int = 60) -> None:
    """Show previous history."""
    clear_screen()
    with open(HISTORY_PATH, 'r') as f:
        data = json.load(f)
    print(f"+{'=' * width}+\n|{"History".center(width)}|\n+{'=' * width}+")
    for history in data:
        left = f"| [{history["time"]}] "
        print(f"{left}{history["content"].ljust(width-len(left))} |")
    print(f"+{'=' * width}+")
