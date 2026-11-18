import unittest

from app.tasks import TaskManager


class TestDeleteTask(unittest.TestCase):
    def test_deleting_one_task_preserves_other_tasks_and_ids(self):
        manager = TaskManager()
        first = manager.add_task("Keep first")
        deleted = manager.add_task("Delete this one")
        last = manager.add_task("Keep last")

        self.assertTrue(manager.delete_task(deleted["id"]))
        self.assertEqual(manager.display_tasks(), [first, last])

        next_task = manager.add_task("Add another")
        self.assertEqual(next_task["id"], 4)

    def test_deleting_invalid_id_leaves_tasks_unchanged(self):
        manager = TaskManager()
        task = manager.add_task("Keep this task")

        for invalid_id in (0, -1, 2, "1", True):
            with self.subTest(task_id=invalid_id):
                self.assertFalse(manager.delete_task(invalid_id))
                self.assertEqual(manager.display_tasks(), [task])


if __name__ == "__main__":
    unittest.main()
