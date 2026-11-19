"""Starter code for the Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API")


class Book(BaseModel):
    title: str
    author: str


# In-memory storage for books
books = {
    1: {"title": "Clean Code", "author": "Robert C. Martin"},
}


@app.get("/")
def root():
    # TODO: return a welcome message
    pass


# TODO: add GET /books, GET /books/{book_id} and POST /books endpoints
