FROM python:3.12.8-alpine

# Set the working directory in the container
WORKDIR /app

# Install make (and other necessary tools)
RUN apk update && \
    apk add --no-cache make bash

# Copy the project files into the container (excluding dependencies like .git or node_modules)
COPY . .

# Install dependencies from the root folder's requirements.txt
RUN python -m pip install pip --upgrade \
    && python -m pip install --no-cache-dir -r /app/requirements.txt \
    && adduser --disabled-password --no-create-home website_user

RUN chown -R website_user:website_user /app

USER website_user

# Expose the port your app will run on
EXPOSE 8002

# Use the Makefile to run the application
CMD ["make", "run"]


