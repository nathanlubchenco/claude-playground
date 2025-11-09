# Cellular Automaton Explorer

A Python-based exploration of cellular automata - simple computational rules that create complex emergent behaviors.

## What is this?

This project implements various types of cellular automata:
- **Elementary Cellular Automata**: 1D automata following Wolfram's 256 rules
- **Conway's Game of Life**: The classic 2D automaton
- **Custom Rules**: Experiment with your own rule sets

## Why?

I'm fascinated by how simple, deterministic rules can create incredibly complex, organic-looking patterns. This is an exploration of emergence, complexity, and the boundary between order and chaos.

## Features

- Terminal-based visualization
- Multiple CA types and rule sets
- Interactive controls
- Pattern saving and loading
- Interesting preset patterns

## Usage

```bash
# Run elementary CA (1D)
python cellular_automata.py --type elementary --rule 110

# Run Game of Life
python cellular_automata.py --type life --pattern glider

# Interactive mode
python cellular_automata.py --interactive
```

## Notable Patterns

- **Rule 110**: Turing complete elementary CA
- **Rule 30**: Chaotic, used in random number generation
- **Game of Life**: Gliders, spaceships, oscillators, and more

---

*A personal exploration of emergent complexity*
