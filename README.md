# Project Details

**Project Name**: URL Shortener
**Project Description**:

A URL shortener is a tool that converts a long URL into a shorter, more
manageable link that redirects to the original URL when clicked.

This project is a simple URL shortener which handles the following:

- Shortening a URL: Given a long URL, the application generates
  a shortened version of the URL.
- Expanding a URL: Given a shortened URL, the application
  redirects the user to the original long URL when the shortened URL is
  accessed.
- Analytics: The application tracks the number of times each
  shortened URL is accessed (clicks).

# Design Choices

## Project Structure

├── app/
│ ├── config.py # Application configuration
│ ├── crud.py # Database operations
│ ├── database.py
│ ├── exceptions.py
│ ├── main.py # FastAPI application and routes
│ ├── models.py # Database models
│ └── schemas.py # Pydantic models for validation
├── tests/
│ ├── test_api.py # API endpoint tests
│ └── test_crud.py # Database operation tests
├── docker-compose.yml
├── Dockerfile
└── requirements.txt

# How to

## How to setup and run

Once cloned:

### Setup REPL from root directory

`npm install` — Installs node_modules folder for dependencies

`npx playwright install` — Installs everything needed to run PlayWright

`npm install @clerk/clerk-react` — Installs everything needed for clerk authentication

`npm install react-router-dom` — Installs everything needed for react routing

### Running Frontend

`npm start` — This starts a local server at port 8000 that compiles your code in real time. TODO explain

### Running Backend

`node server\src\main\java\edu.brown.cs.student.main\server\Server.java` — This starts a local server at port 3232 that mocks a very simple backend with one static JSON output. Once it is run, feel free to visit 'http://localhost:3232' to see what gets returned. TODO explain

_You may have to open multiple terminals to run the frontend and backend simultaneously_

### Running tests

`docker-compose exec fastapi pytest tests/ -v` — Runs all tests

`docker-compose exec fastapi pytest tests/test_api.py -v` - Runs specific test file

### Running the backend Server

- Open the repl as a project in IntelliJ (nagivate to the pom.xml file to open)
- Switch to the Server.java file
- run it using the IntelliJ IDE.
- Click the local host link provided
- Enter the url to make load, view, and search requests (examples can be found in handler files)

# Collaboration

**Collaborators**:
OpenAI. (2023). ChatGPT (September 24 version) [Large language model].
https://chat.openai.com/chat/  
ChatGPT was used to brainstorm test ideas and check our Typescript syntax.  
Also used heavily for help with dropdown size adjustments based on items in them

[Stack Overflow](https://stackoverflow.com/questions/58772186/can-i-exclude-an-individual-test-from-beforeeach-in-junit5)
We used stackoverflow to research excluding specific tests from before each statements.

Livecode and gearup both used to help structure and write code.
