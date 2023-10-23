FROM python:3.9-slim
ADD main.py kafka.txt rand_sentence.py ./
#CMD ["python", "./main.py"]

