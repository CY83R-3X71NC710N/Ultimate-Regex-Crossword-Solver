#!/bin/bash

import time
import sys

def rainbow_text(text):
    rainbow = ["\033[31m", "\033[33m", "\033[32m", "\033[36m", "\033[34m", "\033[35m"]
    for color in rainbow:
        sys.stdout.write(f"{color}{text}\033[0m\r")
        sys.stdout.flush()
        time.sleep(0.1)

start_time = time.time()
while time.time() - start_time < 5:
    rainbow_text("Gavin Klibowitz")

options=(
    "MIT Mystery Hunt Challenge Solver rated the hardest Regex Crossword Challenge to solve in the world"
    "Download Directory Of Solutions All Levels make sure to cat the file use this if you don't have much time or don't know programming"
    "Download custom regex solver that can be modified by editing the source code to solve even a challenge with backlinks, this converts the problem into a SMT problem and then Z3PY to solve it use this if you have a lot of time and know programming to create your own custom regex solver this is also perfect for solving rectangular challenges"
    "Quit"
)

PS3='Please choose an option: '
select opt in "${options[@]}"; do
    case $opt in
        "MIT Mystery Hunt Challenge Solver rated the hardest Regex Crossword Challenge to solve in the world")
            echo "You selected Solve MIT Mystery Hunt Regex Challenge"
            git clone https://github.com/dneiter/regex-crossword.git
            cd regex-crossword
            python2 main.py
            break
            ;;
        "Download Directory Of Solutions All Levels make sure to cat the file use this if you don't have much time or don't know programming")
            echo "You selected to download the largest directory of solutions for the regex crossword challenges make sure to cat the solution"
            git clone https://github.com/deepaksood619/RegexCrossword.git
            cd RegexCrossword
            ls
            break
            ;;
        "Download custom regex solver that can be modified by editing the source code to solve even a challenge with backlinks, this converts the problem into a SMT problem and then Z3PY to solve it use this if you have a lot of time and know programming to create your own custom regex solver this is also perfect for solving rectangular challenges")
            echo "You opted to download a custom regex solver that can solve pretty much any challenge if you modify the source code to do so"
            git clone https://github.com/blukat29/regex-crossword-solver.git
            cd regex-crossword-solver
            ls
            break
            ;;
        "Quit")
            echo "Goodbye!"
            break
            ;;
        *)
            echo "Invalid option, try again"
            ;;
    esac
done
