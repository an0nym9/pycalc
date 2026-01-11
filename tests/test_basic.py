from pycalc.basic import sum, difference, product, qoutient # type: ignore
from pycalc.utils.console import readline, show_menu # type: ignore

def test_sum() -> None:
    assert sum(2, 3, 4, 5).unwrap() == 14

def test_difference() -> None:
    assert difference(12, 3, 5).unwrap() == 4

def test_product() -> None:
    assert product(1, 2, 3, 4).unwrap() == 24

def test_qoutient() -> None:
    assert qoutient(12, 3, 2).unwrap() == 2
