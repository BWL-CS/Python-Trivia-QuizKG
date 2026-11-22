#trivia is a list of dictionary items 
trivia = [
          { 'question': "Which animal is best adapted to survive in the hot desert?",
            'answer': 'Camel',
            'options': ['Polar bear', 'Camel', 'Penguin', 'Snake'],
          },
           { 'question': "Where do polar bears naturally live?",
            'answer': 'Artic regions',
            'options': ['Africa', 'South America', 'Arctic regions', 'Artic regions'],
           },
          { 'question': " Which animal is commonly found in tropical rainforests?",
            'answer': 'Jaguar',
            'options': ['Jaguar', 'Polar bear', 'Penguin', 'Jaguar'],
          },
          { 'question': "Which animal has thick fur to help it survive in extremely cold climates?",
            'answer': 'Arctic fox',
            'options': ['Lizard', 'Brown Bear', 'Monkey', 'Arctic fox'],
          },
           { 'question': "Where do kangaroos naturally live?",
            'answer': 'Australia',
            'options': ['Antarctica', 'Europe', 'North America', 'Australia'],
          },
          { 'question': "What helps a polar bear stay warm in freezing temperatures?",
            'answer': 'Thick fur and a layer of body fat',
            'options': ['Thin skin', 'Large ears', 'Thick fur and a layer of body fat', 'Thick fur and a layer of body fat'],
          },
           { 'question': "Which animal is adapted to living in mountainous regions with cold temperatures?",
            'answer': 'Snow leopard',
            'options': ['Snow leopard', 'Seahorse', 'Flamingo', 'Snow leopard'],
          },
          { 'question': "Which animal is native to the Himalayan mountain range?",
            'answer': 'Snow leopard',
            'options': ['Kangaroo', 'Giraffe', 'Snow leopard', 'Snow leopard'],
          },
             { 'question': "Which animal is adapted to life in the African desert?",
            'answer': 'Fennec Fox',
            'options': ['Lizard', 'Moose', 'Penguin', 'Fennec fox'],
          },
          { 'question': " Why do many animals in cold climates have smaller ears and shorter limbs?",
            'answer': 'conserve body heat',
            'options': ['To conserve body heat', 'To attract predators', 'To help them swim', 'conserve body heat'],
          },
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

    # Function to calculate the percentage score
def calculate_score(total_questions, num_correct):
    score = (num_correct / total_questions) * 100
    return score

def main():
   print("Starting a new Animal Trivia game...")
user_name = input("Enter your name: ")
print(f"Welcome, {user_name}!")

    # Initialize the score
num_correct = 0

    # Going to call the ask question function in main
    # for item in trivia:
current_question = item['question']
current_options = item['options']
current_answer = item['answer']
is_correct = ask_question(current_question, current_options, current_answer)

print(is_correct)

if is_correct:
            num_correct += 1
            print("Correct!")
else:
            print("Incorrect!")

    # Calculate the final score
total_questions = len(trivia)
final_score = calculate_score(total_questions, num_correct)

print("\nQuiz Complete!")
print("You got", num_correct, "out of", total_questions, "correct.")
print("Your final score is:", final_score, "%")

if final_score == 100:
        print("Excellent! You got every question correct!")
elif final_score >= 80:
        print("Great job! You know a lot about animals!")
elif final_score >= 60:
        print("Good effort! Keep learning!")
else:
        print("Keep practicing! You can improve your score next time!")



        main()
        num_correct = 0
if is_correct:
      num_correct += 1

def calculate_score(total_questions, num_correct):
  score = (num_correct / total_questions) * 100
  return score


  