FROM python:3.8.11
COPY . /Users/nathangrey/Desktop/RTI_Exercise
WORKDIR /Users/nathangrey/Desktop/RTI_Exercise
RUN pip install -r requirements.txt
EXPOSE 5150
ENTRYPOINT ["python3"]
CMD [ "app.py" ]