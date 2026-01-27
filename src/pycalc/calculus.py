from pycalc.utils.console import clear_screen, readline, show_menu
from pycalc.utils.guards import handle_exception

@handle_exception
def arithmetic_sequence(
    *,
    tn: float | None = None,
    ti: float | None = None,
    n: float | None = None,
    d: float | None = None,
) -> float | ValueError:
    """Solve arithmetic sequences."""
    if (tn, ti, n, d).count(None) > 1:
        raise ValueError("Need only one unknown value.")
    if tn is None:
        return ti + (n - 1) * d
    elif ti is None:
        return tn / d / (n - 1)
    elif n is None:
        return (tn - ti) / d + 1
    elif d is None:
        return (tn - ti) / (n - 1)
    raise ValueError("Not enough data to solve.")

@handle_exception
def arithmetic_series(
    *,
    sn: float | None = None,
    n: float | None = None,
    ti: float | None = None,
    tn: float | None = None,
    d: float | None = None,
) -> float | ValueError:
    """Solve arithmetic series."""
    if (sn, n, ti, tn, d).count(None) > 2:
        raise ValueError("Need only 2 unknown value to solve.")
    if d is None:
        if sn is None:
            return (n / 2) * (ti + tn)
        elif n is None:
            return sn * 2 / (ti + tn)
        elif ti is None:
            return sn / (n / 2) - tn
        elif tn is None:
            return sn / (n / 2) - ti
    else:
        if sn is None:
            return (n / 2) * (2(ti) + (n - 1) * d)
        elif n is None:
            return sn * 2 / (2(ti) + (n - 1) * d)
        elif ti is None:
            return sn / (n / 2) - ((n - 1) * d)
        elif d is None:
            return sn / (n / 2) / (2(ti) + (n - 1))
    raise ValueError("Not enough data to solve.")

@handle_exception
def arithmetic_difference(
    *,
    tn1: float | None = None,
    tn2: float | None = None,
) -> float | ValueError:
    """Calculate the difference for arithmetic."""
    if any(tn is None for tn in (tn1, tn2,)):
        raise ValueError("Not enough data to find the difference.")
    return tn1 - tn2

def run_calculus() -> None:
    """Runs the main loop."""
    options = ("arithmetic sequence", "arithmetic series", "arithmetic difference",)
    while (
         clear_screen(),
         show_menu("Finance", options + ("exit",), capitalize_options=True),
         user_option := readline("Enter your option (number):", cast=int).unwrap(),
    )[-1] != len(options) + 1:
        if not (1 <= user_option <= len(options)):
            print("Unknown option, try again.")
            continue
        match (option := options[user_option-1]):
            case "arithmetic sequence" | "arithemtic series":
                cond = option == "arithmetic series"
                if cond:
                    sn = readline("Enter the value for S_n:", cast=float, allow_none=True).unwrap()
                tn = readline("Enter the value for t_n:", cast=float, allow_none=True).unwrap()
                ti = readline("Enter the value for t_1:", cast=float, allow_none=True).unwrap()
                n = readline("Enter the value for n:", cast=float, allow_none=True).unwrap()
                d = readline("Enter the value for d:", cast=float, allow_none=True).unwrap()
                result = (
                    arithmetic_sequence(tn=tn, ti=ti, n=n, d=d).unwrap()
                    if not cond else
                    arithmetic_series(sn=sn, n=n, ti=ti, tn=tn, d=d).unwrap()
                )
            case "arithmetic difference":
                tn1 = readline("Enter the value for t_n:", cast=float, allow_none=True).unwrap()
                tn2 = readline("Enter the value for t_n-1:", cast=float, allow_none=True).unwrap()
                result = arithmetic_difference(tn1=tn1, tn2=tn2).unwrap()
        print(f">> {result}")
        readline("Press enter to continue...", enter_only=True).unwrap()
