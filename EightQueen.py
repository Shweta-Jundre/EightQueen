import random
class EightQueen:

    def __init__(self):
        self.population = 0


    def initial_population(size): #making initial population
        return [random.randint(1, nq) for _ in range(nq)]

    def score(sequence):
        horizontal_collisions = sum([sequence.count(queen)-1 for queen in sequence])/2
        diagonal_collisions = 0

        n = len(sequence)
        left_diagonal = [0] * 2*n
        right_diagonal = [0] * 2*n
        for i in range(n):
            left_diagonal[i + sequence[i] - 1] += 1
            right_diagonal[len(sequence) - i + sequence[i] - 2] += 1

        diagonal_collisions = 0
        for i in range(2*n-1):
            counter = 0
            if left_diagonal[i] > 1:
                counter += left_diagonal[i]-1
            if right_diagonal[i] > 1:
                counter += right_diagonal[i]-1
            diagonal_collisions += counter / (n-abs(i-n+1))

        return int(maxScore - (horizontal_collisions + diagonal_collisions)) #28-(2+3)=23

    def probability(self,sequence, score):
        return score(sequence) / maxScore

    def random_pick(self,population, probabilities):
        populationWithProbabilty = zip(population, probabilities)
        total = sum(w for c, w in populationWithProbabilty)
        r = random.uniform(0, total)
        upto = 0
        for c, w in zip(population, probabilities):
            if upto + w >= r:
                return c
            upto += w
        assert False, "Shouldn't get here"

    def cross_over(self,x, y): #doing cross_over between two sequences
        n = len(x)
        c = random.randint(0, n - 1)
        return x[0:c] + y[c:n]

    def mutate(self,x):  #randomly changing the value of a random index of a sequence
        n = len(x)
        c = random.randint(0, n - 1)
        m = random.randint(1, n)
        x[c] = m
        return x

    def genetic_queen(self,population, score):
        mutation_probability = 0.03
        new_population = []
        probabilities = [self.probability(n, score) for n in population]
        for i in range(len(population)):
            x = self.random_pick(population, probabilities) #best sequence 1
            y = self.random_pick(population, probabilities) #best sequence 2
            child = self.cross_over(x, y) #creating two new sequences from the best 2 sequences
            if random.random() < mutation_probability:
                child = self.mutate(child)
            #print_sequence(child)
            new_population.append(child)
            if score(child) == maxScore: break
        return new_population

    def print_sequence(self,chrom):
        print(str(chrom))

def main():
    EightQueen()

if __name__ == "__main__":
    main()
    nq = 8
    maxScore = (nq*(nq-1))/2  # 8*7/2 = 28
    population = [EightQueen.initial_population(nq) for _ in range(100)]

    generation = 1

    while not maxScore in [EightQueen.score(chrom) for chrom in population]:
        population = EightQueen.genetic_queen(EightQueen(),population,EightQueen.score)
        generation += 1
    chrom_out = []
    for chrom in population:
        if EightQueen.score(chrom) == maxScore:
            print("");
            chrom_out = chrom
            EightQueen.print_sequence(EightQueen,chrom)

    print()
