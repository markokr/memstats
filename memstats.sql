
CREATE OR REPLACE FUNCTION memstats() RETURNS int4 AS '$libdir/memstats' LANGUAGE C;

