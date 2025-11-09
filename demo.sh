#!/bin/bash
# Cellular Automaton Demo
# A curated tour through interesting patterns and behaviors

echo "═══════════════════════════════════════════════════════════"
echo "    Cellular Automaton Explorer - Demo Tour"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "This demo will show you some of the most interesting patterns"
echo "in cellular automata. Press Ctrl+C at any time to stop."
echo ""
read -p "Press Enter to begin..."

echo ""
echo "═══ 1. Rule 30: Chaos from Order ═══"
echo "Watch as a single cell creates seemingly random patterns..."
echo ""
sleep 2
python3 cellular_automata.py --type elementary --rule 30 --steps 35 --delay 0.08

echo ""
echo "That was Rule 30 - completely deterministic, yet unpredictable!"
echo ""
read -p "Press Enter to continue..."

echo ""
echo "═══ 2. Rule 90: Fractals ═══"
echo "The Sierpiński triangle emerges..."
echo ""
sleep 2
python3 cellular_automata.py --type elementary --rule 90 --steps 35 --delay 0.08

echo ""
echo "Rule 90 creates fractals - self-similar patterns at every scale!"
echo ""
read -p "Press Enter to continue..."

echo ""
echo "═══ 3. Rule 110: Universal Computation ═══"
echo "This rule is Turing complete - it can compute anything!"
echo ""
sleep 2
python3 cellular_automata.py --type elementary --rule 110 --steps 35 --delay 0.08

echo ""
echo "Notice the complex, structured patterns with local interactions."
echo ""
read -p "Press Enter to continue to Game of Life..."

echo ""
echo "═══ 4. The Glider - Life's Spaceship ═══"
echo "A pattern that flies across the universe..."
echo ""
sleep 2
python3 cellular_automata.py --type life --pattern glider --steps 60 --delay 0.08 --width 50 --height 25

echo ""
echo "═══ 5. The Acorn - Small but Long-Lived ═══"
echo "Just 7 cells that will evolve for over 5,000 generations!"
echo "(We'll only show 100...)"
echo ""
sleep 2
python3 cellular_automata.py --type life --pattern acorn --steps 100 --delay 0.03 --width 60 --height 30

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "                    Demo Complete!"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "To explore more:"
echo "  - Run 'python3 cellular_automata.py --type explore' for interesting rules"
echo "  - Try random Game of Life: 'python3 cellular_automata.py --type life'"
echo "  - Read PATTERNS.md for more details"
echo ""
echo "Remember: All this complexity emerges from simple rules!"
echo ""
