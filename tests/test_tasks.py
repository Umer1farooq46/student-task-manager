from contextlib import redirect_stdout
from io import StringIO
import unittest
from unittest.mock import patch

from app.tasks import TaskManager
from main import main


class TestTaskManager(unittest.TestCase):
    def test_add_task(self):
        manager = TaskManager()
        task = manager.add_task("Complete assignment")

        self.assertEqual(task["title"], "Complete assignment")
        self.assertFalse(task["completed"])

    def test_add_task_rejects_empty_title(self):
        manager = TaskManager()

        with self.assertRaises(ValueError):
            manager.add_task("   ")

    def test_complete_task(self):
        manager = TaskManager()
        task = manager.add_task("Study Git")

        result = manager.complete_task(task["id"])

        self.assertTrue(result)
        self.assertTrue(task["completed"])

    def test_delete_task(self):
        manager = TaskManager()
        task = manager.add_task("Submit project")

        result = manager.delete_task(task["id"])

        self.assertTrue(result)
        self.assertEqual(len(manager.display_tasks()), 0)

    def test_task_actions_reject_invalid_ids(self):
        manager = TaskManager()
        manager.add_task("Keep this task")

        for invalid_id in (0, -1, 2, "1", True):
            with self.subTest(task_id=invalid_id):
                self.assertFalse(manager.complete_task(invalid_id))
                self.assertFalse(manager.delete_task(invalid_id))

    def test_menu_rejects_invalid_input(self):
        output = StringIO()

        with patch("builtins.input", side_effect=["invalid", "5"]):
            with redirect_stdout(output):
                main()

        self.assertIn("Invalid choice. Please try again.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
