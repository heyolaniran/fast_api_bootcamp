# Odoo FastAPI Integration

FAST API BOOTCAMP to masterize API development with Python

## Project Setup

### Prerequisites

- Python 3.8+

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/heyolaniran/fast_api_bootcamp.git
    cd fast_api_bootcamp
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file in the root directory and add the following:
    ```env
    ```

5. **Run the FastAPI server: Through Uvicorn**
    ```bash
    uvicorn main:app --reload
    ```
6. **Run the FastAPI server: Through Dockerfile**
    ```bash
    docker build -t fast_api_bootcamp
    docker run -p 8000:8000 fast_api_bootcamp
    ```
7. **Run the FastAPI server: Through Docker Compose**
    ```bash
    docker compose watch 
    ```
### Usage

- Access the API documentation at `http://localhost:8000/docs`
- Use the endpoints to interact with your Odoo instance

### Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

### License

This project is licensed under the MIT License.

### Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)

