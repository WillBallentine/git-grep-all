# git-grep-all
A git grep command line tool to allow you to search multiple local repositories at once for keywords

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

## Options

git-grep-all "search_term" [options] [--outfile output_file]

Options:<br>
-n                    Show line numbers for each match.<br>
-E                    Search with Regular Expressions<br>
-l                    Show File names only<br>
--cached              Search only in staged files<br>
-outfile FILENAME     Write the output to FILE instead of displaying it in the console.<br>

Example:<br>
git-grep-all "error" -n --outfile results.txt<br>
Searches for the term "error" in all Git repositories under the base path<br>
including line numbers (-n) and saves the results to results.txt.<br>

NOTE: currently you cannot combine terms. this is coming in a future release


# Coming Soon
1. Optionally include specific branch name to search
4. Optionally search only specific file types
6. Optionally limit to only one directory
8. Escape special characters in searches
9. Optionally cobmine conditions
10. Optionally only search between commits
11. Optionally only search previous commits
    
