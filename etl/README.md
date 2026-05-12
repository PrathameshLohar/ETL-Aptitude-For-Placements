---
license: apache-2.0
task_categories:
- text-generation
- question-answering
language:
- en
tags:
- aptitude
- placements
- mathematics
- logical-reasoning
- smollm2
size_categories:
- n<1K
---

# Unseen Aptitude QA Dataset

This dataset contains categorized quantitative and logical aptitude questions explicitly structured for campus placement preparation (e.g., TCS, Wipro, Infosys). It is formatted using the standard **ChatML / OpenAI Messages** schema, making it natively compatible with fine-tuning models like `SmolLM2-1.7B`.

## Dataset Structure

Each data sample contains a `messages` array featuring a structured system persona, metadata-enriched user questions, and detailed step-by-step assistant breakdowns.

### JSON Schema Example
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are an expert aptitude trainer specializing in campus placement preparation. Solve the question with a clear, step-by-step explanation and provide the final answer."
    },
    {
      "role": "user",
      "content": "Topic: Percentage\nQuestion: The price of apple is first increased by 10% and then decreased by 10%. What is the change in the price of apple?"
    },
    {
      "role": "assistant",
      "content": "Note: Percentage change = (Difference ÷ Original price) × 100\nAssume price of apple = 100\n\nIncrease by 10%\nPrice after increase = 100 + 10% of 100 = 110\n\nDecrease by 10%\nPrice after decrease = 110 − 10% of 110 = 99\n\nDifference = 100 − 99 = 1 \nPercentage change = (1 ÷ 100) × 100 = 1% ✅\n\n👍 Final Answer:\nPrice of apple decreases by 1%"
    }
  ]
}
```

## Covered Topics

The dataset provides multi-step mathematical operations across 11 core categories:
* Averages
* Number System
* Partnership
* Percentage
* Probability
* Problem on Ages
* Problems on Train
* Profit & Loss
* Ratio and Proportion
* Time and Work
* Time, Speed and Distance

## How to Load This Dataset

You can stream or download this dataset directly using the Hugging Face `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("Prathamesh25/unseen-aptitude-qa-dataset")
print(dataset["train"][0])
```
