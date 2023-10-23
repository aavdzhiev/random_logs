FROM s390x/python:latest
ADD main.py kafka.txt rand_sentence.py ./
CMD ["python", "./main.py"]

