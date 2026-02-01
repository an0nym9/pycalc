import os
import sys
import time
import msvcrt
from pycalc.utils.guards import handle_exception, enhance_params

clear_screen = lambda: os.system("cls" if os.name == "nt" else "clear")

@handle_exception
@enhance_params
def readline(
    msg: str = "",
    /,
    *,
    cast: callable = str,
    bool_condition: tuple[str, ...] = ("yes", "y", "true"),
    attempts: int = 1,
    case_sensitive: bool = False,
    enter_only: bool = False,
    allow_none: bool = False,
) -> any:
    """Reads user input and cast it into a specific type."""
    if cast not in (str, bool, float, int,):
        raise ValueError(f"Unknown or unsupported type '{cast.__name__}'.")
    if enter_only:
        print(msg, end='', flush=True)
        if os.name == "nt":
            while True:
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    if key in (b'\r', b' ',):
                        break
        else:
            import tty
            import termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            while True:
                key = sys.stdin.read(1)
                if key == b' ':
                    break
        return None
    while attempts != 0:
        user_input = input(f"{msg} ").strip()
        try:
            if cast is bool:
                res = user_input if not case_sensitive else user_input.lower()
                if res in bool_condition:
                    return True
                return False
            return cast(user_input)
        except ValueError:
            if allow_none:
                return None
            print(f"Invalid input, expecting of type '{cast.__name__}'.")
            attempts -= 1
    animateText("Failed to get input, terminating function...")
    return None

@handle_exception
@enhance_params
def animateText(msg: str, /, *, delay: float = 0.1) -> None:
    """Give a typing animation for 'msg'."""
    for char in msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

@handle_exception
@enhance_params
def show_menu(
    title: str,
    options: tuple[str, ...],
    /,
    *,
    width: int = 50,
    capitalize_options: bool = False,
) -> None:
    """Print out a menu."""
    clear_screen()
    s = 0
    def draw() -> None:
        clear_screen()
        print(f"+{'=' * width}+\n|{title.center(width)}|\n+{"=" * width}+", flush=True)
        print(f"|{' ' * width}|", flush=True)
        for i, val in enumerate(options, start=1):
            option = val.capitalize() if capitalize_options else val
            left = f"| {'>' if (s % len(options)) == i - 1 else ''} [{i}] "
            print(f"{left}{option.ljust(width-len(left)+1)}|", flush=True)
        print(f"|{' ' * width}|", flush=True)
        print(f"+{'=' * width}+", flush=True)
    draw()
    while True:
        if os.name == "nt":
            if msvcrt.kbhit():
                match msvcrt.getch():
                    case b'\r' | b' ':
                        return options[s % len(options)]
                    case b'\x00' | b'\xe0':
                        key = msvcrt.getch()
                        if key == b'H':
                            s -= 1
                        elif key == b'P':
                            s += 1
                    case b'w':
                        s -= 1
                    case b's':
                        s += 1
                draw()
        else:
            key = sys.stdin.read(1)
            if key == b'\x1b':
                key += sys.stdin.read(2)
                s += 1 if key == '\1xb[A' else -1
                draw()
                if key == b'\x1b':
                    return options[s % len(options)]
