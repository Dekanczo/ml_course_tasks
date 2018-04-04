import requests

query = "Angela Merkel says 'horoshecno'. Apple is looking at buying U.K. startup for $1 billion"
re = requests.post('http://0.0.0.0:8080/post', data=query)
print(re.text)
