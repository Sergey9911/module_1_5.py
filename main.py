immuttable_var= 1,2, True
print(immuttable_var)
immuttable_var[1] = 3 # нельзя изменять элемент внутри кортежа в скобках
print(immuttable_var)

mutable_list = ["apple", "orange", "car"]
print(mutable_list)
mutable_list[2] = "peach"
print(mutable_list)