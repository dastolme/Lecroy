# Lecroy Project

This repository contains code for interacting with a Lecroy scope.

## Files

- `lecroy_module.py`: Module for Lecroy scope interaction.
- `lecroy_start.py`: Code to start data taking with the scope.
- `lecroy_finish.py`: Code to finish data taking with the scope.

## Scope Interaction

The code in this repository is designed to interact with a Lecroy scope for data acquisition.

- `lecroy_start.py`: Use this script in the Midas sequencer to start data taking.
- `lecroy_finish.py`: Use this script in the Midas sequencer to finish data taking.

## Linking to Local Repository

To link this GitHub repository with your local repository, follow these steps:

```bash
# Initialize a new Git repository in your local folder
git init

# Add the GitHub repository as the remote origin
git remote add origin https://github.com/your-username/Lecroy.git

# Fetch the content from the remote repository
git fetch

# Set up the main branch to track the remote main branch
git branch -u origin/main main