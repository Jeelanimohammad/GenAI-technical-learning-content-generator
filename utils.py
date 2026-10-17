"""
Utility and validation helpers for Technical Learning Content Generator.
Handles input validation, Python code syntax checking with ast,
quiz parsing, and export formatting (Markdown, Plain Text, JSON).
"""

import ast
import json
import re
from typing import Dict, Any, Tuple, Optional


def validate_inputs(subject: str, topic: str, difficulty: str) -> Tuple[bool, str]:
    """
    Validate user inputs.
    Returns (is_valid, error_message).
    """
    if not subject or not subject.strip():
        return False, "Please select or enter a valid technical subject."
    if not topic or not topic.strip():
        return False, "Topic cannot be empty. Please enter or select a topic to continue."
    if len(topic.strip()) < 2:
        return False, "Topic name is too short. Please provide a descriptive technical topic."
    if len(topic.strip()) > 80:
        return False, "Topic name is too long. Please enter a concise concept name (under 80 characters)."
    valid_difficulties = ["Beginner", "Intermediate", "Advanced"]
    if difficulty not in valid_difficulties:
        return False, f"Invalid difficulty level. Must be one of: {', '.join(valid_difficulties)}."
    return True, ""


def validate_python_code(code_str: str) -> Tuple[bool, str]:
    """
    Validates Python code syntax using the built-in ast module.
    Returns (is_valid, status_or_error_message).
    """
    if not code_str or not code_str.strip():
        return False, "No code provided to validate."
    try:
        ast.parse(code_str)
        return True, "Code syntax verified: Valid Python syntax."
    except SyntaxError as e:
        return False, f"Syntax Error on line {e.lineno}: {e.msg}"
    except Exception as e:
        return False, f"Validation warning: {str(e)}"


def format_as_markdown(pack: Dict[str, Any], topic: str, subject: str, difficulty: str) -> str:
    """Format learning content pack into comprehensive Markdown."""
    lines = [
        f"# Technical Learning Pack: {topic}",
        f"**Subject:** {subject} | **Difficulty Level:** {difficulty} | **Generated with:** GenAI Technical Learning Assistant",
        "\n> [!WARNING]",
        "> **Educational Disclaimer:** AI-generated educational content can occasionally contain subtle errors or simplifications. Always review and test code snippets in a safe sandbox before applying in production.",
        "\n---\n"
    ]

    # Concept Explanation
    if "definition" in pack:
        lines.append(f"## 1. Concept Overview: {topic}\n")
        lines.append(f"### Definition\n{pack.get('definition', '')}\n")
        if "how_it_works" in pack:
            lines.append(f"### How It Works\n{pack.get('how_it_works', '')}\n")
        if "important_points" in pack and pack["important_points"]:
            lines.append("### Key Points & Principles")
            for pt in pack["important_points"]:
                lines.append(f"- {pt}")
            lines.append("")

    # Practical Code Example
    if "code" in pack:
        lang = "sql" if subject.lower() == "sql" else "python"
        lines.append(f"## 2. Practical Code Example ({lang.upper()})\n")
        lines.append(f"```{lang}\n{pack.get('code', '').strip()}\n```\n")
        if "code_explanation" in pack and pack["code_explanation"]:
            lines.append("### Step-by-Step Code Walkthrough")
            for step in pack["code_explanation"]:
                lines.append(f"- {step}")
            lines.append("")

    # Common Mistakes
    if "common_mistakes" in pack and pack["common_mistakes"]:
        lines.append("## 3. Common Pitfalls & Misconceptions\n")
        for mistake in pack["common_mistakes"]:
            lines.append(f"- ⚠️ {mistake}")
        lines.append("")

    # Practice Questions
    if "mcq" in pack or "short_question" in pack:
        lines.append("## 4. Practice & Knowledge Check\n")
        if "mcq" in pack:
            mcq = pack["mcq"]
            lines.append(f"### Multiple Choice Question\n**{mcq.get('question', '')}**\n")
            for opt in mcq.get("options", []):
                lines.append(f"- {opt}")
            lines.append(f"\n**Correct Answer:** Option {mcq.get('correct_answer', '')}")
            lines.append(f"**Explanation:** {mcq.get('explanation', '')}\n")
        if "short_question" in pack:
            sq = pack["short_question"]
            lines.append(f"### Conceptual Question\n**Q: {sq.get('question', '')}**\n")
            lines.append(f"**Answer:** {sq.get('answer', '')}\n")

    # Learning Summary
    if "summary" in pack and pack["summary"]:
        lines.append("## 5. Revision Summary & Key Takeaways\n")
        for item in pack["summary"]:
            lines.append(f"- 💡 {item}")
        lines.append("")

    return "\n".join(lines)


def format_as_text(pack: Dict[str, Any], topic: str, subject: str, difficulty: str) -> str:
    """Format learning content pack into clean plain text."""
    lines = [
        f"TECHNICAL LEARNING PACK: {topic.upper()}",
        f"Subject: {subject} | Level: {difficulty}",
        "=" * 60,
        "DISCLAIMER: AI-generated content. Please verify code before use.",
        "=" * 60,
        ""
    ]

    if "definition" in pack:
        lines.extend([
            "[1] CONCEPT OVERVIEW",
            f"Definition: {pack.get('definition', '')}",
            "",
            f"How It Works: {pack.get('how_it_works', '')}",
            ""
        ])
        if "important_points" in pack:
            lines.append("Key Points:")
            for pt in pack["important_points"]:
                lines.append(f"  * {pt}")
            lines.append("")

    if "code" in pack:
        lines.extend([
            "[2] PRACTICAL CODE EXAMPLE",
            "-" * 40,
            pack.get("code", "").strip(),
            "-" * 40,
            ""
        ])
        if "code_explanation" in pack:
            lines.append("Code Explanation:")
            for step in pack["code_explanation"]:
                lines.append(f"  * {step}")
            lines.append("")

    if "common_mistakes" in pack:
        lines.append("[3] COMMON PITFALLS")
        for m in pack["common_mistakes"]:
            lines.append(f"  * {m}")
        lines.append("")

    if "mcq" in pack:
        mcq = pack["mcq"]
        lines.extend([
            "[4] PRACTICE QUESTIONS",
            f"MCQ: {mcq.get('question', '')}"
        ])
        for opt in mcq.get("options", []):
            lines.append(f"  {opt}")
        lines.extend([
            f"Correct Answer: {mcq.get('correct_answer', '')}",
            f"Explanation: {mcq.get('explanation', '')}",
            ""
        ])

    if "short_question" in pack:
        sq = pack["short_question"]
        lines.extend([
            f"Conceptual Question: {sq.get('question', '')}",
            f"Answer: {sq.get('answer', '')}",
            ""
        ])

    if "summary" in pack:
        lines.append("[5] REVISION SUMMARY")
        for s in pack["summary"]:
            lines.append(f"  * {s}")
        lines.append("")

    return "\n".join(lines)


def export_as_json(pack: Dict[str, Any], topic: str, subject: str, difficulty: str) -> str:
    """Export complete pack structure as formatted JSON."""
    payload = {
        "metadata": {
            "topic": topic,
            "subject": subject,
            "difficulty": difficulty,
            "tool": "GenAI-Based Technical Learning Content Generator",
            "disclaimer": "AI-generated content should be verified before production use."
        },
        "content": pack
    }
    return json.dumps(payload, indent=2)
