FROM s390x/ubuntu:latest
ADD main.py kafka.txt rand_sentence.py ./
#CMD ["python", "./main.py"]

