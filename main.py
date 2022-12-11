import random
question_data = [
    {"question": "A slug's blood is green.", "answer": "True"},
    {"question": "The loudest animal is the African Elephant.", "answer": "False"},
    {"question": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"question": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {
        "question": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.",
        "answer": "True"},
    {"question": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
     "answer": "False"},
    {"question": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"question": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"question": "Google was originally called 'Backrub'.", "answer": "True"},
    {"question": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"question": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"question": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


print("Wellcome to quiz!!! GOOD LUCK!!!")
print("Choose the correct answer!!!")



print("please answer the follwing questions by saying 'True' or 'False' ")
Score = 0
for question_num in range(len(question_data)):
    question = question_data[question_num]["question"]
    actual_answer = question_data[question_num]["answer"]
    user_answer = input(f"{question_num+1},{question} (True/False): ").title()
    if user_answer == actual_answer:
        print("you are correct!!")
        Score += 1
    else:
        print("Sorry, you aren't correct!! ")
print("Thank you for taking the quiz")
print(f"Your final score is {Score}/{len(question_data)}")

