---
draft: false
date: 2025-07-20
comments: true
authors:
  - fbruzzesi
categories:
  - Tips
  - Programming
  - Python
---

# Stop Context-Switching: How Git Worktree + UV Revolutionized my python workflow

If you've ever found yourself frantically stashing changes, switching branches, and losing your mental context just to
review a pull request or work on a quick hotfix, you know the pain.

For Python developers, this was made even worse by the overhead of managing virtual environments.
But the combination of [`git worktree`][git-worktree] and [`uv`][uv] has completely changed the game.

<!-- more -->

## The python developer's nightmare

Picture this: you're deep in the zone, refactoring a complex piece of code. Your virtual environment is active,
your IDE has multiple files open, and you're making great progress. Then your teammate asks you to review their PR that
uses different dependencies, or production breaks and you need to create a hotfix, or your open source project has an
issue with a different python version, or a library just got an update you need to test.

The traditional Python workflow was brutal:

1. Deactivate your current virtual environment
2. Stash or commit your work-in-progress with some meaningless message
3. Switch branches
4. Create a new virtual environment
5. Install all dependencies
6. Lose all your IDE context (open files, breakpoints, etc.)
7. Do the review/hotfix
8. Reverse the entire process to get back to your work

This wasn't just context-switching, it was context obliteration.

The alternative I have seen multiple times is to have different clones of the same repo, which also can get quite
impractical to manage very quickly.

## Enter `git worktree`

`git worktree` solved half the problem. It lets you check out multiple branches of the same repository simultaneously,
each in its own directory:

```bash
# Create a new worktree for the hotfix
git worktree add ../myproject-hotfix main

# Your directory structure now looks like:
# myproject/          (your current branch + venv)
# myproject-hotfix/   (main branch, but no venv yet...)
```

This was great for avoiding context-switching, but there is (well actually _was_) still a problem.

If you need a virtual environment (and don't want to mess around with the main repo one), you will need to create a new
one on each worktree. This process was painfully slow:

```bash
cd ../myproject-hotfix
python -m venv .venv          # at least a few seconds
source .venv/bin/activate
pip install -e .              # probably a few minutes
pip install pytest coverage   # more waiting time
```

By the time you finished setting up the environment, you'd lost your flow state anyway.

## `uv` changes everything

Then `uv` came along and made this workflow _actually_ practical.
UV's speed and intelligent caching transformed worktrees from "theoretically useful" to "absolutely essential."

Here's the same workflow with `uv`:

```bash
cd ../myproject-hotfix
uv venv                         # can't even blink
source .venv/bin/activate
uv pip install -e .             # essentially instant if cached
uv pip install pytest coverage
```

What used to take minutes now takes under a second. The difference is game-changing.

## The modern python workflow

I recently started to experiment with [just recipes][just], and this is the global recipe I set up (thanks LLMs):

```bash
cat >> ~/.justfile << 'EOF'
[doc("""
Create a new git worktree with Python virtual environment setup.

Examples:

* Create worktree for branch 'feature/foo-bar' with Python 3.11
just worktree feature/foo-bar 3.11

* Create worktree for branch 'hotfix/bug-123' with Python 3.12
just worktree hotfix/bug-123 3.12

* Create worktree for branch 'develop' with default Python (3.12)
just worktree develop
""")]
worktree branch python="3.12" working_dir=invocation_directory():
    #!/bin/bash
    set -euo pipefail
    
    # Change to the directory where just was invoked
    cd "{{working_dir}}"
    
    # Get current directory name
    current_dir=$(basename "${{working_dir}}")
    
    # Create worktree path: ../<current-folder-name>-<branchname>
    # Replace forward slashes in branch name with dashes for directory name
    safe_branch=$(echo "{{branch}}" | sed 's/\//-/g')
    worktree_path="../${current_dir}-${safe_branch}"

    echo "Creating git worktree for branch '{{branch}}' at path: $worktree_path"
    
    # Run git worktree add
    git worktree add "$worktree_path" origin/main -b "{{branch}}"
    
    echo "Moving into worktree directory: $worktree_path"
    cd "$worktree_path"
    
    # Create virtual environment with uv (with python version if specified)
    echo "Creating virtual environment with uv using Python {{python}}..."
    uv venv --python "{{python}}"
    
    # Activate the virtual environment and install project in editable mode
    echo "Installing project in editable mode..."
    source .venv/bin/activate
    uv pip install -e .
    
    echo "✅ Worktree setup complete!"
    echo "📁 Worktree location: $worktree_path"
    echo "🐍 To activate the environment, run: source $worktree_path/.venv/bin/activate"
```

Now running `just worktree feat/just-for-the-blog` will:

* create a git worktree on the same level of the current folder
* create a virtual env, activate it and install the codebase in editable mode

The entire setup took less than half a second. This is very acceptable!!!

??? tip "Proof"

    <img src="../../../../../images/2025-07-20-worktrees-and-uv/example.png">

## `uv` purists disclaimer

I know the spirit of `uv` is to avoid having virtual envs completely, yet especially when developing on open source
I find myself using different envs, with different python versions and different library versions.

I still didn't wrap my head around how to do it properly in the way `uv` _wants_ this to be done! Feel free to send help!

## The bottom line

For Python developers, the combination of `git worktree` and `uv` isn't just a workflow improvement, it's a paradigm shift.
UV's speed eliminated the last major friction point that made worktrees impractical for Python projects.

The result? Better code reviews, more thorough testing, cleaner dependency management, and the ability to work on multiple Python versions and feature branches simultaneously without losing your mind.

Try the combo for a week. I guarantee you'll never go back to the old way of context-switching hell.

<img src="../../../../../images/written-by-human.svg" align="right">

[git-worktree]: https://git-scm.com/docs/git-worktree
[uv]: https://docs.astral.sh/uv/
[just]: https://just.systems/man/en/introduction.html
