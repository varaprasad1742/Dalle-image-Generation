# Use the official Python image
FROM python:3.9-slim AS backend

# Set working directory
WORKDIR /app

# Copy the backend files
COPY . .
ENV OPENAI_API_KEY=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
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8000

# Command to run the backend server
CMD ["uvicorn", "app:web", "--reload"]

