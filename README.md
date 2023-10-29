# SalleAroundMe Back-End

## Description
SalleAroundMe Back-End is an API that serves as the backbone for the SalleAroundMe project. It provides essential functionalities for user registration and authentication, allowing users to create accounts, log in securely, and access the features of the SalleAroundMe application. The API manages user data, ensuring a seamless and secure user experience.

## Required Packages
Make sure to have Python and the following dependencies installed:

- alembic 1.12.1
- blinker 1.6.3
- click 8.1.7
- colorama 0.4.6
- Flask 3.0.0
- Flask-Cors 4.0.0
- Flask-Migrate 4.0.5
- Flask-SQLAlchemy 3.1.1
- greenlet 3.0.1
- itsdangerous 2.1.2
- Jinja2 3.1.2
- Mako 1.2.4
- MarkupSafe 2.1.3
- mysql-connector-python 8.2.0
- mysqlclient 2.2.0
- passlib 1.7.4
- pip 23.1.2
- protobuf 4.21.12
- PyMySQL 1.1.0
- setuptools 65.5.0
- SQLAlchemy 2.0.22
- typing_extensions 4.8.0
- Werkzeug 3.0.1

## Project Structure
│
├── app/
│ ├── models/
│ │ ├── init.py
│ │ ├── user.py
│ ├── routes/
│ │ ├── init.py
│ │ ├── user.py
│ └── app.py
├── README.md


## Running the Project

2. To run the Flask application, execute the following command in your terminal from the project's root directory:

```bash
python app.py
After running the command, Flask will start, and your application will be available at http://127.0.0.1:5000/ by default. You can access your Flask application in a web browser by entering that address in the URL bar.

Please note that you can modify the port and enable debug mode if needed, but avoid enabling debug mode in a production environment.
