from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer):
        pass

class MCQQuestion(Question):
    def evaluate_answer(self, answer):
        if answer == "B":
            print("Correct Answer")
        else:
            print("Wrong Answer")

class TrueFalseQuestion(Question):
    def evaluate_answer(self, answer):
        if answer == True:
            print("Correct Answer")
        else:
            print("Wrong Answer")

class DescriptiveQuestion(Question):
    def evaluate_answer(self, answer):
        if len(answer) >= 20:
            print("Answer Accepted")
        else:
            print("Answer Too Short")

MCQQuestion().evaluate_answer("B")
TrueFalseQuestion().evaluate_answer(True)
DescriptiveQuestion().evaluate_answer("Python is a programming language")