FROM python:3.9.21

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirment.txt ./
RUN pip install -r requirment.txt
COPY . .

EXPOSE 8000
EXPOSE 12000
CMD ["python", "manage.py", "runserver", "0.0.0.0:"]
ENTRYPOINT [ "8000" ]
