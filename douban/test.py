tem_dict = {
    'name': 'xiao',
    'age': '18',
    'hello': 'world',
}

for i in tem_dict:
    print(i, tem_dict[i])

test = [tem_dict[i] for i in tem_dict]
print(test)