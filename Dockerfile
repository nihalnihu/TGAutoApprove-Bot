FROM python:3.12
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip && pip install -r requirments.txt
CMD ["python", "bot.py"]
