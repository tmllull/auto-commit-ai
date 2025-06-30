# auto-commit-ai

`auto-commit-ai` is a Python module that automatically generates commit messages for your codebase by analyzing the changes in your code. It leverages AI to summarize code diffs and suggest meaningful commit messages, streamlining your development workflow and improving commit quality.

## Features

- **Automatic commit message generation**: Uses AI to analyze code changes and generate descriptive commit messages.
- **Easy integration**: Can be used as a CLI tool or integrated into your existing workflow.
- **Customizable providers**: Supports multiple AI providers for flexibility.

## Installation

```bash
pip install auto-commit-ai
```

Or clone the repository:

```bash
git clone https://gitlab.com/tmllull/auto-commit-ai.git
cd auto-commit-ai
pip install .
```

## Configuration

There are 2 main ways to configure `auto-commit-ai`:

1. Create a `.auto-commit-ai.env` into the root of your project. If you use this option, remember to add it to your `.gitignore`
2. Create a `.auto-commit-ai.env` with the root of your user directory.

After that, just fill the required parameters on `.auto-commit-ai.env`

## Usage

You can use `auto-commit-ai` from the command line:

```bash
auto-commit-ai
```
