immutable_var = 1,2,3,4, 'title'
print(immutable_var)
immutable_var [4]= 'tite kubo'
print(immutable_var)
# Кортеж не поддерживает обращение по элементам.
mutable_list = 1,2,3,4, 'title'
mutable_list = list(mutable_list)
mutable_list [4]= 'tite kubo'
print(mutable_list)