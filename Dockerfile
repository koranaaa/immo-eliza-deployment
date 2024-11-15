# Use Python as the base image
FROM python:3.12

# Create a folder "app" at the root of the image
RUN mkdir /app_Van

# Set the working directory
WORKDIR /app_Van

# Copy all the project files to the working directory of the container
COPY . /app_Van/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Update pip
RUN pip install --upgrade pip

# Install dependencies from "requirements.txt"
RUN pip install -r requirements.txt

# Open port 8000 for API
EXPOSE 8000

# Run the app
# Set host to 0.0.0.0 to make it run on the container's network
CMD ["uvicorn", "api.app_Van:app", "--host", "0.0.0.0", "--port", "8000"]
