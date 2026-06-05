"""Setup configuration for Generative Text Model package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="generative-text-model",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A GPT-2 based generative text model for coherent paragraph generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/generative-text-model",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/generative-text-model/issues",
        "Documentation": "https://github.com/yourusername/generative-text-model#readme",
        "Source Code": "https://github.com/yourusername/generative-text-model",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "pylint>=2.17.0",
            "flake8>=6.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "generate-text=src.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
