FROM python:3.10-slim

WORKDIR /app
COPY py_hexagon /app/py_hexagon
COPY rate_files /app/rate_files
COPY tests /app/tests

ENTRYPOINT ["python","-m"]
CMD ["py_hexagon"]