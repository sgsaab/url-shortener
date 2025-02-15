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

`docker-compose build` — Builds the docker container

`docker-compose up` — Starts the docker container

Then, go to [localhost:3000](http://localhost:3000/) to try out the endpoint!

### Running tests

`docker-compose exec fastapi pytest tests/ -v` — Runs all tests

`docker-compose exec fastapi pytest tests/test_api.py -v` - Runs specific test file
