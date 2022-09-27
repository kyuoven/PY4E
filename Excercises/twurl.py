
# example bit of code that talks to the twitter
# imports
import urllib.request, urllib.parse, urllib.error
import twurl
import json

# We are getting the friendlist for a particular person
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

#ask a person for an account
while True:
	print('')
	acct = input('Enter Twitter Account:')
	if (len(acct) <1 ): break
	url = twurl.augment(TWITTER_URL,
# give me the first 5 friends of this account
						{'screen_name': acct, 'cuont': '5'})
# open the url, read it and decode it because of utf8 and makes sure its in a string
	print('Retrieving', url)
	connection = urllib.request.urlopen(url)
	data = connection.read().decode()
	headers = dict(connection.getheaders())
# key:value
	print('Remaining', headers['x-rate=limit-remaining'])
	js = json.loads(data)
	print(json.dumps(js, indent=4))

# for each user in users print screen name and status text and print it out
	for u in js['users']:
		print(u['screen_name'])
		s = u['status']['text']
		print('		', s[:50])