import os
import json

from pycalc.utils.console import readline, show_menu
from pycalc.utils.history import add_history

current_dir = os.path.dirname(os.path.abspath(__file__))
ELEMENTS_PATH = os.path.abspath(os.path.join(current_dir,  "..", "..", "data", "elements", "elements.json"))

def load_elements(*, default: dict = {}) -> dict:
    """Load all the elements in elements.json."""
    if os.path.exists(ELEMENTS_PATH):
        with open(ELEMENTS_PATH, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return default
    return default

def valid_element(name: str, *, elements: dict = load_elements()) -> bool:
    """Check if an element exists."""
    valid_element_names = tuple(
        (keys := tuple(elements.keys())) +
        tuple(elements[element]["name"] for element in keys),
    )
    return name in valid_element_names

class Element:
    elements = load_elements() # Load all the elements

    def __init__(self, symbol: str, /) -> None:
        """Initialize an Element object."""
        self.symbol = symbol
        self.name = Element.elements[symbol]["name"]
        self.atomic_number = Element.elements[symbol]["atomic number"]
        self.protons = Element.elements[symbol]["protons"]
        self.neutrons = Element.elements[symbol]["neutrons"]
        self.atomic_mass = Element.elements[symbol]["atomic mass"]
        print(self.name)

    def __add__(self, other: Element, /) -> str:
        """Add two Element objects and balance."""
        if self.protons == other.protons:
            return f"{self.symbol}{other.symbol}"
        fel = f"{self.symbol}{f"_{other.protons}" if other.protons != 1 else ''}"
        sel = f"{other.symbol}{f"_{self.protons}" if self.protons != 1 else ''}"
        return fel + sel

def run_chemistry():
    """Runs the main loop."""
    options = (
        "get name", "get atomic number", "get protons",
        "get neutrons", "get atomic mass", "balance",
    )
    while (user_option := show_menu(
            "Chemistry",
            options +  ("exit",),
            capitalize_options=True,
        ).unwrap()) != "exit":
        if user_option not in options:
            print("Unknown option, try again.")
            continue
        if "get" in user_option:
            symbol = readline("Enter the element symbol:").unwrap()
            if not valid_element(symbol):
                print("Element doesn't exist, try again.")
                continue
            element = Element(symbol)
            match user_option:
                case "get name":
                    result = element.name
                case "get atomic number":
                    result = element.atomic_number
                case "get protons":
                    result = element.protons
                case "get neutrons":
                    result = element.neutrons
                case "get atomic mass":
                    result = element.atomic_mass
        elif user_option == "balance":
            symbol1 = readline("Enter the first element symbol:").unwrap()
            symbol2 = readline("Enter the second element symbol:").unwrap()
            if not symbol1 or not symbol2:
                print("Atleast one of the element doesn't exist, try again.")
                continue
            result = Element(symbol1) + Element(symbol2)
        print(f"= {result}")
        add_history(result)
        readline("Press enter to continue...", enter_only=True).unwrap()
