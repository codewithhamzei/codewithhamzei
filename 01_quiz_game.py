

print(("Welcome To Quiz Game"))

# Mcqs Correct Answer
def game():
    playing = input("Want To Play Game:")
    if playing.lower() != "yes":
        quit()

    else:   
        questions = [
                "Which of these is the largest ocean on Earth?",
                "Who is considered the author of the famous play 'Hamlet'?",
                "What is the chemical symbol for iron?",
                "Which planet is known as the Red Planet?",
                "What is the capital city of Canada?",
                "Which of these is not a mammal?",
                "Who painted the famous artwork 'The Starry Night'?",
                "In which year did World War II end?",
                "What is the tallest mountain in the world?",
                "Which gas makes up the majority of the Earth's atmosphere?"
        ]

        options = [
                ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                ["William Shakespeare", "Jane Austen", "Charles Dickens", "Leo Tolstoy"],
                ["Fe", "Au", "Ag", "Hg"],
                ["Mars", "Venus", "Jupiter", "Saturn"],
                ["Toronto", "Vancouver", "Ottawa", "Montreal"],
                ["Whale", "Bat", "Snake", "Dolphin"],
                ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"],
                ["1939", "1945", "1951", "1962"],
                ["Mount Kilimanjaro", "Mount Everest", "Mount McKinley", "Mount Fuji"],
                ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"]
        ]
        correct_answers = [3, 0, 0, 0, 2, 2, 0, 1, 1, 2]

        full_marks = 10
        obtain_marks = 0

        for i in range(0,9):
            print(questions[i],"\n") # Print Question I
            print(options[i]) # Print Answer I

            answers = int(input("Enter Correct Annwer in index: "))

            if answers-1 == correct_answers[i]: # If Answer correct +1 added
                obtain_marks += 1    
                print("Correct Answer")

            else:
                print(f"The Correct answer of this is {options[i][correct_answers[i]]} ")


        print(f"You Got {obtain_marks} out of {full_marks}")

game()
