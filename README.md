# AutoCommitAI 🤖

Automatic commit message generator using AI, with some extra features. But first, why?

## ❓ Why AutoCommit AI?

Writing commit messages is often a tedious task, and it is not always easy to condense or describe the changes we have made (or the bugs we have introduced), but fortunately this message is not as critical as the code we develop. AI can do a lot of things, although the less important that task is, the better. So for this one, it could help us generate meaningful and descriptive messages automatically, adding those “best practices” that, of course, we all apply in our commit messages. And yes, it creates the title and the description.

## 🚀 Main features

- 🧠 **Multiple AI providers**: OpenAI, Google Gemini, Azure OpenAI and Ollama
- 🌍 **Multi-language support**: Generate commits in Spanish, English, French, German, etc.
- 📋 **Interactive staging**: Select which files to include in the commit
- ✅ **User validation**: Ask for user validation before committing
- ➕ **Additional context**: Use extra information to generate more accurate messages, like branch name or manual context

**⚠️ DISCLAIMER for Ollama**: The Ollama integration is experimental and may not work as expected, as there are a lot of models, and some of theme are very limited. It is recommended to use OpenAI or Google Gemini for production use.

## 📦 Installation

You can install **AutoCommit AI** directly from PyPI using pip:

```bash
pip install auto-commit-ai
```

Alternatively, you can clone the repository and install directly from source:

```bash
git clone https://gitlab.com/tmllull/auto-commit-ai.git
cd auto-commit-ai
pip install .
```

## 🔧 Configuration

**AutoCommit AI** loads its configuration from environment variables file. You can set these variables in a `.auto_commit_ai.env` file located in your current working directory (where your git repository is) or your home directory (~/.auto_commit_ai.env).

**NOTE**: If you add the file to your working directory, remember to add it to your `.gitignore` file.

The contents of the `.auto_commit_ai.env` can be found in the `.auto_commit_ai.env.template` file.

## 🎯 Basic Usage

**AutoCommit AI** is a command-line tool. Navigate to your Git repository and run one of the following commands:

```bash
# Default command
auto-commit-ai
```

or

```bash
# Alias for the default command
acai
```

This is the default command, and it will generate a commit message for your **staged changes only**.

Both commands, `auto-commit-ai` and `acai`, are equivalent and can be used interchangeably.

### Basic commands

```bash
# Generates a commit message only for staged changes
auto-commit-ai

# Show help message
auto-commit-ai -h

# Include all changes (staged + unstaged + untracked)
acai --all

# Use specific provider
acai --provider google

# Generate in Spanish
acai --language es
```

### Preview message

```bash
# Preview without committing option
auto-commit-ai --preview

# Preview including all changes
acai --preview --all
```

### Interactive staging

```bash
# Select files for staging
acai --stage
```

## 📊 Repository information

```bash
# Repository status
acai --status

# Commit history
auto-commit-ai --history
```

## 🛠️ Advanced options

```bash
# Specific repository
auto-commit-ai --repo /path/to/repo

# Specific repository
auto-commit-ai --custom-prompts /path/to/custom_prompts.py

# Use current branch name in commit context
acai --branch-name

# Additional context for commit message generation
acai --context "Some extra context here"
```

**⚠️ DISCLAIMER for `--custom-prompts` flag**: Use this flag by your own risk. It allows you to use custom prompts for commit message generation, but it may lead to unexpected results if the prompts are not properly formatted or tested. Check the `custom_prompts_example.py` file for an example of how to create your own prompts.

### Output control

```bash
# Don't show status before commit
acai --no-status

# Verbose mode for debugging
acai --verbose
```

## 🌍 Supported languages

The system supports ISO 639-1 language codes:

- `en` - English (default)
- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `ja` - Japanese
- `zh` - Chinese
- `ru` - Russian
- And many more... As you use the ISO 639-1 codes, the system will adapt to your needs.

## 📋 Usage Examples

### Typical workflow

```bash
# 1. Check repository status
acai --status

# 2. Interactive file staging
acai --stage

# 3. Preview message
acai --preview

# 4. Generate final commit
acai
```

### Working with specific repository

```bash
# Work with another repository
acai --repo /path/to/project --status
acai --repo /path/to/project --all
```

## 🔄 Workflow

1. **Analysis**: Detects repository changes (staged, unstaged, untracked)
2. **Generation**: Uses AI to analyze diffs and generate descriptive message
3. **Review**: Shows generated message for confirmation
4. **Commit**: Creates commit with generated message
5. **Optional push**: Offers to push automatically

## 📝 Message format

Generated messages follow best practices:

- **Title**: Concise line describing the main change
- **Description**: Additional details when necessary
- **Conventions**: Follows standards like _Conventional Commits_ when appropriate

## 🚨 Error handling

The system gracefully handles:

- ❌ Non-Git repositories
- ❌ No changes to commit
- ❌ AI API errors
- ❌ Connectivity issues
- ❌ Incorrect configuration

## 📄 License

This project is licensed under the MIT License. See `LICENSE` file for more details.

## 🆘 Support

To report bugs or request features, please open an issue on the GitHub repository.

---

_Made with ❤️ for developers who value quality commits_
