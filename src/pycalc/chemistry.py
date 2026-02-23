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

    def __add__(self, other: Element, /) -> str:
        """Add two Element objects and balance."""
        if self.protons == other.protons:
            return f"{self.symbol}{other.symbol}"
        fel = f"{self.symbol}{f"_{valence}" if (valence := other.get_valence()) != 1 else ''}"
        sel = f"{other.symbol}{f"_{valence}" if (valence := self.get_valence()) != 1 else ''}"
        return fel + sel

    def is_diatomic(self) -> bool:
        """Checks if the element is diatomic."""
        return self.symbol in ('O', 'H', 'N', 'F', 'Cl', 'Br', 'I',)

    def get_valence(self) -> int:
        """Get the total valence electrons."""
        if self.protons <= 2: # period 1
            return self.protons
        elif self.protons <= 10: # period 2
            return self.protons - 2
        elif self.protons <= 18: # period 3
            return self.protons - 10
        elif self.protons <= 26: # period 4
            return self.protons - 18
        elif self.protons <= 32: # period 5
            return self.protons - 26
        elif self.protons <= 40: # period 6
            return self.protons - 32
        elif self.protons <= 48: # period 7
            return self.protons - 40

    def get_group(self, /) -> int:
        """Get the group or family of the Element object."""
        print("Called")
        ranges = (
            (1, 3, 11, 19, 37, 55, 87), (4, 12, 20, 38, 56, 88),
            (21, 39, range(57, 72), range(89, 104)), (22, 40, 72, 104),
            (23, 41, 73, 105), (24, 42, 74, 106),
            (25, 43, 75, 107), (26, 44, 76, 108),
            (27, 45, 77, 109), (28, 46, 78, 110),
            (29, 47, 79, 111), (30, 48, 80, 112),
            (5, 13, 31, 49, 81, 113), (6, 14, 32, 50, 82, 114),
            (7, 15, 33, 51, 83, 115), (8, 16, 34, 52, 84, 116),
            (9, 17, 35, 53, 85, 117),  (2, 10, 18, 36, 54, 86, 118),
        )
        print("Called2")
        for i, r in enumerate(ranges, start=1):
            if self.atomic_number in r:
                return i
        return -1

    def get_period(self, /) -> int:
        """Get the period of the Element object."""
        ranges = (
            (1, 2), tuple(range(3, 11)),
            tuple(range(11, 19)), tuple(range(19, 37)),
            tuple(range(37, 55)), tuple(range(55, 87)),
            tuple(range(87, 199)),
        )
        for i, r in enumerate(ranges, start=1):
            if self.atomic_number in r:
                return i
        return -1

def run_chemistry():
    """Runs the main loop."""
    options = (
        "get name", "get atomic number",
        "get protons", "get neutrons",
        "get atomic mass", "get valence electrons",
        "get group", "get period",
        "balance",
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
                case "get valence electrons":
                    result = element.get_valence()
                case "get group":
                    result = element.get_group()
                case "get period":
                    result = element.get_period()
        elif user_option == "balance":
            symbol1 = readline("Enter the first element symbol:").unwrap()
            symbol2 = readline("Enter the second element symbol:").unwrap()
            if not valid_element(symbol1) or not valid_element(symbol2):
                print("Atleast one of the element doesn't exist, try again.")
                continue
            result = Element(symbol1) + Element(symbol2)
        print(f"= {result}")
        add_history(result)
        readline("Press enter to continue...", enter_only=True).unwrap()
