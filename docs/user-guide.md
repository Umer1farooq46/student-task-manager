# Student Task Manager User Guide

## Start the application

Open a terminal in the project directory and run:

```shell
python main.py
```

The menu remains available until you choose **5. Exit**. Tasks are held in memory, so they do not persist after the program exits.

## Add a task

Choose **1. Add Task** and enter a title. A title containing only spaces is rejected; valid titles are trimmed before they are saved.

## View tasks

Choose **2. Display Tasks**. Each task is shown with its ID, title, and either Pending or Completed status. If the list is empty, the application says that no tasks are available.

## Complete a task

Choose **3. Complete Task** and enter the task's numeric ID. The application marks an existing task as completed and reports an invalid ID if it cannot find that task.

## Delete a task

Choose **4. Delete Task** and enter the task's numeric ID. The application removes an existing task and reports an invalid ID if it cannot find that task.

For either task-ID prompt, enter a valid positive integer. Invalid input is reported and the menu continues.
