#!/usr/bin/env python

import subprocess
import os
import sys

BASE = 'your/base/directory'

if len(sys.argv) < 2:
    print('used as: git-grep-all "some string"')
    exit(1)

search = sys.argv[1]

output_file = None
if "--outfile" in sys.argv:
    output_index = sys.argv.index("--outfile") + 1
    if output_index < len(sys.argv):
        output_file = sys.argv[output_index]
    else:
        print("Error: please specify a file name after '--outfile'")
        exit(1)

repos = os.listdir(BASE)
repos = [os.path.join(BASE, repo) for repo in repos]

file = open(output_file, "w") if output_file else None

for repo in repos:
    if not os.path.isdir(os.path.join(repo, ".git")):
        message = f"Skipping {repo}: Not a Git Repo"

        if file:
            file.write(message)
        else:
            print(message)
        continue

    try:
        results = subprocess.run( ["git", "grep", search], cwd=repo, capture_output=True, text=True)
        if results.stdout:
            message = f"Results for {repo}:\n{results.stdout}"
        else:
            message = f"No matches found in {repo}\n"

        if file:
            file.write(message)
        else:
            print(message)

    except subprocess.CalledProcessError as e:
        message = f"An error occured for {repo}:\n{e.stderr}"
        if file:
            file.write(message)
        else:
            print(message)

if file:
    file.close()
    print(f"Results have been written to {output_file}")