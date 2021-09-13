import requests
from requests.models import Response

url = '''
https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=2
'''

Response = requests.get(url)
responseDick=Response.json()

movies=responseDick["data"]["movies"]

print(type(movies))

movie1 =movies[0]

movie1Title= movie1["title"]
movie1Rating=movie1["rating"]

print(movie1Title)



