FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY /LaCasa/ /code/
#COPY CARPETA_DE_LA_CASA /CODE/
RUN pip install -r requirements.txt
RUN chown -R $USER:$USER .
RUN ls
