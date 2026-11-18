# Student Task Manager Lab Report

## 1. Git and GitHub

Git is the version-control program on my computer. It records changes and lets me work with branches. GitHub is an online service that hosts Git repositories and adds collaboration features such as pull requests, issues, and Actions.

## 2. Adding, committing, and pushing changes

I use `git add` to stage selected changes, `git commit` to save a local snapshot with a message, and `git push` to send commits to the matching branch on GitHub. For example:

```shell
git add README.md
git commit -m "Update project documentation"
git push
```

## 3. Branches and pull requests

A branch lets me work on a feature without changing another branch while I am developing it. A pull request lets people review the changes and test them before they are merged into the main branch.

## 4. Merge conflict and resolution

For the conflict exercise, both `conflict/branch-one` and `conflict/branch-two` started from the same `Project status: Planning` line. The first branch changed it to `Project status: In Progress`, and the second changed it to `Project status: Completed`. After merging the first branch into `main`, Git could not automatically choose between the different edits to the same line and marked a real conflict in `README.md`. I resolved it by keeping `Project status: Completed`, removing Git's conflict markers, and preserving the surrounding README content.

## 5. `git fetch` and `git pull`

`git fetch` downloads new remote commits and references without changing my current branch. `git pull` fetches and then integrates the remote branch into the current branch, usually by merging or rebasing.

## 6. Merge and rebase

Merge combines histories and can create a merge commit, preserving how branches came together. Rebase replays commits on top of another base and makes a more linear history; it changes commit identities, so it needs extra care on branches shared with others.

## 7. GitHub Issues and GitHub Actions

GitHub Issues are online records for tasks, bugs, and questions. GitHub Actions runs automated jobs in response to repository events, such as running tests when code is pushed or a pull request is opened.

## 8. Difficulty and solution

The task-completion method had an indentation error, so the module could not be imported. I corrected the indentation, added tests for task operations and invalid input, and ran the test suite successfully.

## Work completed locally

- Fixed task completion and deletion ID validation and added six passing `unittest` cases.
- Added the README, user guide, and Python test workflow.
- Created two meaningful commits on `feature/complete-task` and pushed that branch.
- Pushed the conflict exercise baseline and both conflict branches. The conflict was produced by Git during an actual merge and then resolved as described above.

The pull requests, Issues, Actions runs, GitHub Release, and screenshot evidence should only be reported as completed after they are actually created, run, published, or captured on GitHub/the local machine.
