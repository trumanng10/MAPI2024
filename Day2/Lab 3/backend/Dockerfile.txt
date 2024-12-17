# Use the official Python image from Docker Hub
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local app to the container
COPY . /app

# Install required Python libraries
RUN pip install -r requirements.txt

# Expose the app's port
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
