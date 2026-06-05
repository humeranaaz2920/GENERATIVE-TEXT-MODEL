# Quick Start Guide

Get up and running with the Generative Text Model in minutes!

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- ~2GB disk space for model files

## 5-Minute Setup

### Step 1: Clone or Download

```bash
git clone https://github.com/yourusername/generative-text-model.git
cd generative-text-model
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Notebook

```bash
jupyter notebook text_generation_model.ipynb
```

### Step 4: Execute Cells

Run cells from top to bottom by clicking the ▶ button or pressing `Shift + Enter`.

## 10-Minute Tutorial

### Basic Usage in Python

```python
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# Load model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Generate text
prompt = "The future of artificial intelligence"
input_ids = tokenizer.encode(prompt, return_tensors='pt')

with torch.no_grad():
    output = model.generate(
        input_ids,
        max_length=150,
        temperature=0.7,
        top_p=0.9,
        do_sample=True
    )

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
```

### Using the Notebook

1. **Section 1**: Libraries are automatically imported
2. **Section 2**: Model loads on first run (downloads if needed)
3. **Section 3**: Text generation function is defined
4. **Section 4**: Example prompts are listed
5. **Section 5**: Click "Run All" to generate text for all prompts
6. **Section 6**: View results and statistics

## Common Tasks

### Generate Text on Any Topic

```python
topic = "Quantum computing breakthroughs"
output = model.generate(
    tokenizer.encode(topic, return_tensors='pt'),
    max_length=120,
    temperature=0.8,
    do_sample=True
)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

### Adjust Creativity Level

```python
# More factual (conservative)
temperature = 0.3

# More creative
temperature = 0.9
```

### Generate Multiple Variations

```python
output = model.generate(
    input_ids,
    max_length=150,
    num_return_sequences=5,  # Generate 5 different outputs
    temperature=0.8,
    do_sample=True
)

for i, seq in enumerate(output):
    print(f"Variation {i+1}:")
    print(tokenizer.decode(seq, skip_special_tokens=True))
    print()
```

## Troubleshooting

### Issue: "Module not found" error

**Solution**: Install missing packages
```bash
pip install torch transformers
```

### Issue: CUDA out of memory

**Solution**: Use CPU instead
```python
device = torch.device('cpu')
model.to(device)
```

### Issue: Slow on CPU

**Solution**: Install GPU-accelerated PyTorch
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Issue: Model not downloading

**Solution**: Set cache directory
```bash
export HF_HOME=/path/to/cache
```

## Next Steps

- 📖 Read [README.md](README.md) for detailed documentation
- 🤝 Check [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- 🐛 Report issues on [GitHub Issues](https://github.com/yourusername/generative-text-model/issues)
- 💬 Join discussions on [GitHub Discussions](https://github.com/yourusername/generative-text-model/discussions)

## Performance Tips

1. **GPU Usage**: Model runs 10x faster on GPU
2. **Batch Processing**: Generate multiple texts in one call
3. **Shorter Outputs**: Reduce `max_length` for faster generation
4. **Caching**: First run downloads model (~500MB), subsequent runs are instant

## Need Help?

- Check the [Troubleshooting](README.md#-troubleshooting) section in README
- Look at example notebooks
- Open an issue on GitHub
- Ask in discussions

Happy generating! 🎉
