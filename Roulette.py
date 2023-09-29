def roulette_wheel_select(population, fitness, r):
    values = []
    count = 0
    for thing in population:
        thing_fitness = fitness(thing)
        values.append(thing_fitness)
        count += thing_fitness

    running_count = 0
    for i in range(len(values)):
        running_count += values[i]/count
        values[i] = running_count

    for value in values:
        if r <= value:
            return population[values.index(value)]



def fitness_1(x):
    return x


def test_1():
    population = [0, 1, 2]
    print("Test 1:")
    for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
        print(roulette_wheel_select(population, fitness_1, r))


def fitness(x):
    return 1 # everyone has the same fitness

def test_2():
    population = ['a', 'b']
    print("\nTest 2:")
    for r in [0, 0.33, 0.49999, 0.51, 0.75, 0.99999]:
        print(roulette_wheel_select(population, fitness, r))

test_1()
test_2()

