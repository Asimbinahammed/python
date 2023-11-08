import os
# dict={
#     'shyam':25,
#     'anju':24,
#     'muneer':22}

phn_no=dict({'apple':34,'orange':28})
#     print(dict)
# print(dict['22'])

print(f"phn no=> {phn_no}")

phn_num={
    'asim':7890,
    'aswin':234,
    'visu':2324
}
print(phn_num)

phn_num['anju']=4545
phn_num['paru']={'workphn':124,'ofc_phn':898}
print(phn_num)
print(phn_num.get('paru'))
del phn_num['asim']
print(phn_num.keys())
print(phn_num.values())
desiredValue=2324
keys_with_desired_value = [key for key, value in phn_num.items() if value == desiredValue]
print(keys_with_desired_value)

os.system('clear')
print(phn_num.get('anju'))