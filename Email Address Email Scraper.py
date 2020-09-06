import re
text = "random string. myname@websites.com . you_company9-9-0@website.net . some more string."
pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9\.\_\-]+.[a-zA-Z]")
result = pattern.findall(text)
print(result)
