# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API in Python with the FastAPI framework. You will create endpoints that read and change data and test them in the browser with the built in docs page.

## 📝 Tasks

### 🛠️	Create Your First Endpoint

#### Description
Set up a FastAPI app and add a simple endpoint that returns a welcome message as JSON.

#### Requirements
Completed program should:

- Create a FastAPI app object in `main.py`
- Add a `GET /` endpoint that returns `{"message": "Welcome to the Book API"}`
- Run with `uvicorn main:app --reload` and open `/docs` to try the endpoint


### 🛠️	Build a Book Collection API

#### Description
Store a list of books in memory and add endpoints to list, view and add books.

#### Requirements
Completed program should:

- Add a `GET /books` endpoint that returns all books
- Add a `GET /books/{book_id}` endpoint that returns one book or a 404 error if it does not exist
- Add a `POST /books` endpoint that adds a new book with a title and an author
- Use a Pydantic model to validate the book data

Example request:

```json
POST /books
{"title": "The Hobbit", "author": "J.R.R. Tolkien"}
```


### 🛠️	Update and Delete Books (Stretch Goal)

#### Description
Finish the API by letting users change and remove books.

#### Requirements
Completed program should:

- Add a `PUT /books/{book_id}` endpoint that updates a book
- Add a `DELETE /books/{book_id}` endpoint that removes a book
- Return a 404 error when the book does not exist
