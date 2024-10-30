#!/usr/bin/env python

import subprocess
import os
import sys

class GitGrep:
    def __init__(self, base_path, search_term, output_file=None, flags=None):
        self.base_path = base_path
        self.search_term = search_term
        self.output_file = output_file
        self.repos = self.get_repos()
        self.flags = flags if flags else []

    def get_repos(self):
        repos = [os.path.join(self.base_path, repo) for repo in os.listdir(self.base_path)]
        return [repo for repo in repos if os.path.isdir(os.path.join(repo, ".git"))]

    def search_repo(self, repo):
        command = ["git", "grep", *self.flags, self.search_term]
        try:
            result = subprocess.run(
                command,
                cwd=repo,
                capture_output=True,
                text=True,
                check=True
            )
            if result.stdout:
                return f"Results for {repo}:\n{result.stdout}\n"
            else:
                return f"No matches found in {repo}\n"
        except subprocess.CalledProcessError as e:
            return f"No matches found in {repo} or an error occurred:\n{e.stderr}\n"

    def run(self):
        file = open(self.output_file, "w") if self.output_file else None
        try:
            for repo in self.repos:
                result = self.search_repo(repo)
                if file:
                    file.write(result)
                else:
                    print(result)
            if file:
                print(f"Results have been written to {self.output_file}")
        finally:
            if file:
                file.close()

def print_usage():
    usage_text = """
    Usage: git-grep-all "search_term" [options] [--outfile output_file]

    Options:
    -n                    Show line numbers for each match.
    -E                    Search with Regular Expressions
    -l                    Show File names only
    --cached              Search only in staged files
    -outfile FILENAME     Write the output to FILE instead of displaying it in the console.

    Example:
    git-grep-all "error" -n --outfile results.txt
    Searches for the term "error" in all Git repositories under the base path
    including line numbers (-n) and saves the results to results.txt.
    """
    print(usage_text)

if __name__ == "__main__":
    BASE = 'your/base/directory'

    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    search = sys.argv[1]
    output_file = None
    flags = []

    if "-outfile" in sys.argv:
        output_index = sys.argv.index("-outfile") + 1
        if output_index < len(sys.argv):
            output_file = sys.argv[output_index]
            flags = sys.argv[2:output_index-1] + sys.argv[output_index+1:]
        else:
            print("Error: Please specify a file name after '-outfile'")
            sys.exit(1)
    else:
        flags = sys.argv[2:]

    grep = GitGrep(BASE, search, output_file, flags)
    grep.run()