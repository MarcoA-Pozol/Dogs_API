FROM python:3.11-slim

# Set working directory into container
WORKDIR /app

# Copy requirements.txt file to leverage Docker cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of application code to the working directory
COPY . .

# Set the environment variable for the SQLite db file
ENV DATABASE_URL = sqlite:///DogsAPI_DB.db

# Run FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10500"]