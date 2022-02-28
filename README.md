# beach-api
A GraphQL API for rating and commenting on beaches.

## Overview
This project is an example GraphQL API project using Strawberry and Starlette to set up a simple ASGI GraphQL server with Python. It covers functionality for querying beaches with rating and comment information. It also allows users to add, delete, and edit comments on beaches as well as rate available beaches.

## GraphQL Schema
In schema.graphql is the GraphQL schema for this project. You can use http request applications such as Postman to make requests to the application with this schema structure after you spin up a local verson of the application.

## macOS Local Setup
```bash
    $ git clone git@github.com:leeamoore/beach-api.git
    $ cd beach-api
    $ brew install python@3.9
    $ brew install --cask docker
    $ docker-compose up -d
    $ pip-3.9 install poetry
    $ poetry install
    $ poetry shell
    $ python app.py
```

## Tasks
- [X] Design initial GraphQL schema.
- [X] Get initial project structure working.
- [X] Get query endpoints working.
- [ ] Get mutation endpoints working.
- [ ] Design user-specific functionality.
- [ ] Work on unit test coverage of the application.
- [ ] Review application characteristis and update design.
- [ ] Improve PostgreSQL query performance.
- [ ] Design cloud architecture.
- [ ] Cloud deployment strategy.