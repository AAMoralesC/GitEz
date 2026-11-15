import unittest
import sys
import os

# Add src/ to PYTHONPATH so we can import git_ez
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from git_ez.main import generate_suggestions, extract_ticket_from_branch

class TestGitEzSuggestions(unittest.TestCase):
    def test_only_docs_no_ticket(self):
        files = ["README.md"]
        suggestions = generate_suggestions(files, "")
        self.assertIn("docs: actualizar documentación (README.md)", suggestions)
        self.assertIn("feat: actualizar README.md", suggestions)
        self.assertIn("fix: resolver problema en README.md", suggestions)

    def test_only_docs_with_ticket(self):
        files = ["README.md"]
        suggestions = generate_suggestions(files, "ABC-123")
        self.assertIn("docs: [ABC-123] actualizar documentación (README.md)", suggestions)

    def test_has_tests(self):
        files = ["src/git_ez/main.py", "tests/test_main.py"]
        suggestions = generate_suggestions(files, "ABC-123")
        self.assertIn("test: [ABC-123] agregar o actualizar pruebas unitarias", suggestions)

    def test_has_config(self):
        files = ["pyproject.toml"]
        suggestions = generate_suggestions(files, "")
        self.assertIn("chore: actualizar dependencias y configuración del proyecto", suggestions)

    def test_multiple_generic_files(self):
        files = ["src/a.py", "src/b.py", "src/c.py", "src/d.py"]
        suggestions = generate_suggestions(files, "XYZ-99")
        expected_feat = "feat: [XYZ-99] actualizar a.py, b.py y 2 más"
        self.assertIn(expected_feat, suggestions)

    def test_no_files_returns_empty(self):
        self.assertEqual(generate_suggestions([], "ABC-123"), [])

class TestTicketExtraction(unittest.TestCase):
    def test_ticket_found(self):
        self.assertEqual(extract_ticket_from_branch("feature/PROJ-42-login"), "PROJ-42")

    def test_ticket_is_uppercased(self):
        self.assertEqual(extract_ticket_from_branch("fix/abc-7"), "ABC-7")

    def test_branch_without_ticket(self):
        self.assertEqual(extract_ticket_from_branch("main"), "")
        self.assertEqual(extract_ticket_from_branch(""), "")

if __name__ == "__main__":
    unittest.main()
