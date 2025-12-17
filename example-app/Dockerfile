FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5000

# Add environment variables
ENV FLASK_APP=app.py
ENV APP_MESSAGE="Hello from Docker!"
ENV APP_COLOR="#667eea"

CMD ["python", "app.py"]