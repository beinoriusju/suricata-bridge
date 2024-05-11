FROM python:3.12

WORKDIR /app

COPY . /app
    
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "-u", "app.py"]