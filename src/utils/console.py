import os
from utils.guards import handle_exception

clear_screen = lambda: os.system("cls" if os.name == "nt" else "clear")

@handle_exception
def readline(
    msg: str,
    /,
    *,
    cast: callable = str,
    bool_condition: tuple[str, ...] = ("yes", "y", "true"),
    case_sensitive: bool = False,
    enter_only: bool = False,
) -> any:
    """Reads user input and cast it into a specific type."""
    if cast not in (str, bool, float, int,):
        raise ValueError(f"Unknown or unsupported type '{cast.__name__}'.")
    user_input = input(f"{msg} ").strip()
    if not enter_only:
        try:
            if cast is bool:
                res = user_input if not case_sensitive else user_input.lower()
                if res in bool_condition:
                    return True
                return False
            return cast(user_input)
        except ValueError:
            return None
    return None
