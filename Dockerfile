FROM public.ecr.aws/lambda/python:3.9

WORKDIR /var/task

COPY . /var/task

RUN pip install --no-cache-dir -r requirements.txt