# Use an official Python runtime as a parent imageFriday 3/29. 
FROM python:3.6

# Set the working directory to /app
WORKDIR /detect_objects

# Copy the current directory contents into the container at /app
COPY . /detect_objects

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Make port 80? available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World
ENV PYTHONPATH detect_objects
ENV VAR AWS_ACCESS_KEY_ID
ENV VAR AWS_SECRET_ACCESS_KEY

# Run app.py when the container launches
CMD ["python3", "detect_objects/"]