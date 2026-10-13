# ACEest Fitness & Gym DevOps Pipeline

This project implements an automated CI/CD pipeline for a Flask-based web application tailored for fitness and gym management, specifically built for ACEest Fitness & Gym.

## Project Structure
- `app.py`: The core Flask application serving fitness programs and user registration endpoints.
- `test_app.py`: Unit tests using Pytest to validate application logic.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Instructions to containerize the Flask application.
- `.github/workflows/main.yml`: GitHub Actions pipeline for automated building and testing.

## Local Setup and Execution (Windows)
1. **Clone the repository:**
   ```cmd
   git clone <your-github-repo-url>
   cd <repository-directory>