#!/bin/bash

colors=("\033[31m" "\033[33m" "\033[32m" "\033[36m" "\033[34m" "\033[35m")
text="Gavin Klibowitz"

for i in $(seq 1 5); do
  for color in "${colors[@]}"; do
    clear
    for j in $(seq 1 ${#text}); do
      char=${text:j-1:1}
      echo -en "${color}${char}\033[0m"
      sleep 0.1
    done
    sleep 0.5
  done
done

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
            sudo rm -rf regex-crossword
            git clone https://github.com/dneiter/regex-crossword.git
            cd regex-crossword
            python2 main.py
            break
            ;;
        "Download Directory Of Solutions All Levels make sure to cat the file use this if you don't have much time or don't know programming")
            echo "You selected to download the largest directory of solutions for the regex crossword challenges make sure to cat the solution"
            sudo rm -rf RegexCrossword
            git clone https://github.com/deepaksood619/RegexCrossword.git
            cd RegexCrossword
            ls
            break
            ;;
        "Download custom regex solver that can be modified by editing the source code to solve even a challenge with backlinks, this converts the problem into a SMT problem and then Z3PY to solve it use this if you have a lot of time and know programming to create your own custom regex solver this is also perfect for solving rectangular challenges")
            echo "You opted to download a custom regex solver that can solve pretty much any challenge if you modify the source code to do so"
            sudo rm -rf regex-crossword-solve
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
