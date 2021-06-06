import pandas
from bs4 import BeautifulSoup
import requests
import ast

url = 'https://www.domain.com.au/sale/calamvale-qld-4116/?excludeunderoffer=1'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser') 

result = soup.head

body = result.find('script', type="application/ld+json")
filtered_body = str(body)[35:-9] #determine fixed offset required for removing tags on each page

# duplication exists in the json as some get featured at the top (will need to remove later)
result = ast.literal_eval(filtered_body)

result_set = [] # create an empty array to store all json objects
for listing in result:
    result_set.append(listing)

# final listing is a generic post about how many listings there are instead of an actual listing
# therefore, filter this listing entry out of the result set
result_set.pop(len(result_set)-1)

# print(result_set[len(result_set)-1])
print(result_set)

# next steps: 
#   * load data into dataframe using key-value pairs
#   * Transform data to desired shape
#   * Collect remainder of relevant data (geospatial data about localities nearby)
#   * look into a geocoding api to look up lat/long using addresses