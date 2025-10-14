FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy poetry files to the container
COPY pyproject.toml poetry.lock ./

# Install Poetry & dependencies
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi && \

# Copy the application code to the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=my_site.settings

# Set the default command to run the application
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
