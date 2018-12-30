FROM python:3.4
ADD . /drishti
WORKDIR /drishti
EXPOSE 3000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "src/server.py"]
