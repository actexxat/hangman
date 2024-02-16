import random
WORDS = [
    "hello", "world", "python", "language", "programming", "computer",
    "science", "data", "algorithm", "machine", "learning", "artificial",
    "intelligence", "network", "internet", "web", "application", "software",
    "development", "database", "system", "design", "user", "interface",
    "experience", "cloud", "security", "privacy", "business", "innovation",
    "technology", "future", "present", "past", "time", "space", "universe",
    "life", "earth", "nature", "human", "animal", "plant", "food", "water",
    "air", "energy", "sun", "moon", "star", "planet", "galaxy", "black",
    "hole", "light", "dark", "day", "night", "morning", "evening", "love",
    "hate", "joy", "sadness", "fear", "anger", "happiness", "peace", "hope",
    "dream", "reality", "imagination", "creativity", "art", "music",
    "dance", "literature", "poetry", "philosophy", "history", "culture",
    "society", "politics", "economics", "science", "biology", "chemistry",
    "physics", "mathematics", "astronomy", "geology", "geography",
    "anatomy", "physiology", "psychology", "sociology", "anthropology",
    "philosophy", "ethics", "morality", "religion", "spirituality",
    "belief", "faith", "doubt", "meaning", "purpose", "life", "death",
    "existence", "soul", "mind", "body", "brain", "heart", "spirit",
    "freedom", "justice", "equality", "truth", "beauty", "goodness",
    "evil", "light", "darkness", "hope", "despair", "possibility",
    "potential", "limit", "boundary", "challenge", "obstacle",
    "opportunity", "growth", "change", "transformation", "evolution",
    "revolution", "progress", "development", "improvement",
    "innovation", "discovery", "invention", "creation", "imagination",
    "dream", "vision", "goal", "ambition", "desire", "wish",
    "love", "hate", "joy", "sadness", "fear", "anger", "peace",
    "happiness", "hope", "trust", "faith", "belief", "doubt",
    "uncertainty", "confusion", "clarity", "understanding",
    "knowledge", "wisdom", "intelligence", "reason", "logic",
    "emotion", "feeling", "sensation", "perception", "experience",
    "memory", "thought", "belief", "opinion", "judgment",
    "decision", "action", "behavior", "reaction", "consequence",
    "result", "effect", "impact", "influence", "change",
    "transformation", "evolution", "revolution", "progress",
    "development", "growth", "improvement", "innovation",
    "discovery", "invention", "creation", "imagination", "dream",
    "vision", "goal", "ambition", "desire", "wish", "hope", "faith",
    "belief", "doubt", "uncertainty", "confusion", "clarity",
    "understanding", "knowledge", "wisdom", "intelligence", "reason",
    "logic", "emotion", "feeling", "sensation", "perception", "experience",
    "memory", "thought", "belief", "opinion", "judgment", "decision",
    "action", "behavior", "reaction", "consequence", "result", "effect",
    "impact", "influence", "change", "transformation", "evolution",
    "revolution", "progress", "development", "growth", "improvement",
    "innovation", "discovery", "invention", "creation", "imagination",
    "dream", "vision", "goal", "ambition", "desire", "wish", "hope",
    "faith", "belief", "doubt", "uncertainty", "confusion", "clarity",
    "understanding", "knowledge", "wisdom", "intelligence", "reason",
    "logic", "emotion", "feeling", "sensation", "perception", "experience",
    "memory", "thought", "belief", "opinion", "judgment", "decision",
    "action", "behavior", "reaction", "consequence", "result", "effect",
    "impact", "influence", "change", "transformation"]


class Player:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.__score = 0

    def update(self, score):
        self.__score = score


class Engine:
    def __init__(self):
        self.player_name = Player().name
        self.word = list(WORDS[random.randint(0,len(WORDS) - 1)])
        self.lives = len(self.word)
        self.mistakes = 0
        self.blanks = ['-' for letter in self.word]
        self.history = []
        self.draw()

    def draw(self):
        print('-' * len(self.blanks))
        self.get_guess()

    def get_guess(self):
        while self.mistakes < len(self.word) and '-' in self.blanks:
            guess = input('Enter your guess: ')
            self.history.append(guess)
            if guess in self.word:
                index = self.word.index(guess)
                self.word[index] = '✔'
                self.blanks[index] = guess
                print(self.blanks, 'Lives: ', self.lives - self.mistakes, self.history)
            else:
                self.mistakes +=1
                print(self.blanks,'Lives: ', self.lives - self.mistakes, self.history)
                continue
        self.check_progress()

    def check_progress(self):
        if self.mistakes == len(self.word):
            print("Hard Luck!","The Correct Answer was: ", self.word)
            return 1
        score = 2*(len(self.word)) - 1 * self.mistakes
        print("GOOD JOB!", "Your Score Is: ", score)


game = Engine()
