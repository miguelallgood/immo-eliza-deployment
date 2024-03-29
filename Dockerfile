# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12-slim

# Expose the port that Streamlit runs on
EXPOSE 8502

# Update pip
RUN pip install --upgrade pip

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Set the working directory inside the container
WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Command to run the Streamlit app
CMD ["streamlit", "run", ".\streamlit\streamlit.py"]
