#first half of the project
x = int(input("Input a number to get 2 lists containing all the even and odd numbers less than the inputted number: "))
i = 0
evenlist = []
oddlist = []

while i != x:
    if i % 2 == 0:
        evenlist.append(i)
    else:
        oddlist.append(i)
    i+=1

print("\nThe even list", evenlist)
print("The odd list", oddlist)

#second half of the project
fruitlist = ["cupuacu", "araza", "akebi", "cherimoya", "baluno"]
modified_fruitlist = []

for item in fruitlist:
    n = item.capitalize()
    modified_fruitlist.append(n)

print("\n", modified_fruitlist)