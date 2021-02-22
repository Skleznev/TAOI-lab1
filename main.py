from apyori import apriori


def convertResult(input):
    output = []
    for e in input:
        output.append([list(e.items), e.support])
    return sorted(output, key=lambda x: x[1])


datContent = [i.strip().split() for i in open("./retail.dat").readlines()]

for sup in [0.01, 0.03, 0.05, 0.10, 0.15, 0.20]:
    f = open(str(sup) + '.txt', 'w')
    results = list(apriori(datContent, min_support=sup))
    for item in convertResult(results):
        f.write(str(item) + '\n')
