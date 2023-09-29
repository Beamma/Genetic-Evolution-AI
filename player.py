from random import randint

class Player:
    def __init__(self):
        self.length = 0
        self.guessed_wrong = []
        self.guessed_right = []
        self.score = 0
        self.vary_factor = 1

        self.vowles_gene = 1
        self.common_gene = 1
        self.uncommon_gene = 1
        self.pattern_match = 1

    def set_length(self, length):
        self.length = length

    def guess_letter(self):
        common_vowels = ['a', 'e', 'i', 'o', 'u']
        common_cons = ['b', 'c', 'd', 'g', 'h', 'k', 'l', 'm', 'n','r','s','t','y']
        uncommon_cons = ['f','j', 'p', 'q','v','x','w','z']
        
        r = randint(0, self.vowles_gene + self.common_gene + self.uncommon_gene + self.pattern_match)
        
        if r <= self.vowles_gene:
            print("Vowles")
        
        elif r <= self.vowles_gene+ self.common_gene:
            print("Commom")

        elif r <= self.vowles_gene + self.common_gene + self.uncommon_gene:
            print("Uncommon")
        
        elif r <= self.vowles_gene + self.common_gene + self.uncommon_gene + self.pattern_match:
            print("Pattern Match")

    def score_counter(self, score):
        self.score += score
        print(self.score)

    def off_spring():
        pass



entity = Player()
entity.guess_letter()
