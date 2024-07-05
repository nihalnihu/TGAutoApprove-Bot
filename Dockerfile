FROM python:3.12
WORKDIR /app
COPY requirements.txt requirments.txt
RUN pip install --upgrade pip && pip install -r requirments.txt
COPY . .
CMD ["python", "bot.py"]
