# L-System Explorer

An exploration of Lindenmayer systems - where grammar becomes geometry.

## What Are L-Systems?

L-Systems (Lindenmayer systems) are a formal grammar system invented by botanist Aristid Lindenmayer in 1968 to model plant growth. They use **string rewriting rules** that transform symbols through iteration, creating complex structures from simple beginnings.

The magic: **discrete symbolic manipulation produces continuous geometric form.**

## How They Work

Start with an **axiom** (initial string) and **production rules**:

```
Axiom: F
Rule:  F → F+F-F-F+F
Angle: 90°
```

Each iteration applies the rules to every symbol:

```
Generation 0: F
Generation 1: F+F-F-F+F
Generation 2: F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F
...
```

Then interpret the string as **turtle graphics commands**:
- `F` = move forward and draw
- `+` = turn right
- `-` = turn left
- `[` = save position (push to stack)
- `]` = restore position (pop from stack)

The result: intricate fractal patterns that model natural forms.

## Why This Fascinates Me

### 1. **Emergence Through Iteration**

Simple rules, applied repeatedly, create astonishing complexity. Just like cellular automata, but here the transformation is symbolic rather than spatial.

### 2. **Grammar Becomes Geometry**

L-Systems bridge two seemingly different worlds:
- **Formal language theory** (symbolic rewriting, grammars, strings)
- **Visual/geometric form** (curves, fractals, shapes)

This connection between discrete and continuous is profound.

### 3. **Modeling Natural Growth**

Plants don't grow by having a blueprint of their final form. They grow by applying simple local rules repeatedly. L-Systems capture this process:

```
X → F+[[X]-X]-F[-FX]+X
F → FF
```

This creates branching plant structures that look organic because they *are* grown algorithmically, just like real plants.

### 4. **Self-Similarity and Scale**

Many L-Systems are **fractals** - they exhibit the same patterns at different scales. The Koch curve, Sierpiński triangle, and Dragon curve all have this property. You can zoom in forever and still find structure.

### 5. **Determinism vs. Variation**

Deterministic L-Systems always produce the same output. But **stochastic L-Systems** use probabilistic rules:

```
F → F[+F]F[-F]F     (probability 0.7)
F → F[+F]F          (probability 0.3)
```

This creates variation within constraint - like how every tree is unique but recognizably a tree.

## The Seven Systems

### Koch Curve
```bash
python lsystem.py koch --iterations 4
```

One of the earliest fractals. Each straight line becomes four smaller lines in a specific pattern. Infinite detail at every scale. The coastline paradox embodied.

**F → F+F-F-F+F** (angle: 90°)

### Sierpiński Triangle
```bash
python lsystem.py sierpinski --iterations 5
```

A triangle of triangles of triangles. Self-similar, recursive, fractal. Area approaches zero, perimeter approaches infinity.

**F → F-G+F+G-F** and **G → GG** (angle: 120°)

### Dragon Curve
```bash
python lsystem.py dragon --iterations 10
```

Fold a strip of paper in half repeatedly, then unfold at 90° angles. This is what you get. Named because of its dragon-like appearance. Beautiful symmetry emerges from simple folding.

**F → F+G** and **G → F-G** (angle: 90°)

### Branching Plant
```bash
python lsystem.py plant --iterations 5
```

Models how plants branch. Uses `[` and `]` to push/pop turtle state, allowing branches to split and return. Each iteration adds more detail - more branches, more leaves.

**X → F+[[X]-X]-F[-FX]+X** and **F → FF** (angle: 25°)

### Binary Tree
```bash
python lsystem.py tree --iterations 4
```

The archetypal branching structure. Each branch splits into two. Simple, recursive, fundamental.

**F → F[+F]F[-F]F** (angle: 30°)

### Lévy C Curve
```bash
python lsystem.py levy --iterations 10
```

Named after mathematician Paul Lévy. Each line segment becomes two segments at 45° angles. Tiles the plane in interesting ways. Less famous than Koch but equally beautiful.

**F → +F--F+** (angle: 45°)

### Hilbert Curve
```bash
python lsystem.py hilbert --iterations 5
```

A **space-filling curve** - it eventually passes through every point in a square. Used in computer science for spatial data structures. Shows how one-dimensional can map to two-dimensional.

**A → -BF+AFA+FB-** and **B → +AF-BFB-FA+** (angle: 90°)

## Usage

List all available systems:
```bash
python lsystem.py --list
```

Generate a specific system:
```bash
python lsystem.py <name> --iterations <n> --output <file.svg>
```

Options:
- `--iterations, -n`: Number of times to apply rules (default: 4)
- `--output, -o`: Output SVG filename
- `--size`: Output image size in pixels (default: 800)
- `--step`: Turtle step length (default: 10)

## Examples

Simple Koch curve:
```bash
python lsystem.py koch -n 3
```

Detailed dragon curve:
```bash
python lsystem.py dragon -n 12 --size 1200
```

Organic plant:
```bash
python lsystem.py plant -n 6 --step 8
```

## Experiments to Try

1. **Increase iterations** - Watch complexity emerge. How high can you go before the system becomes too complex to render?

2. **Modify angles** - Edit the code to change angles. Small changes create wildly different forms.

3. **Create new systems** - Define your own axiom and rules. What patterns can you discover?

4. **Add stochastic rules** - Make the rewriting probabilistic for variation.

5. **3D L-Systems** - Extend to three dimensions with pitch and roll commands.

6. **Animated growth** - Render each generation separately to create an animation of growth.

## The Deeper Pattern

L-Systems, cellular automata, fractals, natural growth, formal grammars - they all share something:

**Complex behavior emerges from simple rules applied iteratively.**

You can't predict the final form by looking at the rules. You have to run the system. Execute the iterations. Let the patterns unfold.

This is **computational irreducibility** - the only way to know what happens is to actually compute it.

It's also how nature works. No central blueprint. Just local rules, applied everywhere, creating the emergent complexity we call life.

## Further Reading

- **The Algorithmic Beauty of Plants** by Prusinkiewicz & Lindenmayer - The definitive book
- **Fractals Everywhere** by Michael Barnsley - Mathematical foundations
- **The Computational Beauty of Nature** by Gary William Flake - Broader context
- Wikipedia's L-System article - Excellent reference

---

*Grammar becomes geometry. Symbols become forms. Iteration reveals beauty.*
