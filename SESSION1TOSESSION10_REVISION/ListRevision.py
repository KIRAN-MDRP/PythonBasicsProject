l1 = []
print("Type of l1 is: ", type(l1))
l1.append(1)
l1.append("KiranKumar")
l1.append(False)
l1.append(3+5J)
l1.append(None)
l1.append(1)
l1.append(1)

print("After appending updated l1 is: ", l1)
l2 = ["KiranKumar", "SatishKumar", "SudhirKumar"]
print("l2 is: ", l2)
l1.extend(l2)
print("After extending l1 with l2: ", l1)
l3 = l1.copy()
print("l3 is: ", l3)
print("1 is present in the list l1: ", l1.count(1))
print("Index of 1 in l1 is: ", l1.index(1))
l1.insert(0,"Balaji")
print("After inserting Balaji at index 0: ", l1)
l1.pop()
l1.remove(1)
print("After removing 1 from l1: ", l1)
l1.reverse()
print("After reversing l1: ", l1)
print("Filter the list l1 and create new list with only Strings")
l1_str = []
for ele in l1:
    if isinstance(ele, str):
        l1_str.append(ele)
print("l1_str is: ", l1_str)
print("After sorting l1_str: ", sorted(l1_str))
print("After sorting l1_str in reverse order: ", sorted(l1_str, reverse=True))

stringList = ["M.M.Satyanarayana", "M.DurgaKumari", "M.BalaBalaji KiranKumar","M.SatishKumar",
              "M.SudhirKumar","M.SriLakshmiBhavani","M.AnushaJyothirmai","M.ChaithvikaSrihansi"]
intList = [23,1,4,54,6,1,-23,-54]
floatList = [2.56,1.21,9.54,2.34,1.11,0.23]
print("Ascending String Sort", sorted(stringList))
print("Ascending Integer Sort", sorted(intList))
print("Ascending Float Sort", sorted(floatList))
print("-----------------------------------------------------")
print("Descending String Sort", sorted(stringList, reverse=True))
print("Descending Integer Sort", sorted(intList, reverse=True))
print("Descending Float Sort", sorted(floatList, reverse=True))