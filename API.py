import requests


class Urbandict():
    def urban(word):
        url = "http://api.urbandictionary.com/v0/define?term={}".format(word)
        dictionary = requests.get(url).json()
        return dictionary["list"][0]["definition"]
