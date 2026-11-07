# CS 236 Project 0: VS Code Setup & Git Basics

**Pre-requisite**: you must have Python 3.12 or higher and `git` installed on your system _before_ starting this project. If you aren't sure whether these are installed on your system or how to install them, feel free to talk to the TAs or to work with an AI Assistant for help.

## Table of Contents
- [0. Create a Base Folder](#0-create-a-base-folder)
- [1. Install & Configure Visual Studio Code (VSCode)](#1-install--configure-visual-studio-code-vscode)
- [2. Clone the Starter Repository](#2-clone-the-starter-repository)
- [3. Explore Project Structure](#3-explore-project-structure)
  - [Confirm that you have the correct files](#confirm-that-you-have-the-correct-files)
- [4. Set up your Python Environment with `venv`](#4-set-up-your-python-environment-with-venv)
  - [4.1 Deactivate Conda (if active)](#41-deactivate-conda-if-active)
  - [4.2 Create a Virtual Environment](#42-create-a-virtual-environment)
  - [4.3 Activate the Virtual Environment](#43-activate-the-virtual-environment)
- [5. Python Modules, Packages, and Installation](#5-python-modules-packages-and-installation)
  - [5.1 Python Modules vs. Packages](#51-python-modules-vs-packages)
    - [Module](#module)
    - [Package](#package)
  - [5.2 When to Use a Module vs. a Package](#52-when-to-use-a-module-vs-a-package)
- [6. What is a CLI?](#6-what-is-a-cli)
    - [Why Use a CLI?](#why-use-a-cli)
    - [Step-by-Step: How This Project Sets Up a CLI](#step-by-step-how-this-project-sets-up-a-cli)
    - [6.1-Install the project0 package](#61-install-the-project0-package)
    - [6.2-Run the Code](#62-run-the-code)
- [7. Modify and Run `compute()` in `src/project0/project0.py`](#7-modify-and-run-compute-in-srcproject0py)
  - [7.1 Open and Explore the Code](#71-open-and-explore-the-code)
  - [7.2 Learn Learn How to Use TODOs](#72-learn-how-to-use-todos)
  - [7.3 Replace the `compute()` Function](#73-replace-the-compute-function)
  - [7.4 Run the Project from the Command Line](#74-run-the-project-from-the-command-line)
  - [7.5 Run from Inside VS Code](#75-run-from-inside-vs-code)
- [8. Using Git: Modify → Stage → Commit → Push](#8-using-git-modify-stage-commit-push)
  - [What Each Step Means](#what-each-step-means)
  - [8.1 Using the Integrated Terminal](#81-using-the-integrated-terminal)
  - [8.2 Using the VS Code Source Control Panel](#82-using-the-vs-code-source-control-panel)
- [9. Verify on GitHub](#9-verify-on-github)
- [What You’ve Learned](#what-youve-learned)

---

## 0. Create a Base Folder

1. On your machine, create a folder named `CS236`.
2. All CS 236 starter repos (Project 0, 1, 2, …) will be cloned into `CS236/` to keep your work organized.

If you don't know for sure how to create this folder, ask your favorite AI tool for help. You'll need to tell the AI tool whether your computer is a mac or a PC.

---

## 1. Install & Configure Visual Studio Code (VSCode)
You will use Visual Studio Code as the Integrated Development Environment (IDE) for this class. This section describes how to install and configure VSCode so that it will run Python and the tools you will need in this and subsequent projects.

1. **Download & install** VSCode by following the instructions from:
   https://code.visualstudio.com/

2. **Launch VSCode**

3. **Open the Extensions panel in VSCode**:
   - Windows/Linux: `Ctrl+Shift+X`
   - macOS: `⌘+Shift+X`
   - Or click the stacked block icon  <img src="images/extensions_panel.png" alt="Extensions Panel" width="18" /> in the Activity Bar

3. **Search for** and **install**:
   - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) Microsoft bundle
   - [MyPy](https://marketplace.visualstudio.com/items?itemName=matangover.mypy) by Matan Grover
   - [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) by Astral Software
   - [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) by Microsoft
   - [GitHub Actions](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-github-actions) by GitHub

---

## 2. Clone the Starter Repository
We've created a set of files that you will use for the rest of this project. The files are stored in a _git repository_. This section explains how you copy the files from where we've placed them to your local machine. A subsequent section explains how you upload your files to `git` so that they will be saved in the cloud and so that your code can be automatically graded.

1. Open the **Source Control** panel in VSCode:
   - Windows/Linux: `Ctrl+Shift+G`
   - macOS: `⌘+Shift+G`
   - Or click the source control icon <img src="images/source_control_icon.png" alt="Source Control" width="18" /> in the activity bar

2. Click **Clone Repository**, paste your repo URL, and choose `CS236/` as the destination. You can find the repo URL by clicking on the green _Code_ button at the top of the GitHub page.

3. When prompted, click **Open** to load the project in VS Code.

The next section describes the folders that you have copied (or _cloned_) to your machine.

---

## 3. Explore Project Structure

The root folder is the `CS236` directory you created earlier. Inside that folder is another folder named something like `project0`. The precise name might vary, but you'll see the name `project0` somewhere in the name. Inside the `project0` are a handful of other files and folders. The general structure is given by

```
CS236
└── project0/
    ├── README.md
    ├── pyproject.toml
    ├── images/
    ├── src/
    │   └── project0
    └── tests/
```

The key files and folders are:

- **README.md** – this tutorial
- **pyproject.toml** – configuration file that defines project metadata (name, version, dependencies) and CLI entrypoint; CLI stands for Command-Line Interface, letting you run `project0` as a script.
- **images/** - images used in this tutorial
- **src/** - source directory containing Python files used in the `project0` package.  The module `project0.py` is found in this `src/project0` directory folder. We'll look at the other files in the `src/project0` folder later.
- **tests/** –  directory reserved for future projects where you'll use unit tests to verify your code automatically. One goal of CS 236 is to use unit tests to help you connect the mathematical ideas taught in the class with useful coding patterns and practices.

### Confirm that you have the correct files
There are two ways to check whether you have the correct files: using the integrated terminal and using the _Explorer Panel_ in VSCode.

**Using the Integrated Terminal in VSCode.** Open the integrated terminal and list the files. Make sure that you see `images`, `pyproject.toml`, `README.md`, `src`, and `tests`.

**Using Explorer in VSCode.**
Click the explorer icon  <img src="images/explorer_icon.png" alt="Explorer Icon" width="18" /> in the Activity Bar. This will open a window on the left side of VSCode. The window should show all the files listed above and a few others that we aren't using right now.

## 4. Set up your Python Environment with `venv`

A _virtual environment_ is a lightweight, local Python environment used to isolate project-specific packages from the default Python settings on your computer. Using a virtual environment prevents dependency conflicts and ensures that your installed tools (like  `mypy`, `ruff`, or `pytest`, which we'll use in subsequent projects) behave consistently across machines. The name of the virtual environment we will use is `venv`.

### 4.1 Deactivate Conda (if active)

We've learned that some prior classes have you install and automatically load an environment called `conda` so that the tools in those classes work. `conda` doesn't work well with `venv` so you have to make sure that conda is deactivated if you’re using a computer that automatically loads a conda environment (e.g. from Anaconda). You deactivate `conda` by doing the following steps:

- Open the Integrated Terminal inside VSCode
  - **Menu**: _View → Terminal_
  - **Shortcut**:
    - Windows/Linux: ``Ctrl+` ``
    - macOS: ``⌃` ``
- Look to see if you have a conda environment installed. Look at the line before the prompt in the terminal. If it starts with `(base)` or has some other environment indicator in parentheses `(who)`, then you need to do the next step.
- Deactivate conda by typing

```bash
conda deactivate
```

You'll know you've been successful if the `(base)` part of the prompt will have disappeared.

### 4.2 Create a Virtual Environment
You now have to create the virtual environment so that all the code you execute inside of VSCode uses that environment. Make sure you are in your `CS236/` directory. What you type next depends on what type of computer you are using and how it is configured. Usually, PCs install the latest version of Python so that you can execute it by typing `python`. Macs usually ship with an old version of python and the command `python` points to that old version. To overcome this, you run python by typing `python3`. Thus,

If on a PC then you should type
```bash
python -m venv .venv
```
and if on a Mac or a computer configured to use Linux then you should type
```bash
python3 -m venv .venv
```
This creates a hidden directory called `.venv` in your project folder containing a standalone Python environment.

You can check to see if you are successful by typing in the command that lists all files in the current folder. If you don't knw how to do this on your machine, ask your favorite AI agent.

On a Mac or (most) Linux-based machine, you must type
```bash
ls -al
```
from the prompt. The command `ls` lists all the files in the current folder except for those that start with a period. Adding the `-al` next to the `ls` command lists all the files in the current folder including those that start with a period.

When you list all the files in your folder then you should see a folder named `.venv` in the list of things that appear.

### 4.3 Activate the Virtual Environment
You now have to tell VSCode that you want to use the virtual environment. This is called _activating_ the environment. How you activate `venv` depends on your machine.

For a Windows machine running PowerShell,
```powershell
venv\Scripts\Activate.ps1
```

and on a Mac or Linux-based machine
```bash
source .venv/bin/activate
```
If you are having trouble activating the virtual environment, ask an AI agent how to tell which machine you are working on and ask for help.

You'll know that you've been successful if the name of the prompt changes and starts with `(.venv)`.

---

---
## 5. Python Modules, Packages, and Installation

In this step, you’ll learn:

- The difference between Python modules and packages
- How Python project structure affects imports
- How to install your own project as a package
- How command-line interfaces (CLIs) are connected to the configuration file called `pyproject.toml`

---

### 5.1 Python Modules vs. Packages

Python projects are made up of **modules** and **packages**. Understanding the distinction will help you understand how the starter code for subsequent projects is organized. That understanding will help you organize and import your files correctly.

#### Module

- A **module** is a single `.py` file.
- It can contain functions, variables, classes, and runnable code.

Example. Suppose we have a file `project0.py` that contains only the definition of a function called `compute`:
```python
# src/project0.py
def compute(input: str) -> str:
    return "Hello World " + input
```

We can import a module in Python using the following command, which is placed at the top of a file.

```python
import project0       # if project0.py is in your Python path
```
This command imports a _module object_, which is a special type of object. We can access the member functions of this object using the dot notation, just like is done with other objects. If we wanted to access the function `compute` that is defined in `project0.py` we'd type
```python
project0.compute("input to function")
```
We can also just import the function from the module by inserting the following command in a python file:
```python
from project0 import compute
```
We can then directly execute the function without using the dot notation,
```python
compute("input to function")
```


#### Package

- A **package** is a folder that contains a special file called `__init__.py`.
- It may also contain multiple `.py` files or even sub-packages.
Notice that a _module is a single file_ and a _package is a folder_ that contains at least the file `__init__.py` and can contain other files.

Example structure:
```
project0/              ← package directory
├── __init__.py        ← marks this as a package
└── project0.py        ← a module inside the package
```

Importing from a package:
```python
from project0.project0 import compute
```

In the statement
```python
from project0.project0
```
the  _project0._ (note the trailing period) indicates that the package is saved in the `project0` directory, and the _project0_ after the period indicates that we're importing from the file `project0.py`.


This project and the starter code for future projects all use `src/` as the root directory for code. This class will always configure Python to look for packages there. The file `pyproject.toml` configures Python to look in the `src/` directory. The next section says a little more about what else is done by the file `pyproject.toml`.

### 5.2 When to Use a Module vs. a Package

Use a **module** when:
- You’re working on a small, focused piece of functionality
- All your code fits comfortably in one file
- You don’t need to split the logic across multiple files
- Examples:
    - math_utils.py with a few math helper functions
    - cli_tool.py for a short script with a command-line interface
- Benefits:
    - Simple to write and import
    - Great for scripts, utilities, and small tools

Use a **package** when:
- Your project grows beyond a single file
- You want to organize related modules into a namespace (folder)
- You have multiple concerns (e.g., CLI, logic, tests, helpers)
- You want to expose a public API while hiding internal structure
- Benefits:
    - Easier to manage larger codebases
    - Encourages modular design
    - Keeps related functionality grouped

For example, suppose we have several files that can be used together but which are best organized into different logical units. Call the package `myproject` by creating a folder with that name and then save the files into that folder, yielding.

```
myproject/
├── __init__.py
├── compute.py
├── parser.py
└── cli.py
```

You can then import different functions from the different modules using, for example,
```python
from myproject.compute import calculate
from myproject.cli import main
```

---

## 6. What is a CLI?

A **CLI**, or **Command-Line Interface**, lets users interact with a program by typing commands into a terminal.

In previous classes, you ran a Python script either by clicking buttons on a graphical interface or by typing something like this from the command line
```bash
python3 myfile.py
```
This command says to run `python3` and have it execute the code in `myfile.py`. This required that the `myfile.py` had a function called `main`.

A command-line interface allows the a program to be run directly as a command without typing `python3`. In the case of this project, you'd run

```bash
project0 hello
```

#### Why Use a CLI?
- It lets you build tool-like behavior: users can run your code from the terminal, pass arguments, and automate things.
- It helps simulate how real-world Python packages work.
- Many Python libraries include CLI tools (black, pytest, mypy, ruff, etc.).

#### Step-by-Step: How This Project Sets Up a CLI

   1.   Your code is in a function named `project0cli()` in `src/project0/project0.py`

   2.   The `pyproject.toml` file contains:

```python
[project.scripts]
project0 = "project0.project0:project0cli"
```
   3. When you install the projects in this class, several things happen. The two important ones (for now) are: (a) you tell Python that you are using a package and where to find that package, and (b) you tell Python to create a _command-line interface_ so that you can run the code directly from the command line.

### 6.1 Install the project0 package
Type
```bash
pip install --editable ".[dev]"
```
for a Windows-based machine or typing
```bash
pip3 install --editable ".[dev]"
```
for most Macs or Linux-based machines.

Note that the quotation marks and brackets in `".[dev]"` are part of the command. Make sure you are in the root directory of your project, and then run this instruction from the command line.

### 6.2 Run the Code
From the command line, type

```bash
project0 hello
```
You should see something like
```txt
I am not implemented yet.
Traceback (most recent call last)
...
NotImplementedError
```
The ... indicates that the the function isn't yet implemented correctly. We'll talk about this in the next section.

---

## 7. Modify and Run `compute()` in `src/project0.py`

### 7.1 Open and Explore the Code

1. Open the **Explorer** panel:
   - Windows/Linux: `Ctrl+Shift+E`
   - macOS: `⌘+Shift+E`
   - Or click the Explorer icon <img src="images/explorer_icon.png" alt="Explorer Icon" width="18" /> in the Activity Bar

2. Open `src/project0.py` and locate the function:

```python
# TODO: This code should return "Hello World" plus whatever the value of "input" is.
def compute(input: str) -> str:
    # YOUR CODE GOES HERE
    raise NotImplementedError
```

Ask your favorite AI assistant:
> What does `raise NotImplementedError` do?

**Discussion**: Why might this be useful when you’re writing a function that isn’t ready yet?

### 7.2 Learn How to Use TODOs

**How to find TODOs in the code?** The `pyproject.toml` file is configured to report comments that start with `TODO:`. Adding comments like this is a great way to keep track of all the little things that pop into your mind while you are coding.

You can see all your TODOs in _VSCode_ the _Problems_ view. You can access this either
- by opening the file `src/project0/project0.py`, going to the _VS Code_ menu, and choosing _"View" --> "Problems"_ with the `src/project0/project0.py` file open, or
- by opening the integrated terminal and clicking on the `PROBLEMS` tab at the top of the terminal.

**TODOs and Ruff**
When you installed the `project0` package, the `pyproject.toml` file installed a tool called `ruff`.

```
[tool.ruff]
lint.extend-select = ["I","FIX002", "TD001"]
target-version = "py312"
```

It is the `ruff` tool that detects and reports `TODO:` comments. The behavior is configured in the `pyproject.toml` file:

You can run `ruff` in the integrated terminal from the `project0` folder by typing
```bash
ruff check .
```
and see all the _problems_ that it finds. You'll get something in your terminal that looks like

```bash
src/project0/project0.py:15:3: FIX002 Line contains TODO, consider resolving the issue
   |
15 | # TODO: This code should return "Hello World" plus whatever the value of "input" is.
   |   ^^^^ FIX002
16 | def compute(input: str) -> str:
17 |     # YOUR CODE GOES HERE
   |
```

Remove the `TODO` from the file and confirm that it disappears from the `PROBLEMS` and also from the output of running `ruff check .`.

---

### 7.3 Replace the `compute()` Function

Replace the placeholder function with a working version:

```python
def compute(input: str) -> str:
    return "Hello World " + input
```

---

### 7.4 Run the Project from the Command Line

In your terminal (with the virtual environment activated and the package installed):

```bash
project0 CS236
```

You should see:
```
Hello World CS236
```

This runs the CLI entrypoint defined in your `pyproject.toml` as discussed in [6. What is a CLI?](#6-what-is-a-cli):

---

### 7.5 Run from Inside VS Code

To allow running (debugging) inside VS Code without using the CLI, we've included the script `debug_project0.py` which has the following code:

```python
import sys
sys.argv = ["project0", "CS236"]

from project0.project0 import project0cli

if __name__ == "__main__":
    project0cli()
```

The `sys.argv = ["project0", "arg1"]` sets up the CLI argument for `project0cli()`. You can change the input to `compute` function by changing `"CS236"` to something else. For now, just keep it the same, but make a mental note that if you want to modify the input to a file you are debugging, you will need to change that parameter in `debug_project0.py`.

Before you can run or debug a program, you need to tell _VS Code_ which version of Python to use. Click on `View` in the menu anc select `Command Palette`. Start typing `Python` and click on `Python:SelectInterpreter`. Choose the one that starts with `.venv` so that it uses the version of Python that is part of your virtual environment.


Once you've selected the correct Python interpreter, run the `compute` function with input `"VSCode"` from within VSCode by clicking the ▶ **Run Python File** button in the top right of the editor.

If you have modified the code as instructed above, you should see the following in the integrated terminal:

```
Hello World CS236
```

We won't spend time talking about how to set break points and step through code, but now that you have configured _VS Code_ you can ask your favorite AI tool for a tutorial on how to use the debugger in _VS Code_ and it will step you through things.

---

You've now learned how to:
- Modify and test a function
- Use a `NotImplementedError` stub
- Manage TODOs
- Run the project from the command line and from within VSCode

---

## 8. Using Git: Modify, Stage, Commit, Push

In this section, you’ll learn how to:
- Make and track changes with Git
- Use **4 key Git stages**:
  1. Modify your code
  2. Stage your changes (`git add`)
  3. Commit those changes (`git commit`)
  4. Push those commits to GitHub (`git push` or **Sync** in VS Code)

You’ll learn how to do this both:
- Using the **Integrated Terminal**
- Using **VS Code’s Source Control Panel**

---

### What Each Step Means

| Step   | Command         | What it does                                                               |
|--------|------------------|----------------------------------------------------------------------------|
| Modify | —                | You edit files in your workspace                                          |
| Stage  | `git add`        | You tell Git _which changes_ should be included in the next snapshot      |
| Commit| `git commit`     | You create a permanent snapshot of those staged changes                   |
| Push   | `git push` / Sync| You upload your commits to GitHub so they are saved and shared            |

---

### 8.1 Using the Integrated Terminal

Open the integrated terminal and do the following:

1. **Modify your code**
You don't need to do this since you've already been modifying yor code.

2. **Stage your changes**

   If you want to add a specific file:
   ```bash
   git add src/project0/project0.py
   ```

   If you want to stage all modified files:
   ```bash
   git add .
   ```

   > This step **does not save your work yet** — it just marks which files you want to commit.

3. **Commit with a message**
   ```bash
   git commit -m "Implement compute() for Project 0. Command line commit"
   ```

   > A commit message should summarize what you changed. This creates a **named snapshot** of your work.

4. **Push to GitHub**
   ```bash
   git push origin main
   ```

   > This uploads your commits to GitHub, making them visible in the online repository.

   If your default branch is named something else (e.g. `main` vs `master`), replace `main` as needed.

---

### 8.2 Using the VS Code Source Control Panel

Open the _source control panel_.
   - Shortcut:
     - Windows/Linux: `Ctrl+Shift+G`
     - macOS: `⌘+Shift+G`
   - Or click the Source Control icon  <img src="images/source_control_icon.png" alt="Source Control" width="18" />

1. **Change something in your code**

2. **Stage your changes**
   - Find the file(s) listed under **Changes**
   - Hover and click the ➕ next to each file to stage them
   - Or click the **+ Stage All Changes** button

   > If you skip this step, your commit won’t include any files.

3. **Write a commit message**
   - Use the input box above the file list
   - Example:
     ```
     Implement compute() for Project 0. VSCode commit.
     ```

4. **Click ✔ Commit**
   - This saves your staged changes as a named commit.

5. **Click Sync to Push**
   - Click the **Sync Changes** button at the bottom status bar
   - Or open the **… menu → Push** from the Source Control panel

   > “Sync” = Push + Pull = send your changes **and** get any updates from GitHub.


---

## 9. Verify on GitHub

1. Open your repo URL in a browser.
2. Confirm that your latest commit appears.
3. If CI/tests are enabled, check that your code passed.

---

## What You’ve Learned

- Organizing projects under a single `CS236/` folder
- Installing & using VS Code extensions
- Navigating VS Code panels & icons
- Using TODOs
- Running Python code inside VS Code
- Understanding `src/` layout and `pyproject.toml` scripts
- Cloning, staging, committing, and pushing with Git

---
