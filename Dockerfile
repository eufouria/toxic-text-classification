# Using Python 3.11 base image
FROM python:3.11

# Define the virtual environment path
ENV VIRTUAL_ENV=/opt/venv

# Create virtual environment
RUN python3 -m venv $VIRTUAL_ENV

# Set the virtual environment path in PATH
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents to the container at /app
COPY . /app

# Install dependencies, ensuring Uvicorn is included
RUN pip install uvicorn
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 30000

# Command to run the Uvicorn server
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "30000"]
