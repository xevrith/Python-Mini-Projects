# Python Mini Projects

A collection of beginner-friendly Python programs that turn programming fundamentals into practical, interactive exercises. Projects cover problem-solving, conditions, loops, functions, collections, input validation, and simple business workflows.

These are educational projects, not production-ready applications.

## Projects Included

| Project | File | What it does | Main concepts |
|---|---|---|---|
| 1. Guess the Number | `Project 1/guess_the_number.py` | Number guessing game with limited attempts | Input, conditions, loops |
| 2. ATM Simulator | `Project 2/atm_simulator.py` | Basic balance, deposit, and withdrawal simulation | Conditions, loops, numeric input |
| 3. Student Grade Calculator | `Project 3/student_grade_calculator.py` | Calculates student results | Arithmetic, conditions |
| 4. Password Strength Checker | `Project 4/password_strength_checker.py` | Checks basic password composition rules | Strings, loops, validation |
| 5. Calculator | `Project 5/calculator.py` | Repeated calculations with common operators | Functions, conditions, exceptions |
| 6. Mini Banking System | `Project 6/mini_banking.py` | Login, balance, deposits, and withdrawals | Functions, validation, menu loops |
| 7. Expense Tracker | `Project 7/expense_tracker.py` | Adds, views, edits, removes, and summarizes expenses | Lists, dictionaries, functions |
| 8. Hospital Management | `Project 8/hospital.py` | Manages in-memory patient records | Dictionaries, CRUD operations, validation |
| 9. Car Dealership | `Project 9/car_dealership.py` | Displays and searches vehicle inventory | Nested lists, loops, functions |
| 10. Password Generator | `Project 10/password_generator.py` | Generates a sample password | Random selection, strings |
| 11. Cafe Management | `Project 11/cafe.py` | Adds, deletes, displays, and updates menu items | Dictionaries, functions, validation |
| 12. Burger King Invoice | `Project 12/invoice.py` | Builds a cart and calculates an invoice with CGST and SGST | Dictionaries, functions, calculations |
| 13. Guess the Number | `Project 13/guess_the_number.py` | Randomized number guessing game | Random module, loops, conditions |

## Getting Started

### Requirements
- Python 3
- VS Code or another code editor
- A terminal

The projects use Python's standard library and do not normally require third-party packages.

### Run a project

Clone or download the repository, open its folder in a terminal, and run one project at a time. For example:

```bash
python "Project 12/invoice.py"
```

On some systems, use `python3` instead of `python`.

## Learning Goals

- Practice Python fundamentals through complete programs.
- Improve logical thinking and break tasks into smaller steps.
- Use functions to organize repeated operations.
- Validate user input and handle common errors.
- Work with lists and dictionaries in practical scenarios.
- Test normal, boundary, and invalid inputs.

## Project Notes and Limitations

- **Educational use:** These projects are for learning and experimentation.
- **Banking system:** This is a local simulation with a temporary in-memory balance. It is not connected to a real bank and is not secure banking software. Set the `BANKING_PASSWORD` environment variable before running it.
- **Hospital management:** Patient records are stored in memory and are lost when the program exits. Use fictional sample data only.
- **Password checker/generator:** These are learning demonstrations, not a substitute for professional password security tools.
- **Expense tracker and invoice generator:** Data is held in memory; the programs do not save transactions to a database or file.
- **Tax calculation:** The invoice exercise uses a fixed 2.5% CGST and 2.5% SGST demonstration rate. It is not tax advice.

## Repository Structure

```text
Python-Mini-Projects/
├── Project 1/   # Guess the Number
├── Project 2/   # ATM Simulator
├── Project 3/   # Student Grade Calculator
├── Project 4/   # Password Strength Checker
├── Project 5/   # Calculator
├── Project 6/   # Mini Banking System
├── Project 7/   # Expense Tracker
├── Project 8/   # Hospital Management
├── Project 9/   # Car Dealership
├── Project 10/  # Password Generator
├── Project 11/  # Cafe Management
├── Project 12/  # Burger King Invoice
└── Project 13/  # Guess the Number
```

## Related Repository

For topic-by-topic exercises and Python fundamentals, see [Python-Basics](https://github.com/xevrith/Python-Basics).

## Author

Maintained by [@xevrith](https://github.com/xevrith).
