from pyshorteners import Shortener
from pyshorteners.exceptions import ShorteningErrorException
from pyshorteners.exceptions import ExpandingErrorException
from urllib.parse import urlparse
USERTOKEN = '0a500de3665c382a05c18dfa247cebd6d06d2ce2'


# Retrieve user url input and shorten url with bitly
def shorten_url():
    print("Input a url to shorten: \n")
    while True:
        try:
            user_url = input()
            parsed_url = urlparse(user_url)
            if parsed_url.scheme == "":
                user_url = "http://" + user_url

            url_shortener = Shortener(api_key=USERTOKEN)
            print("String url: " + user_url)
            short_url = url_shortener.bitly.short(user_url)
            break
        except ShorteningErrorException:
            print("The entered url is not valid to be shortened, enter a new url.\n")

    print("Shortened url: " + short_url + "\n")


# Expand shortened url
def expand_url():
    print("Input a shortened bitly url to expand: \n")
    while True:
        try:
            short_url = input()
            parsed_url = urlparse(short_url)
            if parsed_url.scheme == "":
                short_url = "https://" + short_url

            url_expander = Shortener(api_key=USERTOKEN)
            long_url = url_expander.bitly.expand(short_url)
            break
        except ExpandingErrorException:
            print("The entered url is not valid to be expanded, enter a new bitly url.\n")

    print("Long url is " + long_url + "\n")


def main():
    while True:
        print("Enter an option:\n1: Shorten a url\n2: Expand a url\n3: Exit\n")
        answer = input()
        if answer == '1':
            shorten_url()
        elif answer == '2':
            expand_url()
        elif answer == '3':
            exit()


if __name__ == "__main__":
    main()
