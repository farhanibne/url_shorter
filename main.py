import pyshorteners

s = pyshorteners.Shortener()

url = "type the link here"
print(s.tinyurl.short(url))