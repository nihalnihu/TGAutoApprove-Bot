FROM python:3.12
WORKDIR TGAutoApprove-Bot
COPY TGAutoApprove-Bot/requirments.txt
RUN pip install --upgrade pip && pip install -r requirments.txt
CMD ["python", "bot.py"]
