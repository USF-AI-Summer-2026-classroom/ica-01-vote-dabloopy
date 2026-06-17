class Candidate:

    def __init__(self, name, leaning):
        self.name = name
        self.leaning = leaning

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
