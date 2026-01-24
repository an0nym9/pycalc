import re
from pycalc.utils.console import clear_screen, readline, show_menu

class Polynomial:
    def __init__(self, exp: str) -> None:
        """Initialize a Polynomial object."""
        self.exp = exp

    def get_coeffs(self) -> tuple[int, ...]:
        """Return the coefficients of the given polynomial expression."""
        return tuple(map(int, re.findall(r"(\d+)[a-zA-Z]+", self.exp)))

    def get_terms(self) -> tuple[str, ...]:
        """Return the terms of the given polynomial expression."""
        return tuple(re.findall(r"\d+[a-zA-Z]+|\d+|[a-zA-Z]+", self.exp))

    def get_vars(self) -> tuple[str, ...]:
        """Returns the variables of the given polynomial expression."""
        return tuple(set(re.findall(r"[a-zA-Z]+", self.exp)))

    def get_type_by_term(self) -> str:
        """Return the type by using the terms of the given polynomial expression."""
        terms_count = len(self.get_terms())
        match terms_count:
            case 1:
                return "monomial"
            case 2:
                return "binomial"
            case 3:
                return "trinomial"
            case _:
                return "polynomial"

    def get_type_by_degree(self) -> str:
        """Return the type by using the degree of the given polynomial expression."""
        if not re.search(r"[a-zA-Z]", self.exp):
            return "constant"
        degrees = re.findall(r"[a-zA-Z]+\^(\d+)|\d+[a-zA-Z]+\^(\d+)", self.exp)
        max_degree =  max(list(map(int, [
            s for s in (*degrees[0], '1',)
            if s.strip() != '']))
        ) if len(degrees) >= 1 else 1
        match max_degree:
            case 1:
                return "linear"
            case 2:
                return "quadratic"
            case 3:
                return "cubic"
            case _:
                return "polynomial"

def run_algebra() -> None:
    """Runs the main loop."""
    options = (
        "get coefficients", "get terms",
        "get variables", "get type by term",
        "get type by degree",
    )
    while (
         clear_screen(),
         show_menu("Algebra", options + ("exit",), capitalize_options=True),
         user_option := readline("Enter your option (number):", cast=int).unwrap(),
    )[-1] != len(options) + 1:
        if not (1 <= user_option <= len(options)):
            print("Unknown option, try again.")
            continue
        poly = Polynomial(readline("Enter a polynomial:").unwrap()) # Assume user types a polynomial
        match options[user_option-1]:
            case "get coefficients":
                result = poly.get_coeffs()
            case "get terms":
                result = poly.get_terms()
            case "get variables":
                result = poly.get_vars()
            case "get type by term":
                result = poly.get_type_by_term()
            case "get type by degree":
                result = poly.get_type_by_degree()
        print(f">> {result}")
        readline("Press enter to continue...", enter_only=True).unwrap()
