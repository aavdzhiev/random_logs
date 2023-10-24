FROM redhat/ubi8/ubi-minimal
RUN yum install -y python3; yum clean all
WORKDIR ./app
ADD main.py kafka.txt rand_sentence.py /app/

ENTRYPOINT ["python3"]
CMD ["./main.py"]

