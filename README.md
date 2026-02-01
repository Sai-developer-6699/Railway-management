# Railway Management System

A Python-based Railway Management System that allows users to check train schedules, make reservations, and cancel tickets. The application features a GUI for user authentication (Login/Register) and a command-line interface for the core railway operations.

## Features

- **User Authentication**: Graphical interface for User Registration and Login.
- **Reservation**: Book train tickets and save them to the database.
- **Cancellation**: Cancel existing reservations.
- **Schedule Inquiry**:
  - View full train schedule.
  - Search trains by Train Number.
  - Search trains by Train Name.
  - Search trains by Origin.
  - Search trains by Destination.

## Prerequisites

- Python 3.x
- MySQL Server

### Required Python Packages

Install the necessary dependencies using pip:

```bash
pip install pandas numpy mysql-connector-python sqlalchemy openpyxl
```

*Note: `tkinter` is included with standard Python installations.*

## Setup Instructions

1.  **Database Configuration**:
    - Ensure you have a MySQL server running locally.
    - The project uses a database named `test`. You may need to create this database if it doesn't exist:
      ```sql
      CREATE DATABASE test;
      ```
    - The application uses the following credentials by default:
      - **User**: `root`
      - **Password**: `shu` (or `password` in some functions)
      - **Host**: `localhost`
    - **Important**: Open `project.py` and update the database connection strings to match your MySQL configuration.
      - Line 170: `mysql+mysqlconnector://root:shu@localhost/test`
      - Line 175: `user="root",password="password",database="test"`
      - Line 213: `mysql+mysqlconnector://root:shu@localhost/test`

2.  **File Paths**:
    - The project relies on an Excel file named `new railway data.xlsx` for train data.
    - **Important**: Update the file path in `project.py` to point to the correct location of `new railway data.xlsx` on your machine.
      - Find occurrences of `C:\\Users\\HP\\Downloads\\new railway data.xlsx` and replace them with the absolute path to the file in your `Railway-management` directory (e.g., `d:\CodingProjects\Python\Railway-Management\Railway-management\new railway data.xlsx`).

## Usage

1.  Navigate to the project directory:
    ```bash
    cd Railway-management
    ```

2.  Run the application:
    ```bash
    python project.py
    ```

3.  **Flow**:
    - The application will first launch a GUI window for **Account Login**.
    - Click **Register** to create a new account (credentials are stored locally in files).
    - Click **Login** to enter the system.
    - Upon successful login, the application proceeds to the terminal/console for the main menu (Reservation/Schedule).

## Project Structure

- `project.py`: Main source code file containing GUI and logic.
- `new railway data.xlsx`: Database of train schedules and details.

## Notes

- The user credentials for login are stored in local files named after the username.
- Ticket reservations are stored in the MySQL table `tick`.
