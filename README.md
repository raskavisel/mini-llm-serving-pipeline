# Mini LLM Serving & Retraining Pipeline

**End-to-end lightweight pipeline for serving, monitoring and retraining open-source LLMs.**

## Overview

This project demonstrates a **production-inspired framework** for managing large language models (LLMs) in a compact and versatile setup. The system:

- Serves a **mini LLM** using FastAPI.
- Tracks **inference telemetry** including latency and request statistics.
- Detects **model drift** based on performance thresholds.
- Triggers **automated retraining** when drift is detected.
- Supports **model versioning** and reproducible experiments.

This is designed to emulate modern GenAI infrastructure practices and is fully compatible with Python environments, including Android (via Pydroid) and desktop platforms.

---

## Features

| Feature                         | Description |
|---------------------------------|-------------|
| **LLM Serving**                  | Handles text input and generates responses via a mini LLM simulation. |
| **Inference Metrics**            | Logs request count, latency and average latency. |
| **Drift Detection**              | Monitors performance degradation and triggers retraining. |
| **Automated Retraining**         | Simulates retraining workflow and version logging. |
| **Cross-Platform**               | Runs on mobile (Pydroid) and desktop Python environments. |

---

## Tech Stack

- **Python 3.13**
- **FastAPI** – REST API serving the model
- **Uvicorn** – ASGI server for running FastAPI
- **MLflow** – Model experiment tracking (simulated in mobile setup)
- **Standard Python libraries** – random, time

---

## Installation & Setup

1. Clone the repository:

```bash
git clone <https://github.com/raskavisel/mini-llm-serving-pipeline>
cd mini-llm-serving-pipeline
