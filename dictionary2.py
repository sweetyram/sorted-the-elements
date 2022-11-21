size = int(input("enter the numbers of elements need to be added in dictionary :"))
org_dict = {}
dic = {}
for i in range(size):
    key  = int(input("enter the key to be added:"))
    value = int(input("enetr the value to be added:"))
    org_dict[key] = value
print(org_dict)
lst1 = list(org_dict.items())
print(lst1)    