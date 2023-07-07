# Newspaper - A Basic Django Project Example

This repository serves as a basic example of a Django project, showcasing key features and functionality. It can be used as a starting point for your own Django projects.

## 🚀 Features

- Built with Django 4.2 and Python 3.11.
- Dependencies managed using [Poetry](https://python-poetry.org/).
- [Docker](https://www.docker.com/) support.
- Advanced development environment setup using [docker-compose](https://docs.docker.com/compose/).
- Basic static files setup.
- Includes a [pre-commit](https://pre-commit.com/) setup.
- Custom login, logout and signup pages to handle user auth.
- Full CRUD functionality for articles.

## 🛠️ Setup and Installation

To set up the project locally, follow these steps:

1. Clone this repository

```bash
git clone https://github.com/daniarlert/newspaper.git
```

2. If is not already installed, install Poetry.
3. Change into the project directory.

```bash
cd newspaper
```

4. Install the project dependencies using Poetry:

```bash
poetry install
```

5. Initialize virtual environment:

```bash
poetry shell
```

6. Install `pre-commit` hooks:

```bash
pre-commit install
```

7. Run the `python manage.py runserver` or `docker-compose up -d --build` commands.
