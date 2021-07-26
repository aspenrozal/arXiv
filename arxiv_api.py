import urllib, urllib.request
import feedparser 
import time

# --------------------------------------------------------------------------------------------------------------------------------------------
# Example from: https://static.arxiv.org/static/arxiv.marxdown/0.1/help/api/examples/python_arXiv_paging_example.txt
# Base api query url
base_url = 'http://export.arxiv.org/api/query?';

# Search parameters
search_query = 'all:fairness+AND+variance' # search for electron in all fields
# published = 
start = 0                       # start at the first result
total_results = 10              # want 20 total results
results_per_iteration = 5       # 5 results at a time
wait_time = 3                   # number of seconds to wait beetween calls

print ('Searching arXiv for %s' % search_query)

# Original:
for i in range(start,total_results,results_per_iteration):
# for i in range(start,results_per_iteration):
    
    print ("Results %i - %i" % (i,i+results_per_iteration))
    
    query = 'search_query=%s&start=%i&max_results=%i' % (search_query,
                                                         i,
                                                        results_per_iteration)

    # perform a GET request using the base_url and query
    response = urllib.request.urlopen(base_url+query).read()

    # parse the response using feedparser
    feed = feedparser.parse(response)

    # Run through each entry, and print out information
    for entry in feed.entries:
        print ('arxiv-id: %s' % entry.id.split('/abs/')[-1])
        print ('Title:  %s' % entry.title)
        # feedparser v4.1 only grabs the first author
        print ('First Author:  %s' % entry.author)

    # Remember to play nice and sleep a bit before you call
    # the api again!
    print ('Sleeping for %i seconds' % wait_time )
    time.sleep(wait_time)

# Response is type "bytes" converting to Str
convStr = response.decode()
# print(type(convStr))
# print(convStr)

# Write the results to a file
with open('test.txt', 'w') as f:
    f.write(convStr)