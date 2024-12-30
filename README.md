# CMSTask
This is a simple Content Management System (CMS) built with Flask and SQLite that allows users to manage words and phrases. It supports loading initial data from a JSON file, viewing and searching words, editing their details, and deleting them.

## Features

- **Load Initial Data**: Loads words and phrases from a provided JSON file at the start if the database is empty.
- **Search and Filter**: Allows users to filter words and phrases by keyword.
- **Edit Words and Phrases**: Users can edit the word, translation, and example sentence for each entry.
- **Delete Words and Phrases**: Users can delete any word or phrase from the database.

## Installation

1. Clone the repository:

    
    git clone https://github.com/bachkaaaaa/CMSTask.git


    cd CMSTask
    

2. Create a virtual environment:

    
    python3 -m venv venv
    

3. Activate the virtual environment:

    - For Windows:
    
        
        .\venv\Scripts\activate
        

    - For macOS/Linux:
    
        source venv/bin/activate
        

4. Install dependencies:

    pip install -r requirements.txt

## Database Setup

1. **Create the database**: Run the following Python code to create the database and the required tables:
 # Use this in Terminal 
  flask shell   

# Then copy following commands in the shell  
  from app import db
  
  db.create_all()  
    

## Usage

1. **Start the application**: Run the Flask application:

   python3 run.py

2. Visit `http://127.0.0.1:5000` in your web browser to access the CMS.
