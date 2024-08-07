# Student Management System API

This is a Flask-based API for managing student information and their academic data. It includes functionalities for student login, viewing personal details, updating account information, viewing course details, checking results, and logging out.

## Table of Contents

- [Student Management System API](#student-management-system-api)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Database Setup](#database-setup)
  - [API Endpoints](#api-endpoints)
    - [Login](#login)
    - [Home](#home)
    - [Account](#account)
    - [Courses](#courses)
    - [Results](#results)
    - [Evaluation](#evaluation)
    - [Logout](#logout)
  - [Token Revocation](#token-revocation)
  - [Error Handling](#error-handling)
  - [Dependencies](#dependencies)
  - [Running the Application](#running-the-application)
  - [Author](#author)

## Features

- Student login with JWT authentication.
- Viewing student personal details.
- Updating student account information.
- Viewing course details.
- Viewing student results.
- Secure logout with token revocation.

## Installation

1. Clone the repository:
    ```
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

## Configuration

Update the configuration settings in the script as needed:

```python
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
```

## API Endpoints

### Login

**URL:** `/`

**Method:** `POST`

**Description:** Authenticates the student and returns a JWT access token.

**Request Body:**

```
{
    "username": "student_id",
    "password": "password"
}
```

**Response:**

```
{
    "access_token": "jwt_access_token"
}
```

### Home

**URL:** `/home`

**Method:** `GET`

**Description:** Retrieves basic personal information of the logged-in student.

**Headers:**

```
Authorization: Bearer <jwt_access_token>
```

**Response:**

```
{
    "first_name": "John",
    "last_name": "Doe",
    "other_name": "A.",
    "student_email": "john.doe@example.com",
    "gender": "Male"
}
```

### Account

**URL:** `/account`

**Methods:** `GET`, `POST`

**Description:** Retrieves or updates the student's account information.

**Headers:**

```
Authorization: Bearer <jwt_access_token>
```

**GET Response:**

```
{
    "student_id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "other_name": "A.",
    "date_of_birth": "2000-01-01",
    "phone": "1234567890",
    "email": "john.doe@example.com",
    "student_email": "john.doe@student.example.com",
    "gender": "Male",
    "level": "Sophomore",
    "student_type": "Full-time",
    "enrollment_date": "2018-08-01",
    "graduation_date": "2022-05-15",
    "degree_programmes": "Computer Science",
    "guardian_name": "Jane Doe",
    "guardian_email": "jane.doe@example.com",
    "guardian_phone": "0987654321",
    "guardian_address": "123 Main St, Hometown"
}
```

**POST Request Body (change password):**

```
{
    "form_name": "change_password",
    "password": "current_password",
    "new_password": "new_password",
    "confirm_password": "new_password"
}
```

**POST Request Body (update details):**

```
{
    "form_name": "update_details",
    "contact_name": "New Guardian",
    "contact_mobile": "1122334455",
    "contact_email": "new.guardian@example.com",
    "contact_address": "456 New St, Newtown",
    "alternative_email": "john.alt@example.com",
    "additional_contact_email": "additional.contact@example.com"
}
```

### Courses

**URL:** `/courses`

**Method:** `GET`

**Description:** Retrieves the list of courses for the logged-in student's current semester.

**Headers:**

```
Authorization: Bearer <jwt_access_token>
```

**Response:**

```
{
    "course1": "Introduction to Programming",
    "course2": "Data Structures",
    "course3": "Calculus I"
}
```

### Results

**URL:** `/results`

**Method:** `GET`

**Description:** Retrieves the results of the logged-in student.

**Headers:**

```
Authorization: Bearer <jwt_access_token>
```

**Response:**

```
{
    "student_id": 1,
    "MATH_173": 85,
    "MATH_171": 90,
    "FREN_171": 75,
    "IT_133": 88,
    "METS_173": 82,
    "IT_101": 95,
    "SCOT_175": 89,
    "FREN_172": 78,
    "IT_102": 87,
    "IT_124": 91,
    "IT_152": 80,
    "MATH_176": 92,
    "ENG_174": 88,
    "AFRS_271": 85,
    "IT_231": 90,
    "IT_241": 85,
    "IT_245": 89,
    "FREN_273": 80,
    "IT_221": 88,
    "ENGL_275": 87,
    "IT_206": 89,
    "IT_274": 90,
    "IT_242": 85,
    "IT_222": 88,
    "IT_232": 87,
    "IT_204": 89,
    "IT_276": 90,
    "IT_323": 85,
    "IT_343": 88,
    "IT_313": 90,
    "IT_371": 85,
    "IT_391": 88,
    "IT_305": 89,
    "IT_301": 90,
    "IT_308": 85,
    "IT_302": 88,
    "IT_324": 90,
    "IT_344": 85,
    "IT_306": 88
}
```

### Evaluation

**URL:** `/evaluation`

**Method:** `GET`

**Description:** Retrieves the evaluation data for the logged-in student.

**Headers:**

```
Authorization: Bearer <jwt_access_token>
```

**Response:**

```
{
    "message": "Evaluation endpoint"
}
```

### Logout

**URL:** `/logout`

**Method:** `DELETE`

**Description:** Logs out the user by revoking their JWT.

**Headers:**

```
Authorization: Bearer <jwt_access_token>
```

**Response:**

```
{
    "message": "Successfully logged out"
}
```

## Token Revocation

The application uses a blacklist to revoke JWT tokens. When a user logs out, their token's `jti` (JWT ID) is added to the blacklist. The `check_if_token_revoked` function checks if a token is in the blacklist, preventing its use if it has been revoked.

## Error Handling

The application returns appropriate error messages and status codes for different scenarios, such as incorrect login credentials, missing student data, and unauthorized access attempts.

## Dependencies

- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Werkzeug
- JSON

Install these dependencies using `pip`:
Ensure your virtual environment is activated.

To activate a virtual environment (`venv`), you need to follow the appropriate steps depending on your operating system:

### **On Windows:**

1. **Open terminal in your project directory:**

2. **Activate the virtual environment:**
    ```bash
    venv\Scripts\activate
    ```
    You should see `(venv)` in your command prompt indicating that the virtual environment is active.

### **On macOS/Linux:**

1. **Open terminal in your project directory:**

2. **Activate the virtual environment:**
    ```bash
    source venv/bin/activate
    ```
    You should see `(venv)` in your terminal prompt indicating that the virtual environment is active.


```
pip install -r requirements.txt
```

## Running the Application

1. Ensure your virtual environment is activated.
2. Run the Flask application:
    ```
    python ussdapi.py
    ```
3. The application will be available at `http://0.0.0.0:5000`.

## Author

This application was developed by tawiah. For any questions or issues, please contact [tawiahin4k@gmail.com].