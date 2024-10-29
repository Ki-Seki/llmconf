# Contributing

Thank you for your interest in contributing! To facilitate a smooth collaboration, please follow these guidelines.

## How to Contribute

1. **Get the Latest Version of the Repository:**
    - **First Time:** Fork the repository and clone your fork to your local machine.
    - **Subsequent Contributions:** Sync your fork with the main repository.

2. **Create a New Branch for Your Changes:**
    ```bash
    git checkout -b feature/new-feature
    ```

3. **Set Up Linting and Formatting:**
   1. Install Poetry following the instructions [here](https://python-poetry.org/docs/#installation).
   2. Install the required dependencies:
       ```bash
       poetry install -G dev
       ```
   3. Set up pre-commit hooks:
       ```bash
       poetry run pre-commit install
       ```

4. **Make Your Changes.**

5. **Run Unit Tests:**
    ```bash
    poetry install -G test
    poetry run pytest tests/
    ```

6. **Commit Your Changes:**
    ```bash
    git commit -m "feat: add new feature"
    ```

7. **Push Your Changes to Your Fork:**
    ```bash
    git push origin feature/new-feature
    ```

8. **Open a Pull Request:**
   Navigate to the main repository and create a pull request from your `feature/new-feature` branch to the `main` branch.

Thank you for contributing!
