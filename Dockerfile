FROM postgres:14-alpine

RUN apk add --no-cache openssl

RUN mkdir -p /var/lib/postgresql/certs /var/lib/postgresql/certs_export && \
   chmod 0700 /var/lib/postgresql/certs /var/lib/postgresql/certs_export && \
   chown -R postgres:postgres /var/lib/postgresql/certs /var/lib/postgresql/certs_export

USER postgres

RUN openssl req -new -x509 -days 365 -nodes \
    -out /var/lib/postgresql/certs/server.crt \
    -keyout /var/lib/postgresql/certs/server.key \
    -subj "/C=US/ST=State/L=City/O=Organization/OU=OrgUnit/CN=localhost" && \
    chmod 0600 /var/lib/postgresql/certs/server.key && \
    chmod 0644 /var/lib/postgresql/certs/server.crt


RUN openssl req -new -nodes -x509 -days 365 \
    -keyout /var/lib/postgresql/certs/ca.key \
    -out /var/lib/postgresql/certs/ca.crt \
    -subj "/C=US/ST=State/L=City/O=Organization/OU=OrgUnit/CN=CA" && \
    chmod 0600 /var/lib/postgresql/certs/ca.key && \
    chmod 0644 /var/lib/postgresql/certs/ca.crt

RUN mkdir -p /var/lib/postgresql/certs_export

WORKDIR /var/lib/postgresql

COPY ./initdb/master/init-master.sh /docker-entrypoint-initdb.d/
#  RUN chmod +x /docker-entrypoint-initdb.d/init-master.sh