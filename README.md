# LLM Cost Calculator

A simple tool to estimate the cost of using large language models (LLMs).

Developers building AI products often want to understand how much their prompts will cost before running large workloads.

This repository provides a simple example for estimating token usage and API costs.

---

## Why this project exists

When working with AI APIs such as:

- OpenAI
- Anthropic
- Google Gemini

developers often ask:

- How much will this prompt cost?
- How many tokens will be used?
- How can I estimate costs before scaling?

This project provides a simple starting point.

---

## Example

```python
from cost_calculator import estimate_cost

cost = estimate_cost(
    model="gpt-4",
    tokens=2000
)

print("Estimated cost:", cost)
```

---

## Example output

```
Estimated cost: $0.06
```

---

## Supported models (example)

| Model | Example Cost |
|------|------|
| GPT-4 | higher cost |
| GPT-4 mini | lower cost |
| Claude | medium cost |
| Gemini | lower cost |

Costs depend on the provider and pricing updates.

---

## Project structure

```
llm-cost-calculator
 ├ cost_calculator.py
 ├ example.py
 └ README.md
```

---

## About

This repository is an experimental developer tool exploring ideas around AI cost estimation and LLM usage.

If you find this useful, feel free to ⭐ star the repo.
