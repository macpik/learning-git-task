shopping_dict = {"piekarnia": ["chleb", "bułki", "pączek"], "warzywniak": ["marchew", "seler", "rukola"]}
count = 0
for key,value in shopping_dict.items():
    if isinstance (value, list) :
      count += len(value)
      print(f'Idę do: {key.upper()}, i kupuje tam: {value}')
print(f' W sumie kupuje {count}')