#beverage_code = int(input("Enter beverage code: "))
beverage_binary = bin(int(input("Enter beverage code: ")))
bevbi = beverage_binary[2:]

bev_type = 'coffee'
bev_milk = 'no milk'
bev_sugar = 'no sugar'
bev_size = 'small'



if bevbi[0] == '1':
    bev_type = 'tea'
if bevbi[1] == '1':
    bev_milk = 'milk'
if bevbi[2] == '1':
    bev_sugar = 'sugar'
if bevbi[3] == '1':
    bev_size = 'large'

print("You have ordered a",bev_size,bev_type,"with",bev_milk,"and",bev_sugar)


