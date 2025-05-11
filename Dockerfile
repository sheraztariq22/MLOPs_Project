# Use official Python image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Set environment variables
ENV MLFLOW_TRACKING_URI=file:///app/mlruns

# Run the training script
CMD ["python", "model/train_model.py"]
