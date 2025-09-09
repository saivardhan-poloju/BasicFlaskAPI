# Basic Flask API

This project is a simple **Flask application** that fetches data from [JSONPlaceholder](https://jsonplaceholder.typicode.com) and exposes it via REST endpoints.  
It also includes **Swagger UI** for interactive API documentation.

---

## Prerequisites

- **Python 3.8+** installed on your machine  
  - [Download Python for Windows](https://www.python.org/downloads/windows/) 
- **pip** (comes bundled with Python 3.4+)

---

## Installation & Setup

### Step 1: Clone the repository (or create a project folder)
```bash
git clone https://github.com/saivardhan-poloju/BasicFlaskAPI.git     # Clone the project from GitHub 
cd BasicFlaskAPI                                                     # Navigate into the project folder
```

### Step 2: Setting up the Environment and running the application
```bash
python -m venv venv                # Create a new virtual environment named 'venv' in the current folder
venv\Scripts\Activate              # Activate the virtual environment (Windows cmd). 
                                   # For PowerShell use: .\venv\Scripts\Activate.ps1
                                   # For Mac/Linux use: source venv/bin/activate
pip install -r requirements.txt    # Install all required Python packages listed in requirements.txt
flask run                          # Start the Flask development server
```

### Step 3: Check Swagger documentation
- **Visit swagger documentation** to understand supported endpoints
    - [Swagger](http://127.0.0.1:5000/apidocs/) 
