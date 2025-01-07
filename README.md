# CMSTask

CMSTask is a simple Content Management System (CMS) built with Flask and SQLite. It allows users to manage words and phrases efficiently. The system supports loading initial data from a JSON file, viewing and searching words, editing their details, and deleting them.

## Features

- **Load Initial Data**: Automatically loads words and phrases from a JSON file if the database is empty.
- **Search and Filter**: Provides filtering options to search words and phrases by keywords.
- **Edit Words and Phrases**: Enables users to update word details, translations, and example sentences.
- **Delete Words and Phrases**: Allows users to remove any word or phrase from the database.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/bachkaaaaa/CMSTask.git
    cd CMSTask
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

1. **Create the database**:
   Open the Flask shell and run the following commands to initialize the database:

    ```bash
    flask shell
    ```

    Inside the Flask shell, execute:

    ```python
    from app import db
    db.create_all()
    ```

## Usage

1. **Start the application**:

    ```bash
    python3 run.py
    ```

2. Open your web browser and visit:

    ```
    http://127.0.0.1:5000
    ```

   Enjoy managing your words and phrases with CMSTask!

