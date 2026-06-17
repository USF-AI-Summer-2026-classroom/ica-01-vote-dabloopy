#importing Queue class from queue_ds.py
from queue_ds import Queue

class Voter:

    def __init__(self, id, leaning):
        self.id = id
        self.leaning = leaning
        #ranked list of candidates based on voter distance
        self.rankings = Queue()

    def __repr__(self):
        return (
            f"Voter with ID={self.id}, "
            f"leaning: {self.leaning:.3f}"
        )

    def generate_rankings(self, candidates):
        #soring candidates based on distance
        distance = lambda candidate: abs(self.leaning - candidate.leaning)
        sorted_candidates = sorted(candidates, key=distance)

        #enqueue candidates closest first
        for candidate in sorted_candidates:
            self.rankings.enqueue(candidate)

    def get_candidate(self, eliminated_candidates):
        #loop queue until we find a candidate (not eliminated)
        while not self.rankings.is_empty():
            # Check front of queue
            top_choice = self.rankings.peek()

            #if candidate is eliminated remove it from queue and continue
            if top_choice.name in eliminated_candidates:
                self.rankings.dequeue()
            #else return top choice(not eliminated)
            else:
                return top_choice
        #if empty return None
        return None