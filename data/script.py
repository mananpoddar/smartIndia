import json
import random

no_of_points = 100000

def rand_range(a, b):
    return (b-a) * random.random() + a

def tax_bracket(credit):
    tax = 0
    if credit <= 250000:
        return 0
    elif credit < 500000:
        return (credit - 250000) * 0.05
    elif credit < 1000000:
        return (credit - 500000) *  0.2 + 250000 * 0.05
    else:
        return (credit - 1000000) * 0.3 + 500000 * 0.2 + 250000 * 0.05

with open('data.csv', 'a') as f:
    f.write(','.join(['lower_education', 'higher_education', 'area', 'jewellery', 'car', 'bike', 'tax', 'misc_credit', 'misc_debit']) + '\n')

with open('template-2.json', 'r') as f:
    o = json.load(f)

obj = o['poor']
for i in range(no_of_points):
    # "poor": {
    #     "lower_education": [0.05,0.10],
    #     "higher_education": [0.05,0.10],
    #     "area":["slum","middle"],
    #     "jewellery":[0,5000],
    #     "car":[0,0],
    #     "bike":[0,1],
    #     "misc_credit":[0,50000],
    #     "misc_debit":[0,50000],
    #     "desc": "poor"
    # },
    lower_education = int(rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    higher_education = int(rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "slum" if random.random() < 0.9 else "middle"
    jewellery  = 0 if random.random() > 0.9 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1]))
    car       = random.randint(obj['car'][0], obj['car'][1])
    bike      = random.randint(obj['bike'][0], obj['bike'][1])
    misc_credit = int(rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    tax       = tax_bracket(misc_credit)
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data.csv', 'a') as f:
        f.write(','.join([str(i) for i in new_data]) + '\n')
    
obj = o['poor_business']
for i in range(no_of_points):
    # "poor_business": {
    #     "lower_education": [0.05,0.10],
    #     "higher_education": [0.05,0.10],
    #     "area":["slum","middle"],
    #     "jewellery":[0,5000],
    #     "car":[0,0],
    #     "bike":[0,1],
    #     "misc_credit":[0,60000],
    #     "misc_debit":[0,60000],
    #     "desc": "poor_business"
    # },
    lower_education = int(rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    higher_education = int(rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "slum" if random.random() < 0.9 else "middle"
    jewellery  = 0 if random.random() > 0.9 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1]))
    car       = random.randint(obj['car'][0], obj['car'][1])
    bike      = random.randint(obj['bike'][0], obj['bike'][1])
    misc_credit = int(rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    tax       = tax_bracket(misc_credit)
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data.csv', 'a') as f:
        f.write(','.join([str(i) for i in new_data]) + '\n')

obj = o['lower_middle']
for i in range(no_of_points):
    # "lower_middle": {
    #     "lower_education": [0.05,0.10],
    #     "higher_education": [0.10,0.15],
    #     "area":["middle"],
    #     "jewellery":[0,10000],
    #     "car":[0,1],
    #     "bike":[0,1],
    #     "misc_credit":[50000,450000],
    #     "misc_debit":[50000,450000],
    #     "desc": "lower_middle"
    # },
    lower_education = int(rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "middle"
    jewellery  = 0 if random.random() > 0.9 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1]))
    car       = random.randint(obj['car'][0], obj['car'][1])
    bike      = random.randint(obj['bike'][0], obj['bike'][1])
    misc_credit = int(rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    tax       = tax_bracket(misc_credit)
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data.csv', 'a') as f:
        f.write(','.join([str(i) for i in new_data]) + '\n')

obj = o['lower_middle_business']
for i in range(no_of_points):
    # "lower_middle_business": {
    #     "lower_education": [0.05,0.10],
    #     "higher_education": [0.10,0.15],
    #     "area":["middle"],
    #     "jewellery":[0,10000],
    #     "car":[0,1],
    #     "bike":[0,1],
    #     "misc_credit":[50000,600000],
    #     "misc_debit":[50000,600000],
    #     "desc": "lower_middle_business"
    # },
    lower_education = int(rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "middle"
    jewellery  = 0 if random.random() > 0.9 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1]))
    car       = random.randint(obj['car'][0], obj['car'][1])
    bike      = random.randint(obj['bike'][0], obj['bike'][1])
    misc_credit = int(rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    tax       = tax_bracket(misc_credit)
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data.csv', 'a') as f:
        f.write(','.join([str(i) for i in new_data]) + '\n')

obj = o['middle']
for i in range(no_of_points):
    # "middle": {
    #     "lower_education": [0.10,0.15],
    #     "higher_education": [0.15,0.20],
    #     "area":["middle"],
    #     "jewellery":[0,50000],
    #     "car":[0,2],
    #     "bike":[0,2],
    #     "misc_credit":[450000,1200000],
    #     "misc_debit":[450000,1200000],
    #     "desc": "middle"
    # },
    lower_education = int(rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "middle"
    jewellery  = 0 if random.random() > 0.9 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1]))
    car       = random.randint(obj['car'][0], obj['car'][1])
    bike      = random.randint(obj['bike'][0], obj['bike'][1])
    misc_credit = int(rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    tax       = tax_bracket(misc_credit)
    with open('data.csv', 'a') as f:
        f.write(','.join([str(i) for i in new_data]) + '\n')

obj = o['middle_business']
for i in range(no_of_points):
    # "middle_business": {
    #     "lower_education": [0.10,0.15],
    #     "higher_education": [0.15,0.20],
    #     "area":["middle","posh"],
    #     "jewellery":[0,50000],
    #     "car":[0,2],
    #     "bike":[0,2],
    #     "misc_credit":[450000,2000000],
    #     "misc_debit":[450000,2000000],
    #     "desc": "middle_business"
    # },
    lower_education = int(rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "middle" if random.random() < 0.9 else "posh"
    jewellery  = 0 if random.random() > 0.9 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1]))
    car       = random.randint(obj['car'][0], obj['car'][1])
    bike      = random.randint(obj['bike'][0], obj['bike'][1])
    misc_credit = int(rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    tax       = tax_bracket(misc_credit)
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data.csv', 'a') as f:
        f.write(','.join([str(i) for i in new_data]) + '\n')

obj = o['upper_middle']
for i in range(no_of_points):
    # "upper_middle": {
    #     "lower_education": [0.15,0.20],
    #     "higher_education": [0.20,0.25],
    #     "area":["posh","middle"],
    #     "jewellery":[0,100000],
    #     "car":[1,3],
    #     "bike":[0,2],
    #     "misc_credit":[1200000,2400000],
    #     "misc_debit":[1200000,2400000],
    #     "desc": "upper_middle"
    # },
    lower_education = int(rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "middle" if random.random() < 0.9 else "posh"
    jewellery  = 0 if random.random() > 0.9 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1]))
    car       = random.randint(obj['car'][0], obj['car'][1])
    bike      = random.randint(obj['bike'][0], obj['bike'][1])
    misc_credit = int(rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    tax       = tax_bracket(misc_credit)
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data.csv', 'a') as f:
        f.write(','.join([str(i) for i in new_data]) + '\n')

obj = o['upper_middle_business']
for i in range(no_of_points):
    # "upper_middle_business": {
    #     "lower_education": [0.15,0.20],
    #     "higher_education": [0.20,0.25],
    #     "area":["posh","middle"],
    #     "jewellery":[0,100000],
    #     "car":[1,3],
    #     "bike":[0,2],
    #     "misc_credit":[1200000,3000000],
    #     "misc_debit":[1200000,3000000],
    #     "desc": "upper_middle_business"
    # },
    lower_education = int(rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "middle" if random.random() < 0.9 else "posh"
    jewellery  = 0 if random.random() > 0.9 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1]))
    car       = random.randint(obj['car'][0], obj['car'][1])
    bike      = random.randint(obj['bike'][0], obj['bike'][1])
    misc_credit = int(rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    tax       = tax_bracket(misc_credit)
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data.csv', 'a') as f:
        f.write(','.join([str(i) for i in new_data]) + '\n')

obj = o['rich']
for i in range(no_of_points):
    # "rich": {
    #     "lower_education": [0.15,0.20],
    #     "higher_education": [0.20,0.25],
    #     "area":["posh"],
    #     "jewellery":[0,500000],
    #     "car":[1,5],
    #     "bike":[0,3],
    #     "misc_credit":[2400000,5000000],
    #     "misc_debit":[2400000,5000000],
    #     "desc": "rich"
    # },
    lower_education = int(rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "posh"
    jewellery  = 0 if random.random() > 0.9 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1]))
    car       = random.randint(obj['car'][0], obj['car'][1])
    bike      = random.randint(obj['bike'][0], obj['bike'][1])
    misc_credit = int(rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    tax       = tax_bracket(misc_credit)
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data.csv', 'a') as f:
        f.write(','.join([str(i) for i in new_data]) + '\n')

obj = o['rich_business']
for i in range(no_of_points):
    # "rich_business": {
    #     "lower_education": [0.15,0.20],
    #     "higher_education": [0.20,0.25],
    #     "area":["posh"],
    #     "jewellery":[0,500000],
    #     "car":[1,5],
    #     "bike":[0,3],
    #     "misc_credit":[2400000,7500000],
    #     "misc_debit":[2400000,7500000],
    #     "desc": "rich_business"
    # },
    lower_education = int(rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "posh"
    jewellery  = 0 if random.random() > 0.9 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1]))
    car       = random.randint(obj['car'][0], obj['car'][1])
    bike      = random.randint(obj['bike'][0], obj['bike'][1])
    misc_credit = int(rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    tax       = tax_bracket(misc_credit)
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data.csv', 'a') as f:
        f.write(','.join([str(i) for i in new_data]) + '\n')

obj = o['elite']
for i in range(no_of_points):
    # "elite": {
    #     "lower_education": [0.13,0.17],
    #     "higher_education": [0.17,0.23],
    #     "area":["posh"],
    #     "jewellery":[0,1000000],
    #     "car":[1,10],
    #     "bike":[0,5],
    #     "misc_credit":[5000000,100000000],
    #     "misc_debit":[5000000,100000000],
    #     "desc": "elite"
    # },
    lower_education = int(rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "posh"
    jewellery  = 0 if random.random() > 0.9 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1]))
    car       = random.randint(obj['car'][0], obj['car'][1])
    bike      = random.randint(obj['bike'][0], obj['bike'][1])
    misc_credit = int(rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    tax       = tax_bracket(misc_credit)
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data.csv', 'a') as f:
        f.write(','.join([str(i) for i in new_data]) + '\n')

obj = o['elite_business']
for i in range(no_of_points):
    # "elite_business": {
    #     "lower_education": [0.13,0.17],
    #     "higher_education": [0.17,0.23],
    #     "area":["posh"],
    #     "jewellery":[0,5000000],
    #     "car":[1,10],
    #     "bike":[0,5],
    #     "misc_credit":[5000000,200000000],
    #     "misc_debit":[5000000,200000000],
    #     "desc": "elite_business"
    # }
    lower_education = int(rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "posh"
    jewellery  = 0 if random.random() > 0.9 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1]))
    car       = random.randint(obj['car'][0], obj['car'][1])
    bike      = random.randint(obj['bike'][0], obj['bike'][1])
    misc_credit = int(rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    tax       = tax_bracket(misc_credit)
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data.csv', 'a') as f:
        f.write(','.join([str(i) for i in new_data]) + '\n')