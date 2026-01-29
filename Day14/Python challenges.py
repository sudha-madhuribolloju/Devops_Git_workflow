#Write a Python script that removes all duplicate
#elements from a list in a single line using sets.
from pytz import country_names

original_list = [1,2,2,6,4,6,2,4,5]
unique_list = list(set(original_list))
print(unique_list)

chars = list('mamma mia mm')
counts = {}
for ch in chars:
    counts[ch] = counts.get(ch, 0) + 1
for ch, count in counts.items():
    print(f"{ch} ---> {count}")

courses = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
len_course={}
for word in courses:
    len_course[word]=len(word)
print(len_course)

d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
sorted_key = dict(sorted(d1.items()))
print(sorted_key)

COUNTRY = country_names
for code in sorted(COUNTRY):
    print(code, ":", COUNTRY[code])

longest_country = max([name for name in COUNTRY.values()], key=len)
print("Country with Longest name :", longest_country)

years = [2015, 2016, 2017, 2018, 2019, 2020]
sales = [350000, 400000, 410000, 439000, 500000, 290000]
print(list(tuple(zip(years, sales))))

years = [2015, 2016, 2017, 2018, 2019, 2020]
sales = [350000, 400000, 410000, 439000, 500000, 290000]
print(dict(zip(years, sales)))

sales = {2015: 350000, 2016: 400000, 2017: 410000, 2018: 439000, 2019: 500000, 2020: 290000}
profit = {key: value * 0.25 for key, value in sales.items()}
print(profit)

names = ["Dan", "John", "Diana"]
phones = [11111, 2222, 3333]
print(set(zip(names, phones)))
