
# SQL Alchemy ORM

This project demonstrates the setup and use of SQLAlchemy ORM in a Python application, using Poetry for dependency management and SQLite as the database. It is designed to showcase a clean architecture for Python applications, separating database configuration, models, and CRUD operations for better maintainability and scalability.

## Project Details

- **Project Name**: SQL Alchemy ORM
- **Author**: Khursheed Gaddi
- **Version**: 1.0.0
- **License**: MIT

## 1. Setup of Poetry

Poetry is used as the dependency manager for this project. It simplifies managing dependencies and virtual environments.

### Steps to install Poetry

First, install Poetry if you don’t have it:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Alternatively, you can follow the [official installation guide](https://python-poetry.org/docs/#installation) for other methods.

### Initialize the project

To set up the project with Poetry, use the following command in the project directory:

```bash
poetry init
```

This will prompt you to define the project details. Here is a quick setup:

- **Package Name**: `sqlalchemy_orm`
- **Version**: `1.0.0`
- **Description**: A Python project showcasing SQLAlchemy ORM with Poetry and SQLite
- **Author**: `Khursheed Gaddi <your-email@example.com>`
- **License**: `MIT`
- **Dependencies**: `SQLAlchemy`

Once initialized, install the dependencies:

```bash
poetry install
```

## 2. Manage All Packages within a File

You can manage all project dependencies in the `pyproject.toml` file that Poetry generates when you initialize the project.

To add a new package, use the following command:

```bash
poetry add <package-name>
```

For example, to add `SQLAlchemy`:

```bash
poetry add sqlalchemy
```

This will automatically update the `pyproject.toml` file. You can see the list of dependencies in this file under the `[tool.poetry.dependencies]` section.

### Activating the Virtual Environment

Once the environment is set up, you can activate the virtual environment by running:

```bash
poetry shell
```

If you need to run commands without activating the shell, you can prefix them with `poetry run`:

```bash
poetry run python script.py
```

## 3. Project Run Guide

### 1. Clone the Repository

Clone the project repository from GitHub:

```bash
git clone https://github.com/khursheed33/sql-alchemy-orm.git
cd sql-alchemy-orm
```

### 2. Install Dependencies

Once inside the project directory, run the following command to install all the dependencies:

```bash
poetry install
```

This will install all the necessary packages defined in `pyproject.toml` and set up a virtual environment.

### 3. Running the Project

To run the project, use the following commands:

```bash
poetry shell  # To activate the virtual environment
python sqlalchemy_project/main.py  # Run the main file
```

This will execute the example code and demonstrate CRUD operations with SQLAlchemy.

### 4. Testing the Database

After running the project, a SQLite database file (`test.db`) will be created in the project directory. You can inspect this database using any SQLite client or directly via the command line.

---

## Examples

After running the project, you can expect the following output:

```plaintext
Created User: Khursheed, khursheed@example.com
User: Khursheed, khursheed@example.com
Item: Item 1, First item description
Item: Item 2, Second item description
```

### Additional Examples

1. **Creating a User**

   You can create a new user using the following function in the code:

   ```python
   create_user(db, name="Alice", email="alice@example.com")
   ```

   Expected Output:
   ```plaintext
   Created User: Alice, alice@example.com
   ```

2. **Adding Items for a User**

   To add items for a specific user:

   ```python
   create_item_for_user(db, title="Task 1", description="Complete the report", user_id=user.id)
   ```

   Expected Output:
   ```plaintext
   Item: Task 1, Complete the report
   ```

3. **Fetching Items for a User**

   You can retrieve all items associated with a user:

   ```python
   items = get_items_for_user(db, user_id=user.id)
   ```

   Expected Output:
   ```plaintext
   Item: Task 1, Complete the report
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
