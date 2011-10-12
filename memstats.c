
#include <postgres.h>
#include <fmgr.h>
#include <utils/memutils.h>

PG_MODULE_MAGIC;

Datum memstats(PG_FUNCTION_ARGS);
PG_FUNCTION_INFO_V1(memstats);

/*
 * launch MemoryContextStats(TopMemoryContext)
 */
Datum memstats(PG_FUNCTION_ARGS)
{
	static int counter;

	elog(NOTICE, "MEMSTATS %d", counter++);
	MemoryContextStats(TopMemoryContext);

	PG_RETURN_INT32(1);
}

