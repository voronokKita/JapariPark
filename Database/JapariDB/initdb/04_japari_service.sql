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

ALTER DATABASE japari_park_default OWNER TO japari_service;
ALTER DATABASE japari_park_accounts OWNER TO japari_service;
ALTER DATABASE japari_friends OWNER TO japari_service;
ALTER DATABASE japari_friends_posts OWNER TO japari_service;
