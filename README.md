# DC Power Supply Circuit Simulation

## Project Overview

This project simulates a regulated DC power supply using Python.

The circuit consists of:

230 V AC Supply → Transformer → Bridge Rectifier → Capacitor Filter → 7805 Voltage Regulator → 5 V DC Load

## Components

- AC supply: 230 V, 50 Hz
- Transformer: 230 V / 9 V
- Bridge rectifier
- Filter capacitor: 1000 µF
- 7805 voltage regulator
- Load resistance: 100 Ω

## Software Used

- Python 3
- NumPy
- Matplotlib
- SciPy
- Visual Studio Code
- GitHub

## Simulation Features

The simulation displays:

1. Transformer secondary AC voltage
2. Full-wave bridge rectifier output
3. Capacitor-filtered voltage
4. Final regulated 5 V DC output
5. Load current
6. Load power
7. Ripple voltage

## How to Run

Create and activate the Python virtual environment, then install the required libraries:

```bash
pip install -r requirements.txt