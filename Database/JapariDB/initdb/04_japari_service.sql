-- Role: japari_service
\set jservice_pass `cat /run/secrets/jservice_pass`

CREATE ROLE japari_service WITH
  LOGIN
  NOSUPERUSER
  INHERIT
  CREATEDB
  NOCREATEROLE
  NOREPLICATION
  PASSWORD :'jservice_pass';

COMMENT ON ROLE japari_service IS 'Japari Park: Backend Service. Django models and migrations.';

GRANT ALL PRIVILEGES ON DATABASE japari_park_default TO japari_service;
GRANT ALL PRIVILEGES ON DATABASE japari_park_accounts TO japari_service;
GRANT ALL PRIVILEGES ON DATABASE japari_friends TO japari_service;
GRANT ALL PRIVILEGES ON DATABASE japari_friends_posts TO japari_service;
