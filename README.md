# git-grep-all
A git grep command line tool to allow you to search multiple repositories at once for keywords

# Setup
Clone this repo to a location that has been added to your PATH already OR clone and add the new location to your path (this is currently configured for Windows only).
NOTE: only the git-grep-all.py file needs to be added to the path.

# Usage
Currently this is setup to work with repos in subdirectories under one main directory.
You need to update the BASE variable to be the path to your main directory of your repos.

- Base directory
  - repo 1
  - repo 2
  - repo 3
  - etc
 
In your command line, type "git-grep-all <search term>" and hit enter. This is the base use of this tool and will print all results in your prompt window.

You can also write all results to a file with the --outfile flag: "git-grep-all <search term> --outfile <fileName>"
