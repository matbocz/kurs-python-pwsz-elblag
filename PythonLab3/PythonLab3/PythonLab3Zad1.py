import urllib.request
import matplotlib.pyplot as plt

def get_html(url):
    req = urllib.request.Request(url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla'
    })
    resp = urllib.request.urlopen(req)
    data = resp.read() # page in bytes
    html = data.decode("UTF-8") # page in string

    return html

def count_letters(txt):
	result = 0
	for x in txt:
		if (ord(x) >= 65 and ord(x) <= 90):
			result += 1
		elif (ord(x) >= 97 and ord(x) <= 122):
			result += 1

	return result

def count_numbers(txt):
	result = 0
	for x in txt:
		if (ord(x) >= 48 and ord(x) <= 57):
			result += 1

	return result

def count_vowels(txt):
	vowels = "AaEeIiOoUuYy"
	result = [each for each in txt if each in vowels]

	return len(result)

def count_consonants(txt):
	consonants = "BbCcDdFfGgHhJjKkLlMmNnPpRrSsTtWwZz"
	result = [each for each in txt if each in consonants]

	return len(result)

url = "https://pwsz.elblag.pl/"

letters = count_letters(get_html(url))
numbers = count_numbers(get_html(url))
vowels = count_vowels(get_html(url))
consonants = count_consonants(get_html(url))

print("Letters: " + str(letters))
print("Numbers: " + str(numbers))
print("Vowels: " + str(vowels))
print("Consonants: " + str(consonants))

labels = ["Letters", "Numbers", "Vowels", "Consonants"]
values = [letters, numbers, vowels, consonants]
colors = ["red", "blue", "green", "yellow"]

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.bar(x=labels, height=values, color=colors)
ax2.pie(x=values, labels=labels, colors=colors)
plt.show()