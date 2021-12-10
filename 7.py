crabs = list(map(int,open("7-input.txt").read().split(",")))

fuelCosts = list()

x = lambda a: sum([i for i in range(1,a+1)])

for position in range(1000):
  a = sum(x(abs(crab - position)) for crab in crabs)
  fuelCosts.append(a)

print(min(fuelCosts))