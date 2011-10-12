#! /usr/bin/env python

import psycopg2

# connect string
cstr = 'dbname=regression port=8300 host=localhost'

# test query
q = 'select testfunc(%s, %s, %s)'
args = ['qwe', 1, 'foo']

# connect
db = psycopg2.connect(cstr)
db.set_isolation_level(0)
curs = db.cursor()

# install func
fn = open('memstats.sql', 'r').read()
curs.execute(fn)

# run test query in loop
curs.execute('select memstats()')
while 1:
    for i in range(10000):
        curs.execute(q, args)
    curs.execute('select memstats()')

