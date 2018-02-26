# with open("small.in", "r") as f:
#     r= f.read()
#     f=list(list(r))
    
#     print(f)
    # for i in f: 
    #     list_pizza = list(i)
    #     list_pizza.pop()
    #     print(list_pizza)
    # for i in list_pizza:
    #     z = zip(i,i)
    #     print(z)

# loading file in program
with open("small.in") as file:
    lines = [line.split() for line in file]

# declaration of variables for cutting pizza
numbers = lines[0]
R = int(numbers[0]) # rows
C = int(numbers[1]) # columns
MIN = int(numbers[2]) # min of each ingredient per slice
MAX = int(numbers[3]) # max cells per slice

#remove numbers from input data
lines.remove(lines[0])

#'create' pizza list
pizza = []
#iterator
i=0
while(i < len(lines)):
	temp = lines[i]
	curStr = temp[0]
	curList = list(curStr)
	pizza.append(curList)
	i += 1
p_1 = zip(pizza[5][0],pizza[4][0],pizza[3][0],pizza[2][0],pizza[1][0])
p_2 = zip(pizza[4][1],pizza[4][1],pizza[3][1],pizza[2][1],pizza[1][1])
p_3 = zip(pizza[3][2],pizza[4][2],pizza[3][2],pizza[2][2],pizza[1][2])
p_4 = zip(pizza[2][3],pizza[4][3],pizza[3][3],pizza[2][3],pizza[1][3])
p_5 = zip(pizza[1][4],pizza[4][4],pizza[3][4],pizza[2][4],pizza[1][4])
p_0 = (pizza[0][6],pizza[0][5],pizza[0][4],pizza[0][3],pizza[0][2])
p_0_1 = (pizza[0][1],pizza[0][0])
print(pizza)
print((p_1,p_2,p_3,p_4,p_5, p_0, p_0_1))













        # list_pizza.pop()
        # for l in list_pizza:
        #     ln = list_pizza
        #     for x in ln:
        #         d = zip(x[0])
        #         print(d)
        # #     if ln == 0:
        # #         print("T")

        # #     else:
        # #         print("M")
        # print("end")