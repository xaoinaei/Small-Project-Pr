import wolframalpha

client =wolframealpha.client('JHVJJ9-5K5KAYEY7H')
while true:
query = str (input('Query: '))
res = client.query(query)
output = next(res.results).text
print(output)