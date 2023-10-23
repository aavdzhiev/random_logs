FROM s390x/ubuntu:latest
RUN apt-get update && apt-get install -y python3.9 python3.9-dev
ADD main.py kafka.txt rand_sentence.py ./
CMD ["python", "./main.py"]

