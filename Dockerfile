# Use the official Python image from the Docker Hub as the base image
FROM python:3.9.19-slim

# Set the working directory in the container to /app
WORKDIR /app

# # Copy the requirements file into the container at /app
# COPY /requirements.txt .

# # Install any needed packages specified in requirements.txt
# RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the python scripts (remaining files) into the container
COPY src/. .
COPY tests/. .

# Run app.py when the container launches
CMD ["python3", "main.py"]