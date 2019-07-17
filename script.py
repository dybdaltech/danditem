import json
import random
base_items = open('simple_base_items.json', 'r')
t1_mods = open('t1_mods.json', 'r')
item_data = json.load(base_items)
mod_data = json.load(t1_mods)




suffixes = []
prefixes = []
print('adding mods to memory')
for amount in range(5):
    mods_amount = random.randint(0, 1)
    item = random.choice(item_data)
    for mod in mod_data:
        if(mod['type'] == 'prefix'):
            prefixes.append(mod)
        if(mod['type'] == 'suffix'):
            suffixes.append(mod)
    p = {}
    s = {}
    delta_mods = [suffixes, prefixes]
    if(mods_amount == 1):
        p = random.choice(prefixes)
        s = random.choice(suffixes)
    else:
        p_or_s = random.choice(delta_mods)
        decision = random.choice(p_or_s)
        if(decision["type"] == "suffix"):
            s = decision
            p['description'] = ""
            p['name'] = ""
        else:
            p = decision
            s['description'] = ""
            s['name'] = ""

    final = str(p['name']) + " " + item["name"] + " " + str(s['name'])
    item_name = item['name']
    item_type = item['type']
    p_description = p['description']
    s_description = s['description']
    print("----------------------------------------------------")
    print(
        f"{final}\n"+
        f"{item_name} " + f"| {item_type}\n"+
        f"<<Mod description>>\nPrefix> {p_description}" + f"\nSuffix> {s_description}\n"
    )
    