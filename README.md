# Basic Flask API

This project is a simple **Flask application** that fetches data from [JSONPlaceholder](https://jsonplaceholder.typicode.com) and exposes it via REST endpoints.  
It also includes **Swagger UI** for interactive API documentation.

---

## Prerequisites

- **Python 3.8+** installed on your machine  
  - [Download Python for Windows](https://www.python.org/downloads/windows/) 
- **pip** (comes bundled with Python 3.4+)  
- (Optional but recommended) **Virtual environment (`venv`)** for isolated dependencies  

---

## Installation & Setup

### Step 1: Clone the repository (or create a project folder)
```bash
git clone <your-repo-url>
cd BasicFlaskAPP
```

### Step 2: Setting up Environment and running the application
```bash
python -m venv venv
venv\Scripts\Activate
pip install -r requirements.txt
flask run
```

### Step 3: Check swagger documentation
- **Visit swagger documentation** to understand supported endpoints
    - [Swagger](http://127.0.0.1:5000/apidocs/) 