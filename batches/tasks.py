from celery import task
from celery.contrib.batches import Batches
@task( base=Batches, flush_every=5, flush_interval=0)
def collect_stats( requests ): 
        print "haiii"
	items = {} 
        print type(requests)
        print len(requests)
        for request in requests:
            print "Keyword Args***"
            print request.kwargs
            print "Args***"
            print request.args
            '''print request.kwargs[item_id]
            print request.kwargs[item_id]
            id = request.kwargs[item_id] 
	    items[ id ] =id
            items[ id ].count += 1
            print items
	    items[ item_id ] = get_obj( item_id ) 
            items[ item_id ].count += 1 # Sync to dbcollect_stats.delay( item_id = 45 )collect_stats.delay( item_id = 57 )'''
