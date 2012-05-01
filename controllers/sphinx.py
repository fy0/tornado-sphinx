#
# $Id$
#

# coding:utf-8

from controllers.sphinxapi import *
import sys, time

q = ''
mode = SPH_MATCH_ALL
host = 'localhost'
port = 9312
index = '*'
filtercol = 'group_id'
filtervals = []
sortby = ''
groupby = ''
groupsort = '@group desc'
limit = 0

# do query
cl = SphinxClient()
cl.SetServer ( host, port )

def query(q):
    if not q:return
    cl.SetWeights ( [100, 1] )
    cl.SetMatchMode ( mode )
    if filtervals:
	    cl.SetFilter ( filtercol, filtervals )
    if groupby:
	    cl.SetGroupBy ( groupby, SPH_GROUPBY_ATTR, groupsort )
    if sortby:
	    cl.SetSortMode ( SPH_SORT_EXTENDED, sortby )
    if limit:
	    cl.SetLimits ( 0, limit, max(limit,1000) )
    return cl.Query ( q, index )

#def getsummry(docs,index,words):
#    pass

#if not res:
#	print 'query failed: %s' % cl.GetLastError()
#	sys.exit(1)

#if cl.GetLastWarning():
#	print 'WARNING: %s\n' % cl.GetLastWarning()
'''
print 'Query \'%s\' retrieved %d of %d matches in %s sec' % (q, res['total'], res['total_found'], res['time'])
print 'Query stats:'

if res.has_key('words'):
	for info in res['words']:
		print '\t\'%s\' found %d times in %d documents' % (info['word'], info['hits'], info['docs'])

if res.has_key('matches'):
	n = 1
	print '\nMatches:'
	for match in res['matches']:
		attrsdump = ''
		for attr in res['attrs']:
			attrname = attr[0]
			attrtype = attr[1]
			value = match['attrs'][attrname]
			if attrtype==SPH_ATTR_TIMESTAMP:
				value = time.strftime ( '%Y-%m-%d %H:%M:%S', time.localtime(value) )
			attrsdump = '%s, %s=%s' % ( attrsdump, attrname, value )

		print '%d. doc_id=%s, weight=%d%s' % (n, match['id'], match['weight'], attrsdump)
		n += 1

#
# $Id$
#'''
