# Step 1: Python base image-ah edukkirom
FROM python:3.10-slim

# Step 2: Container-kulla oru folder create pannikiraom
WORKDIR /app

# Step 3: Namma app.py-ah container-kulla copy panrom
COPY app.py .

# Step 4: Monitoring-ku dheyvaiyana psutil-ah install panrom
RUN pip install psutil

# Step 5: Container start aagumpodhu indha command run aagum
CMD ["python", "app.py"]
