FROM python:latest
RUN pip install flask
COPY app.py /app.py
CMD ["python","app.py"]