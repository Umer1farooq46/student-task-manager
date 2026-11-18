import unittest

from app.tasks import TaskManager


class TestAddTask(unittest.TestCase):
    def test_add_task_trims_title_and_assigns_incrementing_ids(self):
        manager = TaskManager()

        first = manager.add_task("  Study Git  ")
        second = manager.add_task("Write tests")

        self.assertEqual(first["title"], "Study Git")
        self.assertEqual(first["id"], 1)
        self.assertEqual(second["id"], 2)

    def test_add_task_rejects_empty_and_non_string_titles(self):
        manager = TaskManager()

        for title in ("", "   ", None, 42):
            with self.subTest(title=title):
                with self.assertRaises(ValueError):
                    manager.add_task(title)

        self.assertEqual(manager.display_tasks(), [])


if __name__ == "__main__":
    unittest.main()
