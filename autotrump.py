import random

number0 = random.randint(0,5)
number1 = random.randint(0,5)
number2 = random.randint(0,5)
number3 = random.randint(0,5)
number4 = random.randint(0,5)
number5 = random.randint(0,5)

adjective1 = ["TRANSGENDER ", "LIBERAL ", "COMMUNIST ", "SOCIALIST ", "AMERICA HATING ", "DEMOCRAT "]
adjective2 = ["LOSER ", "ANARCHIST ", "ATHEIST ", "JUDGE ", "TRAITOR ", "LIAR "]
name = ["HILARY CLINTON ", "BARACK HUSSEIN OBAMA ", "FAKE NEWS MEDIA ", "POPE ", "RIOTERS ", "FAUCI "]
action = ["HATES ", "LOVES ", "SUPPORTS ", "OPPOSES ", "FIGHTS FOR ", "STANDS AGAINST ",]
thing = ["AMERICA! ", "THIS GREAT NATION! ", "ME AND MY RIGHTFUL AGENDA! ", "THE CONSTITUTION! ", "CHRISTIANITY! ", "GOD! "]
reaction = ["MAKE AMERICA GREAT!!!", "SAD!", "THIS WILL NOT STAND!", "GOD BLESS AMERICA!", "WRONG!", "GOD IS GOOD!"]

print(adjective1[number0] + adjective2[number1] + name[number2] + action[number3] + thing[number4] + reaction[number5])

