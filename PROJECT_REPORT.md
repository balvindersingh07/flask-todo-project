# Flask Todo Project - Git Workflow Evidence Report

## Executive Summary

This report documents the Git and GitHub workflow followed while setting up and iterating on the Flask Todo project. The screenshots capture branch creation, commits, rebasing, conflict handling, and remote pushes to GitHub.

Repository: [balvindersingh07/flask-todo-project](https://github.com/balvindersingh07/flask-todo-project)

## Workflow Timeline and Evidence

### 1) Repository clone and SSH trust prompt

The repository was cloned over SSH, and the GitHub host key was accepted.

![Clone repository and SSH verification](screenshots/c__Users_lenovo_AppData_Roaming_Cursor_User_workspaceStorage_22ab599e5d3377adc0e25d098c2684f1_images_Screenshot_2026-05-19_164917-41b8000a-c033-4025-967e-40b1922d9ecd.png)

### 2) Branch setup for feature work (`master_1`)

Feature branch `master_1` was created and verified via `git branch`.

![Create and verify master_1 branch](screenshots/c__Users_lenovo_AppData_Roaming_Cursor_User_workspaceStorage_22ab599e5d3377adc0e25d098c2684f1_images_Screenshot_2026-05-19_170517-8d8f52ee-0315-4d10-884e-7cd3434cdb76.png)

### 3) Incremental commit creation on `master_1`

Focused commits were created while evolving `todo.html` (for example: adding Item ID field).

![Commit on master_1](screenshots/c__Users_lenovo_AppData_Roaming_Cursor_User_workspaceStorage_22ab599e5d3377adc0e25d098c2684f1_images_Screenshot_2026-05-19_174319-910b23d0-ebcd-4c47-856f-b629131edf07.png)

### 4) Pushes to remote branches on GitHub

Branch pushes were successful, and GitHub confirmed tracking branches and PR URLs.

![Push master_1 and master_2 to origin](screenshots/c__Users_lenovo_AppData_Roaming_Cursor_User_workspaceStorage_22ab599e5d3377adc0e25d098c2684f1_images_Screenshot_2026-05-19_173129-311f23e2-698b-43c1-a79f-d2be2a440fbb.png)

### 5) Merge and publish from `main`

Work from feature branches was merged into `main` and then pushed upstream.

![Merge branch into main and push](screenshots/c__Users_lenovo_AppData_Roaming_Cursor_User_workspaceStorage_22ab599e5d3377adc0e25d098c2684f1_images_Screenshot_2026-05-19_175306-95307d84-839f-471f-a75d-05379102d55a.png)

### 6) Rebase conflict encountered and resolved safely

A rebase conflict occurred in `todo.html`, then the workflow resumed with `git add`, `git rebase --continue`, and a final force push after rebase completion.

![Rebase conflict and successful continuation](screenshots/c__Users_lenovo_AppData_Roaming_Cursor_User_workspaceStorage_22ab599e5d3377adc0e25d098c2684f1_images_Screenshot_2026-05-19_180131-1f7c5374-2ad3-47c7-9dbe-4c72be97c151.png)

## Key Observations

- Branch-based development was used consistently (`main`, `master_1`, `master_2`, and supporting branches).
- Commits were created incrementally rather than as a single large change.
- Remote tracking was set correctly using `git push -u`.
- A non-trivial rebase conflict was resolved without discarding work.
- Merge and push activity confirms the project history reached GitHub.

## Current Project Artifacts

Core files present in the repository include:

- `app.py` (Flask backend API logic)
- `todo.html` (frontend UI)
- `data.json` (stored todo data)
- `README.md` (project overview)
- `screenshots/` (full screenshot evidence set)
- `PROJECT_REPORT.md` (this report)

