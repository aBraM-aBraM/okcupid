FROM ubuntu:latest

# rm to remove lists that are unecessary after build
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-virtualenv && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app
COPY ./okcupid /app/
COPY ./main.py /app/

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN python3 -m virtualenv venv
RUN ./venv/bin/pip3 install --no-cache-dir -r requirements.txt

# Command to run when the container starts (can be modified as needed)
CMD ["python3", "main.py", "--session", "/host/.session"]
