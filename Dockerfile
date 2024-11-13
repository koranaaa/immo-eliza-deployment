# Використовуємо Python як базовий образ
FROM python:3.12

# Create a folder "app" at the root of the image
RUN mkdir /app

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо всі файли проекту в робочу директорію контейнера
COPY . /app

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Update pip
RUN pip install --upgrade pip

# Install dependencies from "requirements.txt"
RUN pip install -r requirements.txt

# Відкриваємо порт 8000 для API
EXPOSE 8000

# Run the app
# Set host to 0.0.0.0 to make it run on the container's network
CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]
