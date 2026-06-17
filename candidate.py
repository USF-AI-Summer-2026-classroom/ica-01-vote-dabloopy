class Candidate:

    def __init__(self, name, leaning):
        self.name = name
        self.leaning = leaning
        #adding eleiminated status to candidate
        self.eliminated = False

    def get_leaning(self):
        return self.leaning

    def get_name(self):
        return self.name

    def __repr__(self):
        return (
            f"Candidate = {self.name}, "
            f"leaning: {self.leaning:.3f}"
        )
    
    def is_eliminate(self):
        return self.eliminated

    def eliminate(self):
        self.eliminated = True

    def __repr__(self):
        return {
            "name": self.name,
            "leaning": self.leaning,
            "eliminated": self.eliminated
        }