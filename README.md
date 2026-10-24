# Big Calculator

A Python calculator that goes beyond normal math — from basic
arithmetic all the way up to hexation, with a custom notation
system for astronomically large numbers.

## Features

- Addition, subtraction, multiplication, and division
- Supports positive and negative numbers
- Exponentiation with large-number formatting
- Tetration, pentation, and hexation
- Fibonacci sequence generation
- Arithmetic, geometric, square, cube, and custom sequences
- Random integer generation
- Colorful command-line interface
- Input validation and helpful error messages
- Protection against division by zero
- Special formatting for very large numbers

## Latest Update

The system now supports negative numbers in basic arithmetic operations, making the calculator more flexible for real mathematical calculations.

Examples:

- `-8 + 3 = -5`
- `-6 × -4 = 24`
- `10 - 17 = -7`
- `-20 ÷ 5 = -4`


## Known limitations
- Pentation and hexation use log-space approximation.
- Extreme inputs correctly return "beyond computable range" — the result is finite, but too large for any computer to store.
- Hyperoperations support positive numbers only, as negative inputs are not well-defined mathematically.
- Very small results may be displayed in scientific notation. Extremely tiny floating-point results may become 0.0 because of Python float limitations.

> Note: Hyperoperations require a positive base because negative bases are not supported by this implementation.

## How to run
python calculator.py

## Built with
Python 3 — standard library only (math, time, os)
