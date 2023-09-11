import json
from scholarly import scholarly

# will paginate to the next page by default
authors = scholarly.search_keyword("biology")

for author in authors:
    print(json.dumps(author, indent=2))