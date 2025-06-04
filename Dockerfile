FROM ubuntu 

WORKDIR /labs
COPY . .

RUN apt update -y
RUN apt install python3 pip -y
RUN pip install nltk --break-system-packages
