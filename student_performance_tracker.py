
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    def calculate_average(self):
        return sum(self.scores) / len(self.scores)
    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)
