FROM python:3.9-slim-bookworm

RUN apt update && apt -y upgrade

WORKDIR /srv

COPY /src /srv

RUN pip install -r requirements.txt 

CMD ["python", "main.py"]

ENTRYPOINT ["python", "main.py"]