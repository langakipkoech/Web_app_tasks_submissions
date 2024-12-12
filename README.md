# Web_app_tasks_submissions
Web application to help users manage the tasks they have at hand, users can create and login to the respective page. Attached is a docker file for building a docker image

# Web_app_tasks_submissions

This repository contains the source code for a web application that enables users to manage their tasks. Users can create accounts, log in, and then create, edit, and view their tasks.

This project also includes a Dockerfile for building a Docker image, allowing for easy deployment and containerization of the application.

## Features

- **User Management**: Users can register, log in, and log out of the application.
- **Task Management**:
  - Create new tasks with descriptions and deadlines.
  - View and edit existing tasks.
  - Mark tasks as completed/incomplete.

## Technologies Used

- **Backend**: Python, Django
- **Authentication**: Django's built-in authentication system
- **Containerization**: Docker (for deployment)

## Prerequisites

To run this application, you'll need the following:

- Python 3.x 
- Django (version specified in `requirements.txt`)
- Docker (if you want to use the Dockerfile)

Make sure you have Docker installed to build the image for easy deployment.

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/langakipkoech/Web_app_tasks_submissions.git
cd Web_app_tasks_submissions

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

docker build -t web_app_tasks .

docker run -p 8000:8000 web_app_tasks





