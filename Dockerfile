FROM python:3.11
ADD main.py kafka.txt rand_sentence.py .
CMD ["python", "./main.py"]

