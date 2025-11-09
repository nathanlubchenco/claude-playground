# Emergence Explorer

A personal playground exploring how simple rules create complex patterns through iteration.

## Projects

### 1. Cellular Automaton Explorer
**[cellular_automata.py](./cellular_automata.py)** | **[Documentation](./PATTERNS.md)**

Exploration of cellular automata - simple computational rules that create complex emergent behaviors.

- **Elementary Cellular Automata**: 1D automata following Wolfram's 256 rules
- **Conway's Game of Life**: The classic 2D automaton
- **Notable patterns**: Rule 110 (Turing complete), Rule 30 (chaos), gliders, oscillators

### 2. L-System Explorer
**[lsystem.py](./lsystem.py)** | **[Documentation](./LSYSTEMS.md)**

Exploration of Lindenmayer systems - where grammar becomes geometry.

- **Classic fractals**: Koch curve, Sierpiński triangle, Dragon curve
- **Organic structures**: Branching plants, binary trees
- **Space-filling curves**: Hilbert curve
- **SVG rendering**: High-quality vector output

## The Pattern

Both projects explore the same fundamental principle:

**Complex behavior emerges from simple rules applied iteratively.**

Cellular automata show this in spatial evolution. L-Systems show it in symbolic transformation. Different mechanisms, same profound pattern.

## Quick Start

**Cellular Automata:**
```bash
# Conway's Game of Life with a glider
python cellular_automata.py --type life --pattern glider

# Turing-complete Rule 110
python cellular_automata.py --type elementary --rule 110

# Explore interesting rules
python cellular_automata.py --type explore
```

**L-Systems:**
```bash
# Generate a Koch snowflake
python lsystem.py koch --iterations 4

# Grow a branching plant
python lsystem.py plant --iterations 5

# Create a dragon curve
python lsystem.py dragon --iterations 10

# List all available systems
python lsystem.py --list
```

## Why This Matters

These aren't just pretty patterns. They represent something profound:

**Computational irreducibility** - You can't predict the outcome by looking at the rules. You have to run the system.

**Emergence** - Complex global behavior from simple local rules. No blueprint, no central control.

**Nature's algorithm** - How plants grow, how patterns form, how complexity arises from simplicity.

---

*A personal exploration of emergent complexity*
