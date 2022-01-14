from pyshorteners import Shortener
USERTOKEN = '0a500de3665c382a05c18dfa247cebd6d06d2ce2'

# Retrieve user url input
print("Input a url to shorten: \n")
user_url = raw_input()
url_shortener = Shortener('Bitly', bitly_token=USERTOKEN)
short_url = url_shortener.short(user_url)
print("Shortened url: {}".format(short_url))

# expand shortened url
print("Input a shortened url to expand: \n")
short_url = raw_input()
url_expander = Shortener('Bitly', bitly_token=USERTOKEN)
long_url = url_expander.expand(short_url)
print("Long url is:  {}".format(long_url))
