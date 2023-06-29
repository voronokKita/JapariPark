-- Role: creator
\set creator_pass `cat /run/secrets/admin_pass`

CREATE ROLE creator WITH
  LOGIN
  NOSUPERUSER
  INHERIT
  CREATEDB
  CREATEROLE
  NOREPLICATION
  PASSWORD :'creator_pass';

COMMENT ON ROLE creator IS 'Can create, may not create.';

GRANT UPDATE, DELETE
      ON ALL TABLES
      IN SCHEMA public TO creator;

GRANT UPDATE
      ON ALL SEQUENCES
      IN SCHEMA public TO creator;

GRANT CREATE ON SCHEMA public TO creator;
