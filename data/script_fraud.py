import json
import random

no_of_points = 100000

def tax_bracket(credit):
    if credit <= 250000:
        return 0
    elif credit < 500000:
        return (credit - 250000) * 0.05
    elif credit < 1000000:
        return (credit - 500000) *  0.2 + 250000 * 0.05
    else:
        return (credit - 1000000) * 0.3 + 500000 * 0.2 + 250000 * 0.05

with open('data_fraud.csv', 'a') as f:
    f.write(','.join(['lower_education', 'higher_education', 'area', 'jewellery', 'car', 'bike', 'tax', 'misc_credit', 'misc_debit']) + '\n')


def rand_range(a, b):
    return (b-a) * random.random() + a
with open('template-2.json', 'r') as f:
    o = json.load(f)

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
    lower_education = int(3 * rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(10 * rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "middle"
    jewellery  = 0 if random.random() > 0.6 else int(3 * rand_range(obj['jewellery'][0], obj['jewellery'][1])) * 3
    car       = random.randint(obj['car'][0], obj['car'][1]) + 1
    bike      = random.randint(obj['bike'][0], obj['bike'][1]) + 1
    misc_credit = int(rand_range(obj["misc_credit"][0] / 10, obj["misc_credit"][1] / 2))
    tax       = tax_bracket(misc_credit if random.random() > 0.2 else misc_credit * random.random())
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data_fraud.csv', 'a') as f:
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
    lower_education = int(3 * rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(10 * rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "posh"
    jewellery  = 0 if random.random() > 0.6 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1])) * 3
    car       = random.randint(obj['car'][0], obj['car'][1]) + 1
    bike      = random.randint(obj['bike'][0], obj['bike'][1]) + 1
    misc_credit = int(rand_range(obj["misc_credit"][0] / 10, obj["misc_credit"][1] / 2))
    tax       = tax_bracket(misc_credit if random.random() > 0.2 else misc_credit * random.random())
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data_fraud.csv', 'a') as f:
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
    lower_education = int(3 * rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(10 * rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "posh"
    jewellery  = 0 if random.random() > 0.6 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1])) * 3
    car       = random.randint(obj['car'][0], obj['car'][1] + 3) 
    bike      = random.randint(obj['bike'][0], obj['bike'][1] + 3)
    misc_credit = int(rand_range(obj["misc_credit"][0] / 20, obj["misc_credit"][1] / 5))
    tax       = tax_bracket(misc_credit if random.random() > 0.2 else misc_credit * random.random())
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data_fraud.csv', 'a') as f:
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
    lower_education = int(3 * rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(10 * rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "posh"
    jewellery  = 0 if random.random() > 0.6 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1])) * 3
    car       = random.randint(obj['car'][0], obj['car'][1] + 3)
    bike      = random.randint(obj['bike'][0], obj['bike'][1] + 3)
    misc_credit = int(rand_range(obj["misc_credit"][0] / 100,obj["misc_credit"][1] / 10))
    tax       = tax_bracket(misc_credit if random.random() > 0.2 else misc_credit * random.random())
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data_fraud.csv', 'a') as f:
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
    lower_education = int(3 * rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(10 * rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "posh"
    jewellery  = 0 if random.random() > 0.6 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1])) * 3
    car       = random.randint(obj['car'][0], obj['car'][1] + 3)
    bike      = random.randint(obj['bike'][0], obj['bike'][1] + 3)
    misc_credit = int(rand_range(obj["misc_credit"][0] / 100, obj["misc_credit"][1] / 10))
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    tax       = tax_bracket(misc_credit if random.random() > 0.2 else misc_credit * random.random())
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data_fraud.csv', 'a') as f:
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
    lower_education = int(3 * rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(10 * rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "posh"
    jewellery  = 0 if random.random() > 0.6 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1])) * 3
    car       = random.randint(obj['car'][0], obj['car'][1] + 3)
    bike      = random.randint(obj['bike'][0], obj['bike'][1] + 3)
    misc_credit = int(rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    misc_debit = int(rand_range(obj["misc_debit"][0] / 100, obj["misc_debit"][1] / 10))
    tax       = tax_bracket(misc_credit if random.random() > 0.2 else misc_credit * random.random())
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data_fraud.csv', 'a') as f:
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
    lower_education = int(3 * rand_range(obj["lower_education"][0],obj["lower_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))     
    higher_education = int(10 * rand_range(obj["higher_education"][0],obj["higher_education"][1]) * rand_range(obj["misc_credit"][0],obj["misc_credit"][1]))
    area      = "posh"
    jewellery  = 0 if random.random() > 0.6 else int(rand_range(obj['jewellery'][0], obj['jewellery'][1])) * 3
    car       = random.randint(obj['car'][0], obj['car'][1] + 3)
    bike      = random.randint(obj['bike'][0], obj['bike'][1] + 3)
    misc_credit = int(rand_range(obj["misc_credit"][0] / 100, obj["misc_credit"][1] / 10))
    tax       = tax_bracket(misc_credit if random.random() > 0.2 else misc_credit * random.random())
    misc_debit = int(rand_range(obj["misc_debit"][0],obj["misc_debit"][1]))
    new_data = [lower_education, higher_education, area, jewellery, car, bike, tax, misc_credit, misc_debit]
    with open('data_fraud.csv', 'a') as f:
        f.write(','.join([str(i) for i in new_data]) + '\n')