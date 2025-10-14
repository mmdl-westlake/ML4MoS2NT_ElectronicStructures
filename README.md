# An Atlas of Chirality-Dependent Electronic Structures of MoS2 Nanotubes from Deep Learning

This repository contains the models and inference scripts for the paper:  
**"An Atlas of Chirality-Dependent Electronic Structures of MoS2 Nanotubes from Deep Learning"**

Developed by: **Ju Huang**

---

## Overview

This project aims to:

- **Fine-tune the CHGNet model** for structural optimization of MoS2 systems.
- **Train DeepH-E3** for predicting electronic band structures across the entire chirality space of MoS2 nanotubes.

The dataset for fine-tuning CHGNet and training DeepH-E3 can be found at:  
[https://doi.org/10.6084/m9.figshare.30338542.v1](https://doi.org/10.6084/m9.figshare.30338542.v1)

---

## Installation

### 1. DeepH-pack Environment

Install the DeepH-pack environment by following the instructions at:  
[https://github.com/mzjb/DeepH-pack](https://github.com/mzjb/DeepH-pack)
[https://github.com/Xiaoxun-Gong/DeepH-E3](https://github.com/Xiaoxun-Gong/DeepH-E3)

Or via conda:

```bash
conda env create -f deeph-gpu.yml
```

### 2. CHGNet

Install CHGNet with pip:

```bash
pip install chgnet
```

Or via conda:

```bash
conda env create -f chgnet.yml
```

---

## Example Usage

### 1. Structure Optimization with CHGNet

- Download the script: `chgnet_relax.py`
- conda activate chgnet
- Use it to perform structure optimization on MoS2 monolayers and nanotubes

### 2. Inference of Electronic Structure with DeepH-E3

- To run inference with the trained DeepH-E3 model for electronic band structures:

**Step 1:** Generate overlap matrices HDF5 files

```bash
sbatch scripts/DeepH_E3/model_inference/run_overlap_inference_forloop.sh
```

**Step 2:** Evaluate electronic structures

```bash
sbatch scripts/DeepH_E3/model_inference/run_eval_band.sh
```

---

## Notes

- The fine-tuned CHGNet and trained DeepH-E3 models in this repository are specifically for MoS2 systems (monolayer and nanotubes).
- Please refer to the paper for details about the research.
---

## Citation

If you use this code or dataset, please cite:

> An Atlas of Chirality-Dependent Electronic Structures of MoS2 Nanotubes from Deep Learning
> (Citation need to update)

---

## Contact

For any questions, contributions and collaborations, please contact:

**Ju Huang** ([huangju33@gmail.com](mailto:huangju33@gmail.com))

**Wenbin Li** ([liwenbin@westlake.edu.cn](mailto:liwenbin@westlake.edu.cn))

---
