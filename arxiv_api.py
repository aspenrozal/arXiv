import urllib, urllib.request
import feedparser 
import time
import pandas as pd
import matplotlib.pyplot as plt
# --------------------------------------------------------------------------------------------------------------------------------------------
# Example from: https://static.arxiv.org/static/arxiv.marxdown/0.1/help/api/examples/python_arXiv_paging_example.txt
# https://arxiv.org/search/advanced?advanced=1&terms-0-operator=AND&terms-0-term=fairness&terms-0-field=all&terms-1-operator=AND&terms-1-term=variance&terms-1-field=all&terms-2-operator=OR&terms-2-term=algorithmic+bias&terms-2-field=title&classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size=50&order=-announced_date_first
# # Base api query url
base_url = 'http://export.arxiv.org/api/query?';

# Search parameters
# Query: "algorithmic fairness" OR "algorithmic bias" OR "disparate impact" OR "equal opportunity" OR "equality of opportunity" OR equalized odds" AND "variance" OR "variation" OR "variability" OR "standard deviation"
search_query = '%28all:%22algorithmic+fairness%22+OR+all:%22algorithmic+bias%22+OR+all:%22disparate+impact%22+OR+all:%22equal+opportunity%22+OR+all:%22equality+of+opportunity%22+OR+all:%22equalized+odds%22%29+AND+%28all:%22variance%22+OR+all:%22variability%22+OR+all:%22variation%22+all:%22standard+deviation%22%29'

# published = 
start = 0                       # start at the first result
total_results = 10               # want x total results
results_per_iteration = 5       # 5 results at a time
wait_time = 3                   # number of seconds to wait beetween calls
sort_type = 'submittedDate'     # submittedDate or relevance or lastUpdatedDate
sort_order = 'descending'        # Ascending or descending

print ('Searching arXiv for %s' % search_query)

#Establish the list outside the loop
#List to store metadata entries which will be used to create the bar chart
metadata = list();

# Original:
for i in range(start, total_results, results_per_iteration):
# for i in range(start,results_per_iteration):
    
    print ("Results %i - %i" % (i,i+results_per_iteration))
    
    query = 'search_query=%s&start=%i&max_results=%i&sortBy=%s&sortOrder=%s' % (search_query,
                                                         i,
                                                        results_per_iteration,
                                                        sort_type,
                                                        sort_order)

    # perform a GET request using the base_url and query
    response = urllib.request.urlopen(base_url+query).read()

    # parse the response using feedparser
    feed = feedparser.parse(response)

    # count( feed.entries )

    # Debugging ------------------------------------
    # print( 'RESPONSE', type( response ) ) #Bytes
    # print( 'RESPONSE',len(response) )
    # print( 'FEED', type( feed ) ) #Feed object
    # print( 'FEED', len( feed ) )
    # ----------------------------------------------
    
    # Run through each entry, and print out information
    

    for entry in feed.entries:
        # print ('arxiv-id: %s' % entry.id.split('/abs/')[-1])
        # print ('Title:  %s' % entry.title)
        # # feedparser v4.1 only grabs the first author
        # print ('First Author:  %s' % entry.author)
        # print ( 'Date: %s ' % entry.date)

        metadata.append( entry.date )
        metadata.append( entry.category )

    # Remember to play nice and sleep a bit before you call
    # the api again!
    print ('Sleeping for %i seconds' % wait_time )
    time.sleep(wait_time)

print( "LENGTH", len(metadata) );
print( metadata );
# len( 'ENTRIES', feed.entries )

# # Response is type "bytes" converting to Str
# convStr = response.decode()
# # print(type(convStr))
# # print(convStr)

# # Write the results to a file
# with open('test.txt', 'w') as f:
#     f.write(convStr)