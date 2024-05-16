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
git clone https://github.com/kavyaballa1020/Oasis-Login-Authentication.git

2. **Navigate to the project directory:**

```bash
cd flask-login-authentication
```

3. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**

   - Create a `.env` file in the project root directory.
   - Define the following variables in the `.env` file:
     - `SECRET_KEY`: A secret key used for session management.
     - `MONGO_URI`: URI for connecting to your MongoDB database.

5. **Run the application:**

```bash
python app.py
```

6. **Access the application in your web browser at** `http://localhost:5000`.

## Usage

1. Register a new account by clicking on the "Register" link and providing the required information.
2. Log in using your registered username and password.
3. Upon successful login, you will be redirected to the secured page displaying your first name and last name.
4. Click on the "Logout" link to log out of your session.

## Screenshots

1. **Register Page:**

   ![Register Page](screenshots/Login%20Authentication%20-%201.PNG)

2. **Login Page:**

   ![Login Page](screenshots/Login%20Authentication%20-%202.PNG)

3. **Secured Page:**

   ![Secured Page](screenshots/Login%20Authentication%20-%203.PNG)

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```