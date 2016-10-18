import unirest
# These code snippets use an open-source library. http://unirest.io/python

#getting the desired category name from user
category = raw_input('Enter the category of quote you want: "movies" or "famous" \n')

print('You have asked for '+category + ' quote')

#building the request url
our_url = "https://andruxnet-random-famous-quotes.p.mashape.com/?cat="+category 

#print(our_url)

#sending POST request call
result = unirest.post(our_url,
  headers={
    "X-Mashape-Key": "xxx", #replace xxx with your own key
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  }
)

#print(result.body)


#parsing the dictionary which came out of json 
for key in result.body:
    print(key + ' : ' + result.body[key])
