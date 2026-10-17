# 🧠 GenAI-Based Technical Learning Content Generator

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.14-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.56.0-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![HuggingFace Transformers](https://img.shields.io/badge/%F0%9F%A4%97%20Transformers-5.5.3-yellow)](https://huggingface.co/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.11.0%2Bcpu-EE4C2C.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)

An interactive Generative AI application that generates customized technical learning content—including core concepts, practical code examples, interactive quizzes with answer validation, and revision summaries—using open-source language models without paid APIs or external keys.

---

## 📸 Application Preview

![GenAI Technical Learning Content Generator](assets/screenshot.png)

---

## 📌 Project Overview

Learning technical computer science concepts often requires juggling textbooks, code repositories, question banks, and notes. 

The **GenAI Technical Learning Content Generator** provides an all-in-one platform to generate structured, difficulty-adapted technical learning materials on demand. Built with a **Hybrid Architecture**, it combines open-source instruction-following models (`google/flan-t5-small`) with grounded domain knowledge and Python AST code verification to ensure reliable, high-quality educational content.

---

## 🎯 Features

- **Multi-Subject Domain Coverage:**
  - 🐍 **Python Programming:** List comprehensions, generators, decorators, memory scopes, concurrency.
  - 🗄️ **SQL & Databases:** Inner/Left/Self joins, aggregation, window functions, query optimization.
  - 🧩 **Object-Oriented Programming (OOP):** Polymorphism, duck typing, inheritance, abstract classes, dunder methods.
  - 🌲 **Data Structures:** Binary Search Trees, traversal orders, stacks, queues, hash tables.
  - 🤖 **Machine Learning:** Bias-Variance tradeoff, regularization (L1/L2), evaluation metrics, overfitting guards.
  - ✨ **Generative AI:** Transformers, Self-Attention mechanisms, tokenization, prompt engineering, RAG vs Fine-tuning.

- **Adaptive Difficulty Levels:**
  - **Beginner:** Clear definitions, core syntax, intuitive analogies, and baseline examples.
  - **Intermediate:** Internal mechanics, execution lifecycles, and edge case handling.
  - **Advanced:** Bytecode analysis, computational complexity, AST optimizations, and system trade-offs.

- **Automated AST Code Syntax Verification:**
  - Python code snippets are verified using Python's built-in `ast.parse` module to ensure syntax validity before display.

- **Interactive Practice Quizzes:**
  - Multiple-choice questions with selectable answers, instant evaluation, and detailed explanations.
  - Conceptual short-answer questions with revealable expert solutions.

- **Flexible Multi-Format Export:**
  - One-click downloads as **Markdown (`.md`)**, **Plain Text (`.txt`)**, and structured **JSON (`.json`)**.

- **100% Free & Open-Source:**
  - Runs locally on CPU/GPU with no paid subscriptions, OpenAI keys, or external token limits.

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    User([User / Student]) -->|Selects Subject, Topic, Level| UI[Streamlit Web Interface]
    
    subgraph Frontend [Presentation Layer - app.py]
        UI --> Sidebar[Sidebar Controls & Validation]
        UI --> Display[Tabbed Results & Interactive Quiz]
        UI --> Exporter[Download Hub - MD, TXT, JSON]
    end

    subgraph Core [Orchestration Layer - generator.py]
        Sidebar --> Validation[Input Validator - utils.py]
        Validation --> Router{Curated Topic?}
        
        Router -- Yes --> KnowledgeBase[(Knowledge Base - knowledge_base.py)]
        Router -- Custom/No --> PromptEngine[Prompt Templates - prompts.py]
        PromptEngine --> ModelInference[Transformers Pipeline - FLAN-T5]
        
        KnowledgeBase --> Synthesizer[Pack Synthesizer]
        ModelInference --> Synthesizer
        
        Synthesizer --> ASTCheck[AST Python Syntax Validator]
    end

    ASTCheck --> Display
```

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Language** | Python 3.10+ | Core application logic and data processing |
| **Web Framework** | Streamlit | Interactive, responsive web interface |
| **Model Architecture** | Google FLAN-T5-Small / Base | Open-source instruction-following Seq2Seq model |
| **ML Framework** | Hugging Face Transformers & PyTorch | Local tensor loading, tokenization, and inference |
| **Validation** | Python `ast` Standard Library | Abstract Syntax Tree code verification |
| **Data Handling** | Python standard libraries & JSON | Structured content export and serialization |

---

## 📋 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- Git installed
- Standard laptop/desktop CPU (GPU optional)

### 1. Clone the Repository
```bash
git clone https://github.com/Jeelanimohammad/GenAI-technical-learning-content-generator.git
cd GenAI-technical-learning-content-generator
```

### 2. Set Up Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501`.

---

## 🧪 Testing

The repository includes an automated test suite covering model loading, input validation, difficulty level scaling, code syntax parsing, and content export.

To run the test suite:
```bash
python -m unittest test_generator.py -v
```

**Test Suite Coverage:**
1. `test_model_loading`: Hugging Face model and tokenizer weights load into memory.
2. `test_input_validation_empty_topic`: Rejection of empty/whitespace inputs.
3. `test_input_validation_invalid_difficulty`: Schema constraint checks.
4. `test_valid_python_topic`: Complete learning pack generation for Python.
5. `test_valid_sql_topic`: SQL join queries and schema generation.
6. `test_difficulty_levels`: Beginner, Intermediate, and Advanced tiers generate distinct content.
7. `test_content_type_filtering`: Single-component isolation (Code only, Quiz only, etc.).
8. `test_code_syntax_validator`: Evaluates `ast.parse` behavior on Python code.
9. `test_exports`: Serialization validation for Markdown, Plain Text, and JSON schemas.

---

## 🔬 Model Insights & Limitations

### Model Characteristics
- **Model:** `google/flan-t5-small` (~80 Million parameters, ~308 MB footprint).
- **Inference:** Runs smoothly on CPU with less than 1 GB RAM usage.
- **Tuning:** Instruction-tuned across 1,800+ NLP tasks via Google's FLAN dataset.

### Handling Limitations
- **Token Limits:** Small seq2seq models have a 512-token context window. The application uses modular prompt decomposition rather than single-shot generation to prevent truncation.
- **Deterministic Decoding:** Uses `do_sample=False` and `repetition_penalty=1.2` to prevent infinite text loops.
- **Hallucination Safeguards:** Verified foundational concepts are backed by structured technical knowledge, while code is parsed through `ast.parse` prior to display.

---

## 📁 Repository Structure

```
GenAI-technical-learning-content-generator/
├── app.py                # Streamlit web user interface
├── generator.py          # AI model loading, inference & pack synthesis
├── prompts.py            # Modular prompt engineering templates
├── knowledge_base.py     # Multi-subject technical knowledge base
├── utils.py              # AST syntax validator, input checker & export formatters
├── test_generator.py     # Automated unit & integration test suite
├── requirements.txt      # Production project dependencies
├── .gitignore            # Git exclusions (caches, bytecode, venv)
├── assets/
│   └── screenshot.png    # Application interface preview
└── README.md             # Project documentation
```