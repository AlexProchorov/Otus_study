FROM python:3.11.8
ENV PYTHONUNBUFFERED=1
LABEL maintainer="Alex Prochorov <proch0r0v@yandex.ru>"

#SHELL ["bin/bash","-c"]
# switch working directory
WORKDIR /otus_app
# copy every content from the local file to the image
COPY /otus_app .

# copy the requirements file into the image
COPY otus_app/requirements.txt /otus_app/requirements.txt

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt
RUN mkdir /otus_app/static
#RUN python manage.py collectstatic --noinput
EXPOSE 8000
# configure the container to run in an executed manner
CMD ["gunicorn", "otus_app.wsgi:application", "--bind", "0.0.0.0:8000"]


