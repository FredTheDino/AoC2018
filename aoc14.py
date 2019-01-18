max_recipes = 293801
#max_recipes = 2018
#max_recipes = 9
#max_recipes = 5
in_data = 293801
#in_data = 59414
#in_data = 51589

uid = [int(x) for x in str(in_data)]
print(uid)

a = 0
b = 1
recipes = [3, 7]
done = False
while not done: #num_recipes < (max_recipes + 10):
    c = recipes[a] + recipes[b]
    for d in str(c):
        recipes.append(int(d))

    a = (a + recipes[a] + 1) % len(recipes)
    b = (b + recipes[b] + 1) % len(recipes)

    for i in range(-2, 1):
        start = len(recipes) - len(uid) - i - 2
        if start < 0:
            continue
        match = True
        for e, d in enumerate(uid):
            #print(len(recipes), start, e)
            if recipes[start + e] != d:
                match = False
                break
        if match:
            print(start)
            done = True
            break

