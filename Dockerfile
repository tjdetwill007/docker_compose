FROM python:latest
WORKDIR /app
COPY . .
RUN pip install flask  mysql.connector
EXPOSE 5000
CMD ["flask", "run"]