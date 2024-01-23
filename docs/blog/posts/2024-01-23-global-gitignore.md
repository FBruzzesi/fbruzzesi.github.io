---
draft: true
date: 2024-01-23
authors:
  - fbruzzesi
categories:
  - TIL
tags:
  - git
  - TIL
---

# Global `.gitignore`

I was today years old when I learned about the possibility of setting a global `.gitignore` file.

<!-- more -->

Are you annoyed by people (mostly yourself) adding random files/patterns to repository `.gitignore` file, such as editor configuration files, temporary files, or tool caches?

Say no more! You can set a global `.gitignore` file that will be used _everywhere_.

The steps are really simple:

1. Create a `.gitignore` file, typically in your home directory:
  
    ```bash
    touch ~/.gitignore
    ```

2. Open you favourite editor and add to such `.gitignore` file whatever file, folder and pattern you _always_ want to ignore.
  
    My personal configuration looks something like this:

    ```bash
    .vscode
    .env
    **/*.log
    **/dev_nb.ipynb
    _typos.toml

    # caches
    .mypy_cache/
    .ruff_cache/
    ```

3. Make **git** aware of such global configuration by setting the `core.excludesFile` property to the path of the `.gitignore` file you just created:

    ```bash
    git config --global core.excludesFile ~/.gitignore
    ```

4. That's it, you are set and done! 🎉
  
From now on, every time you run a git command the files and patterns you added to the global `.gitignore` file will be ignored.

Happy coding! 🚀
