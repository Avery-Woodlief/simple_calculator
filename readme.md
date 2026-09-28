# Simple Arithmetic Calculator

A simple graphical arithmetic calculator built with Python and Tkinter.

The calculator provides a basic user interface for entering and evaluating mathematical expressions.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Modulo
- Percentages
- Square
- Square root
- Parentheses
- Decimal numbers
- Pi (π)
- Clear button
- Expression display
- Basic error handling

## Built With

- Python
- Tkinter
- `math`
- JSON for color configuration

## Calculator Layout

```text
⌫    (    )    mod    π
7    8    9     ÷     √
4    5    6     ×     x²
1    2    3     -     =
0    .    %     +     =
```

## Running the Calculator

Clone or download the project and navigate to its directory.

Run:

```bash
python3 main.py
```

## Requirements

The calculator uses Python's standard library and does not require any third-party Python packages.

Tkinter must be installed on the system. On Ubuntu/Debian systems, it can be installed with:

```bash
sudo apt install python3-tk
```

## Project Structure

```text
simple_calculator/
├── main.py
├── README.md
└── colors.json
```

## Usage

Click the calculator buttons to construct a mathematical expression. The current expression is displayed at the top of the window.

Press `=` to evaluate the expression and display the result.

Use `⌫`/clear to clear the current expression.

## Purpose

This project demonstrates the fundamentals of building a desktop GUI application with Tkinter, including widget layouts, button commands, `StringVar`, event handling, and dynamic expression evaluation.