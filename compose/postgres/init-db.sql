CREATE EXTENSION dblink;
CREATE EXTENSION "uuid-ossp";

DO
$body$
BEGIN
  IF NOT EXISTS (
      SELECT *
      FROM   pg_catalog.pg_user
      WHERE  usename = 'interview_admin') THEN

    CREATE ROLE airdna_test_admin LOGIN PASSWORD 'interview_password_wow';
  END IF;
END
$body$;

DO
$body$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_database WHERE datname = 'airdna') THEN
    RAISE NOTICE 'Database already exists';
  ELSE
    PERFORM dblink_exec('dbname=' || current_database()
    , 'CREATE DATABASE airdna');
  END IF;
END
$body$;

DO
$body$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_database WHERE datname = 'airdna_bind') THEN RAISE NOTICE 'Database already exists';
  ELSE
    PERFORM dblink_exec('dbname=' || current_database()
    , 'CREATE DATABASE airdna_bind');
  END IF;
END
$body$;

DO
$body$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_database WHERE datname = 'airdna_mat_bind') THEN RAISE NOTICE 'Database already exists';
  ELSE
    PERFORM dblink_exec('dbname=' || current_database()
    , 'CREATE DATABASE airdna_mat_bind');
  END IF;
END
$body$;

\connect airdna;

CREATE EXTENSION postgis;

\connect airdna_bind;

CREATE EXTENSION "uuid-ossp";
CREATE EXTENSION postgis;

\connect airdna_mat_bind;
CREATE EXTENSION postgis;

grant all on all tables in schema public to airdna_test_admin;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO airdna_test_admin;

\connect airdna;

CREATE TABLE property (
  property_id TEXT PRIMARY KEY,
  description TEXT
);

CREATE TABLE reservation (
  property_id TEXT REFERENCES property (property_id),
  start_date DATE,
  number_of_nights INT
);

INSERT INTO property VALUES
('xE6vqTqA6LTwpE', 'Spacious 1-bedroom villa overlooking a lake!'),
('SnbrmRLFxOhCAT', 'Studio apartment close to downtown.'),
('djddZlw8apLVfi', 'Ski in, ski out, 2-bedroom condo'),
('ApkY2fkDHhlsVY', 'Short walk to shopping and dining'),
('g3hbWxJ5TdXidt', '3 bedroom house, cook''s kitchen'),
('H75e1FjJFudcbC', '1-bedroom house with country feel'),
('1BlCOXqGH2MZb2', 'Two bedroom condo, walk to restaurants');

INSERT INTO RESERVATION VALUES
('xE6vqTqA6LTwpE', '2021-01-02', 2),
('xE6vqTqA6LTwpE', '2021-01-04', 7),
('xE6vqTqA6LTwpE', '2021-01-22', 3),
('SnbrmRLFxOhCAT', '2021-01-15', 2),
('SnbrmRLFxOhCAT', '2021-01-17', 2),
('SnbrmRLFxOhCAT', '2021-01-25', 4),
('djddZlw8apLVfi', '2021-01-10', 2),
('djddZlw8apLVfi', '2021-01-14', 5),
('djddZlw8apLVfi', '2021-01-23', 1),
('ApkY2fkDHhlsVY', '2021-01-03', 2),
('ApkY2fkDHhlsVY', '2021-01-07', 3);

