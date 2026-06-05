# Contributing to Generative Text Model

Thank you for your interest in contributing to the Generative Text Model project! 🎉

This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

Please be respectful and constructive in all interactions. We are committed to providing a welcoming and inclusive environment.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:

1. **Clear description**: What is the bug?
2. **Steps to reproduce**: How can we reproduce it?
3. **Expected behavior**: What should happen?
4. **Actual behavior**: What actually happens?
5. **Environment**: Python version, OS, GPU/CPU, etc.
6. **Error messages**: Any relevant error messages or logs

### Suggesting Features

To suggest a feature:

1. Use the GitHub Issues tab
2. Provide a clear description of the feature
3. Explain why it would be useful
4. Show examples if applicable
5. Label as "enhancement"

### Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/generative-text-model.git
   cd generative-text-model
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the code style (PEP 8)
   - Add comments for complex logic
   - Update docstrings
   - Add type hints where applicable

4. **Test your changes**
   ```bash
   pytest tests/
   ```

5. **Run linting**
   ```bash
   black .
   pylint src/
   flake8 src/
   ```

6. **Commit your changes**
   ```bash
   git commit -m "Add descriptive commit message"
   ```

7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request**
   - Provide a clear title and description
   - Reference any related issues
   - Explain the changes made
   - Add before/after comparisons if applicable

## Development Setup

### Prerequisites
- Python 3.8+
- Git
- pip or conda

### Local Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/generative-text-model.git
cd generative-text-model

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black pylint flake8

# Run tests
pytest tests/
```

## Code Style Guidelines

### Python Style
- Follow PEP 8
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use descriptive variable names

### Documentation
- Add docstrings to all functions and classes
- Use Google-style docstrings
- Include type hints

Example:
```python
def generate_text(prompt: str, max_length: int = 150, 
                  temperature: float = 0.7) -> str:
    """
    Generate text based on a prompt using GPT-2 model.
    
    Args:
        prompt (str): Input prompt for text generation
        max_length (int): Maximum length of generated text. Default: 150
        temperature (float): Controls randomness (0.0-1.0). Default: 0.7
        
    Returns:
        str: Generated text
        
    Raises:
        ValueError: If temperature is not between 0 and 1
        
    Example:
        >>> text = generate_text("Hello", max_length=100)
        >>> print(len(text.split()))
    """
    # Implementation
    pass
```

## Testing

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_generation.py

# Run with coverage
pytest --cov=src tests/
```

### Writing Tests
- Use descriptive test names
- Test both success and error cases
- Include docstrings
- Use fixtures for common setup

```python
def test_generate_text_with_valid_prompt():
    """Test text generation with valid prompt."""
    result = generate_text("Hello")
    assert isinstance(result, str)
    assert len(result) > 0

def test_generate_text_with_invalid_temperature():
    """Test that invalid temperature raises ValueError."""
    with pytest.raises(ValueError):
        generate_text("Hello", temperature=1.5)
```

## Documentation

- Update README.md if adding new features
- Add docstrings to new code
- Update requirements.txt if adding dependencies
- Create/update relevant comments for complex logic

## Commit Message Guidelines

Use clear, descriptive commit messages:

```
Format: [TYPE] Brief description

Types:
- [FEAT] New feature
- [FIX] Bug fix
- [DOCS] Documentation update
- [STYLE] Code style changes
- [REFACTOR] Code refactoring
- [TEST] Test additions/modifications
- [PERF] Performance improvements

Examples:
- [FEAT] Add batch text generation support
- [FIX] Fix CUDA memory overflow in generation
- [DOCS] Update installation instructions
- [PERF] Optimize tokenizer performance
```

## Issue Labels

- `bug` - Bug reports
- `enhancement` - Feature requests
- `documentation` - Documentation improvements
- `good first issue` - Good for new contributors
- `help wanted` - Need assistance
- `wontfix` - Will not be fixed

## Review Process

1. All PRs require at least one review
2. CI/CD checks must pass
3. Code coverage should not decrease
4. Conflicts must be resolved
5. Squash commits when requested

## Questions?

- Check existing issues and discussions
- Ask in GitHub Discussions
- Contact maintainers via email

## Recognition

Contributors will be acknowledged in:
- CONTRIBUTORS.md
- Release notes
- GitHub contributors page

Thank you for contributing! 🙌
