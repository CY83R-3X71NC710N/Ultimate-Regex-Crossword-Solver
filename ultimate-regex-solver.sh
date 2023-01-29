#!/bin/bash
# Presented on replit
# Define options
options=(
    "MIT Mystery Hunt Challenge Solver (Rated the hardest Regex Crossword Challenge to solve in the world"
    "Download Directory Of Solutions All Levels (cat the file) (use this if you don't have much time or don't know programming)"
    "Download custom regex solver that can be modified by editing the source code to solve a challenge with backlinks (use this if you have a lot of time and know programming to create your own custom regex solver)"
    "Quit"
)

# Display options
PS3='Please choose an option: '
select opt in "${options[@]}"; do
    case $opt in
        "Option 1")
            echo "You selected Solve MIT Mystery Hunt Regex Challenge"
            # Solves the 2013 MIT Mystery Hunt, by Dan Gulotta, Palmer Mebane Regex Crossword https://regexcrossword.com/playerpuzzles/8cbea27f-c4c5-4d11-a509-6a622ba01107
            git clone https://github.com/dneiter/regex-crossword.git
            cd regex-crossword
            python2 main.py
            break
            ;;
        "Option 2")
            echo "You selected to download the largest directory of solutions for the regex crossword challenges (cat the solution)"
            git clone https://github.com/deepaksood619/RegexCrossword.git
            break
            ;;
        "Option 3")
            echo "You opted to download a custom regex solver that can solve pretty much any challenge if you modify the source code to do so"
            git clone https://github.com/blukat29/regex-crossword-solver.git
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
