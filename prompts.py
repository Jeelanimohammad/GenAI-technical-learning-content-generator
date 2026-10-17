"""
Prompt templates for GenAI-Based Technical Learning Content Generator.
Provides structured prompt engineering templates designed for instruction-following models (e.g. FLAN-T5).
"""

from typing import Dict, Any


def get_definition_prompt(topic: str, subject: str, difficulty: str) -> str:
    """Prompt for concise technical definition."""
    return (
        f"Subject: {subject}\n"
        f"Topic: {topic}\n"
        f"Target Audience Level: {difficulty}\n"
        f"Task: Provide a clear, accurate 2-sentence technical definition of {topic} in the context of {subject} for a {difficulty} learner."
    )


def get_how_it_works_prompt(topic: str, subject: str, difficulty: str) -> str:
    """Prompt for explaining the underlying mechanism and how it works."""
    return (
        f"Subject: {subject}\n"
        f"Topic: {topic}\n"
        f"Level: {difficulty}\n"
        f"Task: Explain step-by-step how {topic} works internally. Mention the key mechanics and lifecycle."
    )


def get_code_prompt(topic: str, subject: str, difficulty: str) -> str:
    """Prompt for generating practical code or query."""
    lang = "SQL" if subject.lower() == "sql" else "Python"
    return (
        f"Subject: {subject}\n"
        f"Topic: {topic}\n"
        f"Language: {lang}\n"
        f"Level: {difficulty}\n"
        f"Task: Write a clean, working, idiomatic {lang} code example demonstrating {topic}. Include comments."
    )


def get_common_mistakes_prompt(topic: str, subject: str, difficulty: str) -> str:
    """Prompt for highlighting common pitfalls and misconceptions."""
    return (
        f"Subject: {subject}\n"
        f"Topic: {topic}\n"
        f"Level: {difficulty}\n"
        f"Task: List 2 common mistakes or misconceptions developers encounter when learning or using {topic}."
    )


def get_quiz_prompt(topic: str, subject: str, difficulty: str) -> str:
    """Prompt for practice questions (MCQ and short-answer)."""
    return (
        f"Subject: {subject}\n"
        f"Topic: {topic}\n"
        f"Level: {difficulty}\n"
        f"Task: Create 1 multiple-choice question (with options A, B, C, D) and 1 conceptual short-answer question about {topic}."
    )


def get_summary_prompt(topic: str, subject: str, difficulty: str) -> str:
    """Prompt for quick revision takeaways."""
    return (
        f"Subject: {subject}\n"
        f"Topic: {topic}\n"
        f"Level: {difficulty}\n"
        f"Task: Provide a 3-bullet revision summary of {topic} emphasizing the most important takeaways."
    )
