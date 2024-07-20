FROM python:3.10

COPY requirement.txt /tmp/requirement.txt

RUN python -m pip install --timeout 30000 --no-cache-dir -r /tmp/requirement.txt

WORKDIR /app

COPY . /app

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
