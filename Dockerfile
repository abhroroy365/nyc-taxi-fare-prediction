FROM continuumio/anaconda3:4.4.0
COPY . /user/app/
EXPOSE 5000
WORKDIR /user/app/
RUN pip install -r requirements.txt
CMD python flask_api.py
