from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="cyp450-gnn-prediction",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Graph Neural Networks for CYP450 Substrate Prediction and Generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/CYP450-GNN-Prediction",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": ["pytest", "black", "flake8", "mypy"],
        "docs": ["sphinx", "sphinx-rtd-theme"],
        "gpu": ["torch-geometric[gpu]"],
    },
    entry_points={
        "console_scripts": [
            "cyp450-train=scripts.training.train_single_model:main",
            "cyp450-generate=scripts.generation.generate_molecules:main",
            "cyp450-evaluate=scripts.evaluation.evaluate_model:main",
        ],
    },
)
