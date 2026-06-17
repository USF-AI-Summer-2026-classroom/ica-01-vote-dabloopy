from candidate import Candidate
from voter import Voter

import random


class VotingSystem:
    def __init__(self):
        self.candidates = []
        self.voters = []

    def generate_candidates(self, count):
        names = ['Aang', 'Katara', 'Sokka', 'Zuko', 'Iroh', 'Appa', 'Momo', 'Toph', 'Azula', 'Suki', 'Ozai', 'Mai', 'Ty']
        self.candidates = [
            Candidate(
                name=names[i],
                leaning=random.uniform(-1.0, 1.0)
            )
            for i in range(count)
        ]

    def generate_voters(self, count):
        self.voters = [
            Voter(
                id=i + 1,
                leaning=random.uniform(-1.0, 1.0)
            )
            for i in range(count)
        ]

    def run_election(self, eliminated_candidates):
        # results is dictionary W/ candidate names & zero votes
        results = {candidate.name: 0 for candidate in self.candidates}

        #loop through voters -> get top choice using queue method & count votes
        for voter in self.voters:
            candidate_choice = voter.get_candidate(eliminated_candidates)  
            if candidate_choice:
                results[candidate_choice.name] += 1
        return results
    
    def election_results(self, results, eliminated_candidates):
        current_results = {
            name: votes for name, votes in results.items()
            if name not in eliminated_candidates
        }

        total_curr_votes = sum(current_results.values())

        if total_curr_votes == 0:
            return [], 0.0, [], 0.0

        high_vote = max(current_results.values())
        low_vote = min(current_results.values())

        max_votes = (high_vote / total_curr_votes) * 100
        min_votes = (low_vote / total_curr_votes) * 100

        winner = [name for name, votes in current_results.items() if votes == high_vote]
        loser = [name for name, votes in current_results.items() if votes == low_vote]

        return winner, max_votes, loser, min_votes

if __name__ == "__main__":
    voting_system = VotingSystem()

    voting_system.generate_candidates(5)
    voting_system.generate_voters(100)

    print("Candidates:")
    for candidate in voting_system.candidates:
        print(candidate)

    print("\nVoters:")
    for voter in voting_system.voters:
        print(voter)

    #initialize voter queues
    for voter in voting_system.voters:
        voter.generate_rankings(voting_system.candidates)

    winner_found = False
    eliminated_candidates = []
    rounds = 0
    #run election rounds until a winner is found
    while not winner_found:
        rounds += 1
        print(f"\n----------- Election Has Started -----------  ")
        #get election results, determine winners & losers
        results = voting_system.run_election(eliminated_candidates)
        winner, max_votes, loser, min_votes = voting_system.election_results(results, eliminated_candidates)

        #error detection
        if not winner:
            print("No votes or candidate available")
            break

        #if winner is found
        if max_votes > 50.0:
            winner_found = True
            print(f"\nMajority has been reached! Round {rounds} standings:")
            for name, votes in results.items():
                if name in eliminated_candidates:
                    continue
                else:
                    percent = (votes / len(voting_system.voters)) * 100
                    print(f"\n  - {name} got {percent:.2f}% of votes")
            print(f"\nThe winner is {winner[0]} with {max_votes:.2f}% of the vote")
        
        else:
            print(f"\nMajority was not reached! Round {rounds} standings:")
            for name, votes in results.items():
                if name in eliminated_candidates:
                    continue
                else:
                    percent = (votes / len(voting_system.voters)) * 100
                    print(f"\n  - {name} got {percent:.2f}% of votes")
            print(f"\nEliminating {loser[0]} with only {min_votes:.2f}% of votes")
            eliminated_candidates.extend(loser)

