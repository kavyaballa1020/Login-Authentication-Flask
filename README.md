# Flask Login Authentication

This repository contains a simple web application built with Flask for user login authentication. It utilizes MongoDB for storing user data and login sessions, Flask-Bcrypt for password hashing, and Flask-PyMongo for interacting with the MongoDB database.

## Features

- User registration: Users can create an account by providing their first name, last name, username, and password.
- User login: Registered users can log in using their username and password.
- Session management: User sessions are managed using Flask's session functionality.
- Password hashing: User passwords are hashed using Flask-Bcrypt before being stored in the database.
- MongoDB integration: MongoDB is used as the backend database for storing user data and login sessions.

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/flask-login-authentication.git
