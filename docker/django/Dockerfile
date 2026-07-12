FROM python:3.14-slim


# Forces streams to be unbuffered
ENV PYTHONUNBUFFERED=1


# Install Python package
COPY requirements.txt /
RUN pip install --no-cache-dir --only-binary=:all: -r requirements.txt


# Create src folder
WORKDIR /src
COPY /src /src


# Install gunicorn
RUN pip install --no-cache-dir --only-binary=:all: gunicorn


# Run server
ENV PORT=8000
CMD ["sh", "-c", "gunicorn main.wsgi:application --bind 0.0.0.0:${PORT}"]
