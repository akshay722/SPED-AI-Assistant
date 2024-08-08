# Use the official Python image as the base image

FROM python:3.10

# Set the working directory to /app

WORKDIR /app

# Copy the current directory contents into the container at /app

COPY . /app

# Install any needed packages specified in requirements.txt

RUN pip install -r requirements.txt

# RUN pip install langchain-google-community==1.0.2

# RUN pip install langchain-experimental==0.0.57

# Expose port 8000 for the server

EXPOSE 8000

# Define the command to start the server

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
