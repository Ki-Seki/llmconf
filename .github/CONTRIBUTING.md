# Contributing

We appreciate your interest in contributing. To ensure a smooth collaboration, please review the following guidelines.

## How to Contribute

1. Get the latest version of the repository:
    - For the first time: Fork the repository. Clone the forked repository to your local machine.
    - For the second time: Sync your fork with the main repository.
2. Create a new branch for your changes:
    ```bash
    git checkout -b feature/new-feature
    ```
3. Automatic linting and formatting
   1. Install Poetry at https://python-poetry.org/docs/#installation
   2. Install the dependencies:
       ```bash
       poetry install -G dev
       ```
   3. Install pre-commit hooks:
       ```bash
       poetry run pre-commit install
       ```
4. Make your changes
5. Run unittests
    ```bash
    poetry install -G test
    poetry run pytest tests/
    ```
6. Commit changes
    ```bash
    git commit -m "feat: add new feature"
    ```
7. Push your changes to your fork
    ```bash
    git push origin feature/new-feature
    ```
8. Open a pull request to the main repository on the `main` branch
