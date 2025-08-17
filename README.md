# Running LLMs on Your PC

This repository contains everything you need to run **Large Language Models (LLMs)** locally on your PC, either on **CPU** or **GPU**. The guide covers setting up the environment, required dependencies, and example scripts for TinyLlama, along with tips to optimize performance.

---

## Table of Contents

1. [The Backstory](#the-backstory)
2. [What This Repo Covers](#what-this-repo-covers)
3. [Environment Setup](#environment-setup)
4. [Running on CPU](#running-on-cpu)
5. [Running on GPU](#running-on-gpu)
6. [Tips & Tricks](#tips--tricks)
7. [License](#license)

---

## The Backstory

While building an **Agentic AI project**, I ran into limitations with API keys while testing multiple bots. That’s when I realized: why not run **LLMs locally**? This repo shares the exact steps I followed to get LLMs like TinyLlama running on my own machine.

---

## What This Repo Covers

* Understanding the core components of LLMs.
* Setting up a clean environment (CPU or GPU).
* Installing required libraries.
* Running LLMs locally with example scripts.
* Tips for improving performance on CPU or GPU.

---

## Environment Setup

* **CPU users**: Python + pip is enough for smaller models.
* **GPU users**: Ensure you have **CUDA** installed and PyTorch with GPU support.
* Recommended libraries include:

**CPU Essentials:**
`torch`, `transformers`, `accelerate`, `auto-gptq`, `peft`, `datasets`, `sentencepiece`

**GPU Extras:**
`torchvision`, `torchaudio`, `bitsandbytes`, `onnxruntime-gpu`

> Tip: You can install everything in one go using a `requirements.txt` or your preferred environment manager.

---

## Running on CPU

* Use the **TinyLlama 1.1B model** for testing.
* CPU works fine for small models but is slower than GPU.
* Example script: [cpu\_chat.py](./cpu_chat.py)

**Tips:**

* Reduce `max_new_tokens` to speed up response.
* Use quantized models (`auto_gptq`) to save memory.

---

## Running on GPU

* GPU dramatically improves speed and allows larger models.
* Example script: [gpu\_chat.py](./gpu_chat.py)

**Tips:**

* Use `bitsandbytes` for 4-bit/8-bit quantized models.
* Check `torch.cuda.is_available()` to ensure your GPU is recognized.
* Adjust `torch_dtype` and `device_map` for optimal VRAM usage.

---

## Tips & Tricks

* Start small: experiment on CPU first, then switch to GPU.
* Quantized models reduce memory and increase inference speed.
* Keep conversation history for context in chat-based models.

---

## License

This project is open-source. Feel free to **fork, experiment, and contribute**.

"# Running_LLms_on_Pc" 
