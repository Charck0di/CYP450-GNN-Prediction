# CYP450 GNN Prediction: Graph Neural Networks for Cytochrome P450 Substrate Prediction and Generation

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.12%2B-red.svg)](https://pytorch.org)

A comprehensive framework for predicting and generating Cytochrome P450 (CYP450) substrates using Graph Neural Networks (GNNs) and protein embeddings.

## Features

- 🧬 Multi-CYP enzyme prediction (CYP1A2, CYP2C9, CYP2C19, CYP2D6, CYP2E1, CYP3A4)
- 🔬 Multiple GNN architectures (GCN, GAT, GIN, D-MPNN)
- 🤖 ESM-1b protein embeddings integration
- 🎯 Ensemble modeling with XGBoost
- 🧪 Molecule generation and optimization
- 📊 Comprehensive evaluation metrics
- 🔍 Virtual screening capabilities

## Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/CYP450-GNN-Prediction.git
cd CYP450-GNN-Prediction

# Install dependencies
pip install -r requirements.txt

# Train a model
python scripts/training/train_single_model.py --cyp_enzyme CYP3A4 --model_type GIN

# Generate molecules
python scripts/generation/generate_molecules.py --cyp_enzyme CYP3A4 --n_candidates 1000
