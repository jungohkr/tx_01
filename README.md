# New Project

This project is a web application built using Flask and PostgreSQL, featuring user authentication, session management with Redis, and row-level security for enhanced data protection.

## Project Structure

```
new_project
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   └── static
│       ├── css
│       │   └── style.css
│       ├── js
│       │   └── app.js
│       └── images
├── migrations
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── config.py
├── README.md
└── setup.sql
```

## Features

- User registration and login functionality.
- Session management using Redis.
- Row-level security in PostgreSQL to restrict data access based on user roles.
- Responsive design with a clean user interface.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd new_project
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your database connection details and secret keys.

5. **Initialize the database:**
   Run the SQL commands in `setup.sql` to set up the initial database schema.

6. **Run the application:**
   ```
   flask run
   ```

## Usage

- Navigate to `/register` to create a new account.
- Use `/login` to access your account.
- After logging in, you will be redirected to your dashboard at `/dashboard`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.