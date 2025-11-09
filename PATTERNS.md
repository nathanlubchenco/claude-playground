# Pattern Gallery

A collection of fascinating patterns and behaviors in cellular automata.

## Elementary Cellular Automata (1D)

Elementary CA are the simplest possible cellular automata - each cell looks at itself and its two neighbors to determine its next state. Despite this simplicity, they exhibit remarkably diverse behaviors.

### Rule 30 - Chaos
```bash
python cellular_automata.py --type elementary --rule 30 --steps 40
```
**Behavior**: Chaotic and unpredictable. Mathematica uses Rule 30 to generate random numbers!

**Why it's interesting**: A completely deterministic rule that produces seemingly random output. This demonstrates how chaos can emerge from simple, predictable rules.

### Rule 90 - Fractals
```bash
python cellular_automata.py --type elementary --rule 90 --steps 40
```
**Behavior**: Creates a perfect Sierpiński triangle fractal pattern.

**Why it's interesting**: Self-similar patterns at every scale. The same structure repeats infinitely whether you zoom in or out.

### Rule 110 - Computation
```bash
python cellular_automata.py --type elementary --rule 110 --steps 40
```
**Behavior**: Complex, structured patterns with localized structures that interact.

**Why it's interesting**: Proven to be Turing complete - capable of universal computation! This simple rule can theoretically compute anything a computer can.

### Rule 184 - Traffic Flow
```bash
python cellular_automata.py --type elementary --rule 184 --steps 40
```
**Behavior**: Models traffic flow and particle movement.

**Why it's interesting**: Used in real traffic flow simulations. Shows how CA can model physical phenomena.

### Other Notable Rules
- **Rule 54**: Creates beautiful regular patterns
- **Rule 126**: Complex but organized
- **Rule 225**: Creates diagonal patterns
- **Rule 250**: Interesting local interactions

## Conway's Game of Life (2D)

The Game of Life is perhaps the most famous cellular automaton. Its rules are simple but create an astonishing variety of behaviors.

### Glider - The Spaceship
```bash
python cellular_automata.py --type life --pattern glider --steps 100
```
**Behavior**: A small pattern that moves diagonally across the grid forever.

**Why it's interesting**: It's a "spaceship" - a pattern that translates itself across space. The glider is the smallest possible spaceship.

### Blinker - The Oscillator
```bash
python cellular_automata.py --type life --pattern blinker --steps 20
```
**Behavior**: Alternates between horizontal and vertical configurations.

**Why it's interesting**: The simplest oscillator with period 2. Demonstrates stable periodic behavior.

### Acorn - Methuselah
```bash
python cellular_automata.py --type life --pattern acorn --steps 300 --delay 0.05
```
**Behavior**: A tiny 7-cell pattern that takes 5,206 generations to stabilize!

**Why it's interesting**: Shows how tiny initial conditions can have incredibly long-lasting effects. A "Methuselah" pattern.

### Random Soup
```bash
python cellular_automata.py --type life --steps 200 --delay 0.05
```
**Behavior**: Random initial state that evolves unpredictably.

**Why it's interesting**: Watch as order emerges from chaos. Stable patterns, oscillators, and gliders often spontaneously appear.

## Philosophy

What makes cellular automata fascinating?

1. **Emergence**: Complex behavior emerges from simple rules. No cell "knows" about the global patterns it's creating.

2. **Determinism vs Unpredictability**: Even though the rules are completely deterministic, the behavior can be effectively unpredictable (Rule 30, random soups).

3. **Computation**: Some CA (like Rule 110) are universal computers, meaning they can compute anything computable.

4. **Life-like Behavior**: Patterns that seem to "live" - they move, reproduce, interact, and die. Hence "Game of Life."

5. **Edge of Chaos**: The most interesting rules exist at the boundary between order and chaos - not too regular, not too random.

## Experiments to Try

1. **Find New Patterns**: Run random Game of Life configurations and look for interesting emergent structures.

2. **Rule Exploration**: Try random elementary CA rules (0-255) to discover new behaviors.

3. **Pattern Collisions**: What happens when two gliders collide? (Spoiler: They can annihilate, create new patterns, or pass through each other!)

4. **Long-term Evolution**: Run for thousands of generations. Do patterns stabilize, oscillate, or continue changing forever?

## Further Reading

- Stephen Wolfram's "A New Kind of Science" - Comprehensive exploration of CA
- "The Recursive Universe" by William Poundstone - Accessible introduction to Life
- "Cellular Automata Machines" by Tommaso Toffoli - Technical deep dive
