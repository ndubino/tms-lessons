my_list = [1, 2, 3, 4,1123,123,12425,215521]
max_element = my_list[0]
for i in my_list:
    if i > max_element:
        max_element = i

print(max_element)