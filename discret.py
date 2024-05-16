def generate_WFFs(n):
    if n == 0:
        #      [T, F, q, p]
        return [' \033[93mT\033[0m ', ' \033[93mF\033[0m ', ' \033[93mp\033[0m ', ' \033[93mq\033[0m ']
    else:
        result = []
        for i in range(n):
            #         ['¬', '∨', '∧', '→', '↔']
            for op in [' \033[96m¬\033[0m ', ' \033[96m∨\033[0m ', ' \033[96m∧\033[0m ', ' \033[96m→\033[0m ', ' \033[96m↔\033[0m ']:
                for left in generate_WFFs(i):
                    for right in generate_WFFs(n - 1 - i):
                        result.append('(' + left + op + right + ')')
                        if len('(' + left + op + right + ')') <= n:
                            result.append(left + op + right)
        return result

print("Elements : ", ['T', 'F', 'q', 'p'])
print("Operants : ", ['¬', '∨', '∧', '→', '↔'])
n = int(input("Enter the complexity level : "))
WFFs = generate_WFFs(n)
for formula in set(WFFs):  # Using set to remove duplicates
    print(formula,"\n")

print("Total number of combinations:", len(WFFs))
print("End of the proccess")
print("Developmen Proccess")

# n = 0 total number of combinations : 0
# n = 1 total number of combinations : 80
# n = 2 total number of combinations : 3200
# n = 3 total number of combinations : 1600000
# n = 4 total number of combinations : 8960000
# n = 5 total number of combinations : MemoryError :)