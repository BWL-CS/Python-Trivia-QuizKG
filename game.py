#trivia is a list of dictionary items 
trivia = [
          { 'question': "Which animal is best adapted to survive in the hot desert?",
            'answer': 'camel',
            'options': ['polar bear', 'option b', 'option c', 'correct answer'],
          },
          { 'question': "question body goes here",
            'answer': 'correct answer',
            'options': ['option a', 'option b', 'option c', 'correct answer'],
          }
         ]

def ask_question(question, options, answer): 
    print(question)
    #display options
    for choice in options: 
        print(choice)

    #next step is taking input 
    user_choice = input("Enter your answer: ")

    #step three. see if input macthes answer
    if user_choice==answer:
        return True
    else:
        return False

def main():
    print("Starting a new Trivia game...")
    user_name = input("Enter your name: ")
    print(f"Welcome, {user_name}!")
    #going to call the ask question function in main 
    for item in trivia:
        current_question=item['question']
        current_options=item['options']
        current_answer=item['answer']
        is_correct = ask_question(current_question,current_options,current_answer)
        print(is_correct) #see if answer was right




main()
