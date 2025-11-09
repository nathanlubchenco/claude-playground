#!/usr/bin/env python3
"""
Cellular Automaton Explorer

An exploration of emergent complexity from simple computational rules.
"""

import argparse
import time
import random
from typing import List, Callable, Optional
from dataclasses import dataclass


class ElementaryCA:
    """
    Elementary Cellular Automaton (1D)

    Implements Wolfram's 256 elementary CA rules. Each cell's next state
    depends on its current state and its two neighbors, creating surprisingly
    complex behaviors from simple rules.
    """

    def __init__(self, width: int, rule: int):
        self.width = width
        self.rule = rule
        self.state = [0] * width
        # Start with a single cell in the middle
        self.state[width // 2] = 1

    def get_rule_mapping(self) -> dict:
        """Convert rule number to binary lookup table"""
        rule_binary = format(self.rule, '08b')
        mapping = {}
        for i in range(8):
            pattern = format(7 - i, '03b')
            mapping[pattern] = int(rule_binary[i])
        return mapping

    def step(self):
        """Compute next generation"""
        rule_map = self.get_rule_mapping()
        new_state = [0] * self.width

        for i in range(self.width):
            left = self.state[(i - 1) % self.width]
            center = self.state[i]
            right = self.state[(i + 1) % self.width]

            pattern = f"{left}{center}{right}"
            new_state[i] = rule_map[pattern]

        self.state = new_state

    def to_string(self, alive_char='█', dead_char=' ') -> str:
        """Convert current state to string"""
        return ''.join(alive_char if cell else dead_char for cell in self.state)


class GameOfLife:
    """
    Conway's Game of Life (2D)

    The classic cellular automaton. Rules:
    1. Any live cell with 2-3 neighbors survives
    2. Any dead cell with exactly 3 neighbors becomes alive
    3. All other cells die or stay dead

    These simple rules create an incredibly rich universe of patterns.
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def set_cell(self, x: int, y: int, value: int):
        """Set a cell's state"""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = value

    def count_neighbors(self, x: int, y: int) -> int:
        """Count living neighbors around a cell"""
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = (x + dx) % self.width
                ny = (y + dy) % self.height
                count += self.grid[ny][nx]
        return count

    def step(self):
        """Compute next generation"""
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                current = self.grid[y][x]

                if current == 1:  # Alive
                    if neighbors in [2, 3]:
                        new_grid[y][x] = 1
                else:  # Dead
                    if neighbors == 3:
                        new_grid[y][x] = 1

        self.grid = new_grid

    def to_string(self, alive_char='█', dead_char=' ') -> str:
        """Convert current state to string"""
        lines = []
        for row in self.grid:
            lines.append(''.join(alive_char if cell else dead_char for cell in row))
        return '\n'.join(lines)

    def randomize(self, density: float = 0.3):
        """Fill grid with random cells"""
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = 1 if random.random() < density else 0

    def load_pattern(self, pattern: str):
        """Load a named pattern"""
        patterns = {
            'glider': [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)],
            'blinker': [(1, 0), (1, 1), (1, 2)],
            'toad': [(1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2)],
            'beacon': [(0, 0), (1, 0), (0, 1), (3, 2), (2, 3), (3, 3)],
            'pulsar': [
                # Ring pattern - simplified pulsar
                (2, 0), (3, 0), (4, 0), (8, 0), (9, 0), (10, 0),
                (0, 2), (5, 2), (7, 2), (12, 2),
                (0, 3), (5, 3), (7, 3), (12, 3),
                (0, 4), (5, 4), (7, 4), (12, 4),
                (2, 5), (3, 5), (4, 5), (8, 5), (9, 5), (10, 5),
            ],
            'acorn': [(1, 0), (3, 1), (0, 2), (1, 2), (4, 2), (5, 2), (6, 2)],
        }

        if pattern in patterns:
            # Center the pattern
            coords = patterns[pattern]
            offset_x = self.width // 2 - 5
            offset_y = self.height // 2 - 5

            for x, y in coords:
                self.set_cell(x + offset_x, y + offset_y, 1)


def clear_screen():
    """Clear terminal screen"""
    print('\033[2J\033[H', end='')


def run_elementary(rule: int, steps: int = 50, width: int = 79, delay: float = 0.1):
    """Run elementary CA simulation"""
    ca = ElementaryCA(width, rule)

    print(f"\n═══ Elementary Cellular Automaton - Rule {rule} ═══\n")

    for i in range(steps):
        print(ca.to_string())
        ca.step()
        time.sleep(delay)

    print(f"\n{steps} generations of Rule {rule}")


def run_life(pattern: Optional[str] = None, steps: int = 100,
             width: int = 60, height: int = 30, delay: float = 0.1):
    """Run Game of Life simulation"""
    life = GameOfLife(width, height)

    if pattern:
        life.load_pattern(pattern)
        title = f"Conway's Game of Life - {pattern.capitalize()}"
    else:
        life.randomize(density=0.3)
        title = "Conway's Game of Life - Random"

    print(f"\n═══ {title} ═══\n")
    print("Rules: Survival [2,3] / Birth [3]\n")

    for i in range(steps):
        clear_screen()
        print(f"═══ {title} ═══")
        print(f"Generation: {i}\n")
        print(life.to_string())
        life.step()
        time.sleep(delay)


def explore_rules():
    """Explore interesting elementary CA rules"""
    interesting_rules = {
        30: "Chaotic - used in random number generation",
        90: "Fractal - creates Sierpiński triangle",
        110: "Turing complete - complex behavior",
        184: "Traffic flow simulation",
    }

    print("\n═══ Interesting Elementary CA Rules ═══\n")
    for rule, description in interesting_rules.items():
        print(f"Rule {rule:3d}: {description}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Cellular Automaton Explorer - Emergent complexity from simple rules"
    )
    parser.add_argument(
        '--type',
        choices=['elementary', 'life', 'explore'],
        default='life',
        help='Type of cellular automaton'
    )
    parser.add_argument(
        '--rule',
        type=int,
        default=110,
        help='Rule number for elementary CA (0-255)'
    )
    parser.add_argument(
        '--pattern',
        type=str,
        help='Named pattern for Game of Life (glider, blinker, toad, beacon, pulsar, acorn)'
    )
    parser.add_argument(
        '--steps',
        type=int,
        default=100,
        help='Number of generations to simulate'
    )
    parser.add_argument(
        '--width',
        type=int,
        default=79,
        help='Width of the grid'
    )
    parser.add_argument(
        '--height',
        type=int,
        default=30,
        help='Height of the grid (for 2D CA)'
    )
    parser.add_argument(
        '--delay',
        type=float,
        default=0.1,
        help='Delay between generations (seconds)'
    )

    args = parser.parse_args()

    if args.type == 'explore':
        explore_rules()
    elif args.type == 'elementary':
        run_elementary(args.rule, args.steps, args.width, args.delay)
    elif args.type == 'life':
        run_life(args.pattern, args.steps, args.width, args.height, args.delay)


if __name__ == '__main__':
    main()
