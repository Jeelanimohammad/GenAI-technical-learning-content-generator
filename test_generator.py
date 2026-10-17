"""
Automated Test Suite for GenAI-Based Technical Learning Content Generator.
Tests:
1. Valid Python topic generation
2. Valid SQL topic generation
3. Different difficulty levels (Beginner, Intermediate, Advanced)
4. Empty topic and invalid input handling
5. Content type filtering
6. Model loading and error fallback
7. Python code syntax validation (AST parser)
8. Content export formatting (Markdown, Text, JSON)
"""

import unittest
import json
from generator import ContentGenerator
from utils import (
    validate_inputs,
    validate_python_code,
    format_as_markdown,
    format_as_text,
    export_as_json
)
from knowledge_base import get_curated_pack


class TestLearningContentGenerator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Initialize generator once for test suite."""
        cls.generator = ContentGenerator(model_name="google/flan-t5-small")
        cls.loaded, cls.msg = cls.generator.load_model()

    def test_model_loading(self):
        """Test model initialization."""
        self.assertTrue(self.loaded, f"Model failed to load: {self.msg}")
        self.assertIsNotNone(self.generator.model)
        self.assertIsNotNone(self.generator.tokenizer)

    def test_input_validation_empty_topic(self):
        """Test empty topic input is rejected with clear error."""
        is_valid, msg = validate_inputs("Python", "", "Beginner")
        self.assertFalse(is_valid)
        self.assertIn("cannot be empty", msg)

        is_valid, msg = validate_inputs("Python", "   ", "Beginner")
        self.assertFalse(is_valid)
        self.assertIn("cannot be empty", msg)

    def test_input_validation_invalid_difficulty(self):
        """Test invalid difficulty rejection."""
        is_valid, msg = validate_inputs("Python", "Lists", "Expert")
        self.assertFalse(is_valid)
        self.assertIn("Invalid difficulty level", msg)

    def test_valid_python_topic(self):
        """Test valid Python topic generation."""
        pack = self.generator.generate_learning_pack(
            subject="Python",
            topic="List Comprehensions",
            difficulty="Beginner",
            content_type="Complete learning pack"
        )
        self.assertIn("definition", pack)
        self.assertIn("code", pack)
        self.assertIn("mcq", pack)
        self.assertIn("summary", pack)
        self.assertEqual(pack["mcq"]["correct_answer"], "B")

        # Test AST Python code validation
        is_valid, val_msg = validate_python_code(pack["code"])
        self.assertTrue(is_valid, f"Python code syntax invalid: {val_msg}")

    def test_valid_sql_topic(self):
        """Test valid SQL topic generation."""
        pack = self.generator.generate_learning_pack(
            subject="SQL",
            topic="Joins",
            difficulty="Beginner",
            content_type="Complete learning pack"
        )
        self.assertIn("definition", pack)
        self.assertIn("code", pack)
        self.assertIn("INNER JOIN", pack["code"])
        self.assertIn("LEFT JOIN", pack["code"])
        self.assertEqual(pack["mcq"]["correct_answer"], "C")

    def test_difficulty_levels(self):
        """Test Beginner, Intermediate, and Advanced tiers for Python."""
        for level in ["Beginner", "Intermediate", "Advanced"]:
            pack = self.generator.generate_learning_pack(
                subject="Python",
                topic="List Comprehensions",
                difficulty=level,
                content_type="Complete learning pack"
            )
            self.assertIsNotNone(pack.get("definition"))
            self.assertIsNotNone(pack.get("code"))

    def test_content_type_filtering(self):
        """Test that selecting individual content types returns only requested components."""
        # Only Code example
        code_pack = self.generator.generate_learning_pack(
            subject="Python",
            topic="List Comprehensions",
            difficulty="Beginner",
            content_type="Code example"
        )
        self.assertIn("code", code_pack)
        self.assertNotIn("mcq", code_pack)
        self.assertNotIn("summary", code_pack)

        # Only Practice questions
        quiz_pack = self.generator.generate_learning_pack(
            subject="Python",
            topic="List Comprehensions",
            difficulty="Beginner",
            content_type="Practice questions"
        )
        self.assertIn("mcq", quiz_pack)
        self.assertNotIn("code", quiz_pack)
        self.assertNotIn("definition", quiz_pack)

    def test_code_syntax_validator(self):
        """Test Python code syntax validator with valid and invalid code."""
        valid_code = "def add(a, b):\n    return a + b\n"
        is_valid, msg = validate_python_code(valid_code)
        self.assertTrue(is_valid)

        invalid_code = "def broken(:\n    return 42"
        is_valid, msg = validate_python_code(invalid_code)
        self.assertFalse(is_valid)
        self.assertIn("Syntax Error", msg)

    def test_exports(self):
        """Test Markdown, Text, and JSON formatting functions."""
        sample_pack = {
            "definition": "A test definition.",
            "how_it_works": "Test mechanism.",
            "code": "print('hello world')",
            "mcq": {
                "question": "What is 1+1?",
                "options": ["A) 1", "B) 2", "C) 3", "D) 4"],
                "correct_answer": "B",
                "explanation": "1+1=2."
            },
            "summary": ["Takeaway 1", "Takeaway 2"]
        }

        # Test Markdown
        md = format_as_markdown(sample_pack, "Sample Topic", "Python", "Beginner")
        self.assertIn("# Technical Learning Pack: Sample Topic", md)
        self.assertIn("```python", md)

        # Test Text
        txt = format_as_text(sample_pack, "Sample Topic", "Python", "Beginner")
        self.assertIn("TECHNICAL LEARNING PACK", txt)

        # Test JSON
        json_str = export_as_json(sample_pack, "Sample Topic", "Python", "Beginner")
        parsed = json.loads(json_str)
        self.assertEqual(parsed["metadata"]["topic"], "Sample Topic")
        self.assertEqual(parsed["content"]["definition"], "A test definition.")


if __name__ == "__main__":
    unittest.main()
