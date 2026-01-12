# pycalc

![Version](https://img.shields.io/badge/version-0.0.4-purple?style=flat-square) ![Python](https://img.shields.io/badge/python-3.14.0-blue?style=flat-square&logo=python&logoColor=white) ![Pytest](https://img.shields.io/badge/pytest-2.2.1-orange?style=flat-square&logo=pytest&logoColor=white) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)


A simple command-line calculator built with **Python**. This simple program allows you to do math in your terminal, while keeping it simple and user-friendly.

> [!NOTE]
> This program is still under development and still not production ready.

## Features

Here are the features this program currently supports.

* **Basic Arithmetic** (`+`, `-`, `*`, `/`)
* **Prime / Semi Prime Checker**
* **Generate Prime / Semi Prime Sequence**
* **Fraction to Decimal**
* **Decimal to Fraction**
* **Factor**
* **Least Common Multiple**
* **Greatest Common Divisitor**
* **Get Remainder**
* **Fraction Tools**
    * **Proper Funciton**
    * **Get Numerator / Denominator**
* **Factorial**
* **Permutations**
* **Combinations**
* **History**

## Installation

Follow the steps to set up and run **Pycalc**:

* **Clone the repository**
    ```bash
    git clone https://github.com/an0nym9/pycalc
    cd clone
    ```

* **Install dependencies with Poetry**<br/>
    Make sure you have Poetry installed (tested with 2.2.1)
    ```bash
    poetry install
    ```

* **Run Pycalc**
    ```bash
    poetry run pycalc
    ```

* **Running tests with Pytest**<br/>
    Make sure Pytest is installed (tested with 9.0.2):
    ```bash
    poetry run pytest
    ```

## Example

Here is an example of the program calculating the **LCM** of `12`, `6`, `9`, `7`, and `14`.

```txt
+==================================================+
|                      Number                      |
+==================================================+
|                                                  |
|  [1] Check prime                                 |
|  [2] Check semi prime                            |
|  [3] Generate prime sequence                     |
|  [4] Generate semi prime sequence                |
|  [5] Fraction to decimal                         |
|  [6] Decimal to fraction                         |
|  [7] Factor                                      |
|  [8] Least common multiple                       |
|  [9] Greatest common divisitor                   |
|  [10] Get remainder                              |
|  [11] Fraction tools                             |
|  [12] Exit                                       |
|                                                  |
+==================================================+
Enter your option (number): 8
How many number would you like to add? 5
Enter the number: 12
Enter the number: 6
Enter the number: 9
Enter the number: 7
Enter the number: 14
LCM: 252
Press enter to continue...
```

## License

This project is licensed under the [MIT License](LICENSE).
