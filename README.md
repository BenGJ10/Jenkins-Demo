# Flask Jenkins CI/CD Demo

A simple Flask web application created to demonstrate a basic Jenkins CI/CD pipeline. The project demonstrates source code checkout, dependency installation, automated testing, and build execution using Jenkins.

## Tech Stack

- **Python** – Application development
- **Flask** – Web framework
- **Gunicorn** – WSGI HTTP server
- **Jenkins** – CI/CD automation
- **Git & GitHub** – Source code management

## Project Structure

```text
flask-jenkins-demo/
├── app.py
├── requirements.txt
├── Jenkinsfile
└── README.md
```

## Application Endpoints

| Endpoint | Description |
|---|---|
| `/` | Home page |
| `/health` | Application health check |
| `/api` | Returns application information in JSON |

## Prerequisites

- Python 3.10+
- pip
- Git
- Jenkins
- GitHub repository


## Jenkins CI/CD Pipeline

The project includes a `Jenkinsfile` that defines the following stages:

1. **Checkout:** Retrieves source code from the configured Git repository.
2. **Install Dependencies:** Creates a Python virtual environment and installs dependencies.
3. **Test:** Runs basic endpoint tests using Flask's test client.
4. **Build:** Marks the build stage as completed.

## Configure Jenkins

1. Open the Jenkins dashboard.
2. Click **New Item**.
3. Enter the project name: `Flask-Jenkins-Demo`.
4. Select **Pipeline** and click OK.
5. Under Pipeline configuration, select **Pipeline script from SCM**.
6. Select **Git** as SCM.
7. Enter your GitHub repository URL.
8. Specify the branch (usually `*/main`).
9. Set Script Path to `Jenkinsfile`.
10. Save the configuration.
11. Click **Build Now**.

## Verify Pipeline Execution

Open the Jenkins job and inspect:

- Console Output
- Stage View
- Build Status

A successful pipeline should complete all four stages.

## Expected Result

```text
Checkout                 SUCCESS
Install Dependencies     SUCCESS
Test                     SUCCESS
Build                    SUCCESS
```

## Future Enhancements

- Docker image creation
- Automated deployment
- GitHub webhook integration
- Docker Hub image publishing
- Deployment to AWS EC2

---

**Purpose:** This project is intended for learning and demonstrating basic CI/CD concepts using Jenkins and Python Flask.