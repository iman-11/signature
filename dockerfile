FROM python:3.9

# Define the working directory inside the container
WORKDIR /signature_based

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 2000

# Define the command to run the Flask app
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=2000"]