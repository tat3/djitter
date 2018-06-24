FROM python:3

ENV PORT 8000
ENV PYTHONUNBUFFERED 1
ENV DIRAPP /code
RUN mkdir $DIRAPP
WORKDIR $DIRAPP
ADD requirements.txt $DIRAPP/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . $DIRAPP/

CMD python manage.py runserver 0.0.0.0:$PORT
