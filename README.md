# Backend Project for Learning

## What is this?

This is a backend-only project I am building to understand how backend systems actually work.

Instead of directly using Django or FastAPI and blindly building things, I am starting from scratch using:

* Python
* OOP
* File handling (JSON as database)

Goal is to understand the flow properly before moving to frameworks.

---

## Why I am doing this

I realized that just writing code is not enough.

I was able to build things using tools, but I didn’t clearly understand:

* where the code runs
* how data flows
* how backend is structured

So this project is to fix that.

---

## Current Structure

```plaintext
backend_project/
│
├── models/        → data structure (User)
├── services/      → logic (UserService)
├── storage/       → file handling (FileHandler)
├── data/          → JSON files (acts like DB)
│
└── main.py        → entry point (CLI)
```

---

## How it works (simple flow)

```plaintext
User input (CLI)
    ↓
main.py
    ↓
UserService (logic)
    ↓
FileHandler (read/write file)
    ↓
users.json (data stored)
```

---

## What I have done (Day 1)

* Created User class (OOP)
* Built FileHandler to read/write JSON
* Built UserService for logic
* Connected everything using main.py (CLI)

Now I can:

* create user
* store user in file
* retrieve users

---

## Key things I understood

* Model → only holds data (no file logic)
* Service → handles logic (validation, operations)
* Storage → handles file/database

Everything is separated properly.

Also:

* Data is stored as list in one file (not separate file per user)
* Object → converted to dict → stored in JSON

---

## What next

* Add Task system
* Link users and tasks
* Add logging
* Later convert this into API (FastAPI / Django)

---

## Note

This project is mainly for learning backend architecture properly.

Even if it looks simple, focus is on:

* understanding flow
* clean structure
* real backend thinking
