FROM python:3.11-slim-bullseye

ENV APPPATH /app

COPY . ${APPPATH}
WORKDIR ${APPPATH}

RUN chmod +x ${APPPATH}/docker-entrypoint.sh \
  && pip install --no-cache-dir -r requirements.txt

CMD ["./dev_script/docker-entrypoint.sh"]