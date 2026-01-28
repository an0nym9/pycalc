import math
from pycalc.utils.console import clear_screen, readline, show_menu
from pycalc.utils.guards import handle_exception

@handle_exception
def interest(
    *,
    I: float | None = None,
    P: float | None = None,
    r: float | None = None,
    t: float | None = None,
    compound: bool = False,
    n: int = 1,
    FV: bool = False,
) -> float | ValueError:
    """Calculate interest or future value for simple or compound interest."""
    if compound:
        if FV or I is None:
            if P is None:
                raise ValueError("Cannot solve for P in compound interest.")
            if r is not None and t is not None:
                fv = P * (1 + r/n)**(n*t)
                if FV:
                    return fv
                else:
                    return fv - P
            elif r is None and t is not None:
                return n * ((FV / P) ** (1/(n*t)) - 1)
            elif t is None and r is not None:
                return math.log(FV / P) / (n * math.log(1 + r/n))
    else:
        if I is None and all(n is not None for n in (P, r, t)):
            return P * r * t
        elif P is None and all(n is not None for n in (I, r, t)):
            return I / (r * t)
        elif r is None and all(n is not None for n in (I, P, t)):
            return I / (P * t)
        elif t is None and all(n is not None for n in (I, P, r)):
            return I / (P * t)
    raise ValueError("Not enough information to solve.")

def run_finance() -> None:
    """Runs the main loop."""
    options = ("simple", "compound",)
    while (
        user_option := show_menu(
            "Finance",
            options + ("exit",),
            capitalize_options=True,
        ).unwrap(),
    ) != "exit":
        if user_option not in options:
            print("Unknown option, try again.")
            continue
        print("Enter space for no values.")
        cond = options[user_option-1] == "compound"
        I = readline("Enter the value for I:", cast=float, allow_none=True).unwrap()
        P = readline("Enter the value for P:", cast=float, allow_none=True).unwrap()
        r = readline("Emter the value for r:", cast=float, allow_none=True).unwrap()
        t = readline("Enter the value for t:", cast=float, allow_none=True).unwrap()
        n = readline("Enter the value for n:", cast=float, allow_none=True).unwrap() if cond else None
        result = interest(I = I, P = P, r = r, t = t, n = n, compound=cond).unwrap()
        print(f">> {result:.2f}")
        readline("Press enter to continue...", enter_only=True).unwrap()


