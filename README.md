# Student Task Manager

A small Python console application for managing student tasks in memory.

## Features
- Add tasks after validating that the title is not empty.
- Display tasks and their pending/completed status.
- Complete or delete a task by its ID.
- Handle invalid task IDs and menu input without exiting unexpectedly.

## Requirements
- Python 3.13 or later.
- Git (only needed to clone the repository).

## Setup

Clone the repository and enter its directory:

```shell
git clone https://github.com/Umer1farooq46/student-task-manager.git
cd student-task-manager
```

There are no third-party Python dependencies to install.

## Usage

Start the console application:

```shell
python main.py
```

Choose an option from the menu and follow the prompts. Tasks are stored in memory and are cleared when the application exits.

## Testing

Run the unit tests with Python's built-in `unittest` runner:

```shell
python -m unittest discover -s tests -v
```

## User guide

See [docs/user-guide.md](docs/user-guide.md) for step-by-step instructions.

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE).
