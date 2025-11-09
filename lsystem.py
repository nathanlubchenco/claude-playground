#!/usr/bin/env python3
"""
L-System Explorer

An exploration of Lindenmayer systems - how simple string rewriting rules
create intricate geometric forms and model natural growth.

L-Systems bridge the discrete (symbolic manipulation) and continuous (geometric form).
They show how iteration transforms meaning, how grammar becomes geometry.
"""

import argparse
import math
import random
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional, Callable


@dataclass
class Rule:
    """A rewriting rule: symbol -> replacement string"""
    symbol: str
    replacement: str
    probability: float = 1.0  # For stochastic L-systems


@dataclass
class LSystem:
    """
    An L-System definition

    Components:
    - axiom: Starting string (the seed)
    - rules: How to rewrite each symbol
    - angle: Rotation angle for turtle graphics
    - iterations: How many times to apply rules
    """
    axiom: str
    rules: List[Rule]
    angle: float
    name: str = "Unnamed"
    description: str = ""

    def evolve(self, iterations: int, stochastic: bool = False) -> str:
        """Apply rewriting rules iteratively"""
        current = self.axiom

        # Build rule lookup
        rule_map = {}
        for rule in self.rules:
            if rule.symbol not in rule_map:
                rule_map[rule.symbol] = []
            rule_map[rule.symbol].append(rule)

        for _ in range(iterations):
            next_string = []

            for symbol in current:
                if symbol in rule_map:
                    # Choose rule (stochastic or deterministic)
                    rules = rule_map[symbol]
                    if stochastic and len(rules) > 1:
                        # Weighted random choice
                        rand = random.random()
                        cumulative = 0.0
                        chosen_rule = rules[0]
                        for rule in rules:
                            cumulative += rule.probability
                            if rand <= cumulative:
                                chosen_rule = rule
                                break
                        next_string.append(chosen_rule.replacement)
                    else:
                        # Use first rule (deterministic)
                        next_string.append(rules[0].replacement)
                else:
                    # No rule for this symbol, keep it
                    next_string.append(symbol)

            current = ''.join(next_string)

        return current


class TurtleState:
    """State of a turtle graphics cursor"""
    def __init__(self, x: float = 0, y: float = 0, angle: float = 0):
        self.x = x
        self.y = y
        self.angle = angle  # In degrees

    def copy(self) -> 'TurtleState':
        return TurtleState(self.x, self.y, self.angle)


class TurtleInterpreter:
    """
    Interprets L-System strings as turtle graphics commands

    Standard commands:
    - F: Move forward and draw
    - f: Move forward without drawing
    - +: Turn right by angle
    - -: Turn left by angle
    - [: Push state onto stack
    - ]: Pop state from stack
    """

    def __init__(self, step_length: float = 10, start_x: float = 0,
                 start_y: float = 0, start_angle: float = 90):
        self.step_length = step_length
        self.state = TurtleState(start_x, start_y, start_angle)
        self.stack: List[TurtleState] = []
        self.lines: List[Tuple[float, float, float, float]] = []

        # Track bounds for auto-scaling
        self.min_x = start_x
        self.max_x = start_x
        self.min_y = start_y
        self.max_y = start_y

    def interpret(self, commands: str, angle: float) -> List[Tuple[float, float, float, float]]:
        """Execute turtle commands and return list of line segments"""
        self.lines = []

        for cmd in commands:
            if cmd == 'F' or cmd == 'G':  # Draw forward (G for some systems)
                self._draw_forward()
            elif cmd == 'f':  # Move forward without drawing
                self._move_forward()
            elif cmd == '+':  # Turn right
                self.state.angle -= angle
            elif cmd == '-':  # Turn left
                self.state.angle += angle
            elif cmd == '[':  # Push state
                self.stack.append(self.state.copy())
            elif cmd == ']':  # Pop state
                if self.stack:
                    self.state = self.stack.pop()

        return self.lines

    def _draw_forward(self):
        """Move forward and draw a line"""
        old_x, old_y = self.state.x, self.state.y

        rad = math.radians(self.state.angle)
        self.state.x += self.step_length * math.cos(rad)
        self.state.y += self.step_length * math.sin(rad)

        self.lines.append((old_x, old_y, self.state.x, self.state.y))

        # Update bounds
        self.min_x = min(self.min_x, self.state.x)
        self.max_x = max(self.max_x, self.state.x)
        self.min_y = min(self.min_y, self.state.y)
        self.max_y = max(self.max_y, self.state.y)

    def _move_forward(self):
        """Move forward without drawing"""
        rad = math.radians(self.state.angle)
        self.state.x += self.step_length * math.cos(rad)
        self.state.y += self.step_length * math.sin(rad)

        # Update bounds
        self.min_x = min(self.min_x, self.state.x)
        self.max_x = max(self.max_x, self.state.x)
        self.min_y = min(self.min_y, self.state.y)
        self.max_y = max(self.max_y, self.state.y)

    def get_bounds(self) -> Tuple[float, float, float, float]:
        """Return bounding box (min_x, min_y, max_x, max_y)"""
        return (self.min_x, self.min_y, self.max_x, self.max_y)


def render_svg(lines: List[Tuple[float, float, float, float]],
               output_file: str,
               width: int = 800,
               height: int = 800,
               stroke_color: str = "#2c3e50",
               stroke_width: float = 1,
               background: str = "#ecf0f1"):
    """Render lines to SVG file"""

    if not lines:
        print("No lines to render!")
        return

    # Calculate bounds
    min_x = min(x1 for x1, _, _, _ in lines + [(x2, 0, 0, 0) for _, _, x2, _ in lines])
    max_x = max(x1 for x1, _, _, _ in lines + [(x2, 0, 0, 0) for _, _, x2, _ in lines])
    min_y = min(y1 for _, y1, _, _ in lines + [(0, y2, 0, 0) for _, _, _, y2 in lines])
    max_y = max(y1 for _, y1, _, _ in lines + [(0, y2, 0, 0) for _, _, _, y2 in lines])

    # Add padding
    padding = 20
    scale_x = (width - 2 * padding) / (max_x - min_x) if max_x > min_x else 1
    scale_y = (height - 2 * padding) / (max_y - min_y) if max_y > min_y else 1
    scale = min(scale_x, scale_y)

    # Transform coordinates
    def transform(x, y):
        tx = (x - min_x) * scale + padding
        ty = (y - min_y) * scale + padding
        return tx, ty

    # Generate SVG
    svg_lines = [
        f'<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
        f'  <rect width="{width}" height="{height}" fill="{background}"/>',
        f'  <g stroke="{stroke_color}" stroke-width="{stroke_width}" fill="none">',
    ]

    for x1, y1, x2, y2 in lines:
        tx1, ty1 = transform(x1, y1)
        tx2, ty2 = transform(x2, y2)
        svg_lines.append(f'    <line x1="{tx1:.2f}" y1="{ty1:.2f}" x2="{tx2:.2f}" y2="{ty2:.2f}"/>')

    svg_lines.append('  </g>')
    svg_lines.append('</svg>')

    with open(output_file, 'w') as f:
        f.write('\n'.join(svg_lines))

    print(f"Rendered to {output_file}")


# ============================================================================
# Classic L-Systems
# ============================================================================

def get_lsystem(name: str) -> Optional[LSystem]:
    """Get a predefined L-System by name"""

    systems = {
        'koch': LSystem(
            name="Koch Curve",
            description="One of the first fractals. A snowflake made of infinite detail.",
            axiom="F",
            rules=[Rule("F", "F+F-F-F+F")],
            angle=90
        ),

        'sierpinski': LSystem(
            name="Sierpiński Triangle",
            description="Self-similar at every scale. Order within order, infinitely.",
            axiom="F-G-G",
            rules=[
                Rule("F", "F-G+F+G-F"),
                Rule("G", "GG")
            ],
            angle=120
        ),

        'dragon': LSystem(
            name="Dragon Curve",
            description="Folds a strip of paper infinitely. Beautiful symmetry emerges.",
            axiom="F",
            rules=[
                Rule("F", "F+G"),
                Rule("G", "F-G")
            ],
            angle=90
        ),

        'plant': LSystem(
            name="Branching Plant",
            description="Models plant growth. Branches split and reach toward light.",
            axiom="X",
            rules=[
                Rule("X", "F+[[X]-X]-F[-FX]+X"),
                Rule("F", "FF")
            ],
            angle=25
        ),

        'tree': LSystem(
            name="Binary Tree",
            description="Simple branching structure. The archetype of recursive growth.",
            axiom="F",
            rules=[
                Rule("F", "F[+F]F[-F]F")
            ],
            angle=30
        ),

        'levy': LSystem(
            name="Lévy C Curve",
            description="Named after Paul Lévy. Tiles the plane in fascinating ways.",
            axiom="F",
            rules=[
                Rule("F", "+F--F+")
            ],
            angle=45
        ),

        'hilbert': LSystem(
            name="Hilbert Curve",
            description="Space-filling curve. Eventually touches every point.",
            axiom="A",
            rules=[
                Rule("A", "-BF+AFA+FB-"),
                Rule("B", "+AF-BFB-FA+")
            ],
            angle=90
        ),
    }

    return systems.get(name.lower())


def list_systems():
    """List all available L-Systems"""
    systems = ['koch', 'sierpinski', 'dragon', 'plant', 'tree', 'levy', 'hilbert']

    print("\n═══ Available L-Systems ═══\n")
    for name in systems:
        sys = get_lsystem(name)
        if sys:
            print(f"  {name:12s} - {sys.description}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="L-System Explorer - Grammar becomes geometry"
    )
    parser.add_argument(
        'system',
        nargs='?',
        help='L-System to generate (koch, sierpinski, dragon, plant, tree, levy, hilbert)'
    )
    parser.add_argument(
        '--iterations', '-n',
        type=int,
        default=4,
        help='Number of iterations (default: 4)'
    )
    parser.add_argument(
        '--output', '-o',
        type=str,
        help='Output SVG file (default: <system>.svg)'
    )
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='List all available L-Systems'
    )
    parser.add_argument(
        '--size',
        type=int,
        default=800,
        help='Output size in pixels (default: 800)'
    )
    parser.add_argument(
        '--step',
        type=float,
        default=10,
        help='Step length for turtle (default: 10)'
    )

    args = parser.parse_args()

    if args.list or not args.system:
        list_systems()
        return

    # Get L-System
    lsys = get_lsystem(args.system)
    if not lsys:
        print(f"Unknown system: {args.system}")
        list_systems()
        return

    print(f"\n═══ {lsys.name} ═══")
    print(f"{lsys.description}\n")
    print(f"Axiom: {lsys.axiom}")
    print(f"Rules:")
    for rule in lsys.rules:
        print(f"  {rule.symbol} → {rule.replacement}")
    print(f"Angle: {lsys.angle}°")
    print(f"Iterations: {args.iterations}\n")

    # Evolve the system
    print("Evolving...")
    result = lsys.evolve(args.iterations)
    print(f"String length: {len(result)} symbols")

    # Interpret as turtle graphics
    print("Interpreting...")
    turtle = TurtleInterpreter(step_length=args.step)
    lines = turtle.interpret(result, lsys.angle)
    print(f"Generated: {len(lines)} line segments")

    # Render to SVG
    output = args.output or f"{args.system}.svg"
    render_svg(lines, output, width=args.size, height=args.size)
    print(f"\n✓ Complete! Open {output} to view.\n")


if __name__ == '__main__':
    main()
