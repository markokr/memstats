
MODULES = memstats
DATA = memstats.sql
REGRESS = memstats

PG_CONFIG = pg_config
PGXS = $(shell $(PG_CONFIG) --pgxs)
include $(PGXS)

zip:
	zip memstats.zip memstats.c memstats.sql Makefile

test:
	make install installcheck || { less regression.diffs; exit 1; }

ack:
	cp results/*.out expected/

