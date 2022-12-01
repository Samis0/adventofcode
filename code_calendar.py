#!/usr/bin/env python3

import requests

cookies = {'session': 'cookie'}

x = requests.get('https://adventofcode.com/2022/day/1/input', cookies=cookies)



my_string = x.text




test = [item.split('\n') for item in my_string.split('\n\n') if item]


for item in test:
    try:
        item.remove('')
    except ValueError:
        pass

teeeest = [list(map(int, itemm)) for itemm in test]

tetete = [sum(item) for item in teeeest]

maxtest = max(tetete)

teeeeeest = sorted(tetete, reverse=True)


wow = teeeeeest[:3]

print(wow)

wou = sum(wow)

print(wou)

