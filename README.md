# Big Calculator

A Python calculator that goes beyond normal math — from basic
arithmetic all the way up to hexation, with a custom notation
system for astronomically large numbers.

## Features
- Addition, subtraction, multiplication, division
- Exponentiation, tetration, pentation, hexation
- Fibonacci sequence generator
- Custom big-number notation (log-layer stacking: e, f, g, h...)
- Graceful handling of values beyond computable range
- After 1e1,000,000,000,000: goes until 1f, after 1f1,000,000,000,000: goes to 1g (etc..)
## Known limitations
- Pentation and hexation use log-space approximation.
- Extreme inputs correctly return "beyond computable range" — the result is finite, but too large for any computer to store.
- Hyperoperations support positive numbers only, as negative
  inputs are not well-defined mathematically.

## How to run
python calculator.py

## Built with
Python 3 — standard library only (math, time, os)
