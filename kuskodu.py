with open('/prihlasky.txt', 'r') as file:
    list_zajemci = file.readlines()
    print(list_zajemci)

def vycisteni (list_list):
  cleaned_list = []
  for name in list_list:
    newname = name.strip()
    cleaned_list.append(newname)
  cleaned_list = [item.replace("\n", "").replace("\t", "").strip() for item in list_list]
  cleaned_list = [item.replace('CZE ', 'CZE') for item in cleaned_list]
  return cleaned_list


zajemci = vycisteni(list_zajemci)
print(zajemci)




  