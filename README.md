# Pro Medicus DevOps Technical Interview

Welcome to the DevOps Technical Interview Code Challenge!

In this challenge, you'll be tasked with solving problems that assess your understanding of core DevOps
concepts. You'll work with tools commonly used in modern DevOps practices, so be prepared to showcase your skills.

This challenge should only take a couple of hours to complete. Best of luck, and we look forward to seeing how you apply
your DevOps expertise!

## Required Software

* [`docker`](https://www.docker.com/)
* [`python3.12`](https://www.python.org/downloads/)

### Install Dependencies

You can install the required dependencies using [`poetry`](https://python-poetry.org/) or `pip`.

## Instructions

* clone repository
* create new branch from master to work on
* make changes to `server.py`
* build the api server container with the `Dockerfile`
* run the container exposing port 8081
* make changes to `client.py`

## Requirements

For this task you will need to make changes to an API server to add new functionality. Once the changes to the API
server have been made; you will then need to update the client to support the changes.

While you are making changes to the code base; please also

* simplify any code
* fix any bugs (hint there is at least 1 critical bug)

### `server.py`

* Add a new route `POST /{language}` to the API which supports 1 argument - which will add a new languages
  to `PROGRAMMING_LANGUAGES`
* Update the code to count the number of times each language is requested via the `GET /{language}` route
* Add a new route `GET /stats` which will return all languages as well as the number of times they have been requested

### `client.py`

* add a new command `add` which supports 1 argument that will call the `POST /{language}` route and add a language to
  the API server
* add a new command `top3` which will call the `GET /stats` route and print out the 3 most requested languages

## Rules

* cannot add any new packages
