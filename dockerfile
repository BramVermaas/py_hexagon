FROM python:3.10-slim

WORKDIR /app
COPY . /app/

ENTRYPOINT ["python","-m"]
CMD ["py_hexagon"]