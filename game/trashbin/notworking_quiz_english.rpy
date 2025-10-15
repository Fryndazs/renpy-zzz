# default quiz_questions = [
#     {   
#         "question": "Who is the person that leads the creative process of a film and tells the actors what to do?",
#         "image": None,
#         "choices": ["Producer", "Screenwriter", "Director", "Editor"],
#         "answer": "Director"
#     },
#     {
#         "question": "What term is used for a movie's main song or collection of songs?",
#         "image": None,
#         "choices": ["Screenplay", "Casting", "Special Effects", "Soundtrack"],
#         "answer": "Soundtrack"
#     },
#     {
#         "question": "The standard term for the professional actors and actresses who perform the roles in a film is the:",
#         "image": None,
#         "choices": ["Crew", "Cast", "Extras", "Audience"],
#         "answer": "Cast"
#     },
#     {
#         "question": "Which film genre focuses on fictional events that take place in outer space or the future?",
#         "image": None,
#         "choices": ["Western", "Horror", "Science Fiction", "Musical"],
#         "answer": "Science Fiction"
#     },
#     {
#         "question": "What is a \"sequel\"?",
#         "image": None,
#         "choices": ["A film that is made before the first film", "A film based on a book", "A completely unrelated film", "A film that continues the story of an earlier film"],
#         "answer": "A film that continues the story of an earlier film"
#     },
#     {
#         "question": "A \"cameo\" in a movie refers to:",
#         "image": None,
#         "choices": ["A special camera movement", "A very long, dramatic monologue", "A brief appearance by a famous person or the director", "A hidden message in the background of a scene"],
#         "answer": "A brief appearance by a famous person or the director"
#     },
#     {   
#         "question": "What is the primary purpose of the closing credits (or end credits) shown at the very end of a movie?",
#         "image": None,
#         "choices": ["To show bloopers and funny scenes", "To promote the sequel", "To list every person who worked on the film", "To replay the best scenes"],
#         "answer": "To list every person who worked on the film"
#     },
#     {
#         "question": "Which professional is primarily responsible for writing the entire script, including dialogue and action?",
#         "image": None,
#         "choices": ["Director", "Cinematographer", "Screenwriter", "Art Director"],
#         "answer": "Screenwriter"
#     },
#     {
#         "question": "Which famous film studio logo features a small boy fishing from a crescent moon?",
#         "image": "dreamworks.png",
#         "choices": ["Pixar Animation", "Walt Disney Pictures", "DreamWorks Pictures", "Studio Ghibli"],
#         "answer": "DreamWorks Pictures"
#     },
#     {
#         "question": "Which film studio logo is this?",
#         "image": "warnerbros.png",
#         "choices": ["Warner Bros.", "Pixar Animation", "Walt Disney Company", "Universal Studios"],
#         "answer": "Warner Bros."
#     },
# ]

# default wrong_responses = [
#     "Incorrect. The correct answer was: ",
#     "Not quite. The right answer is: ",
#     "That's not right. The answer is: ",
#     "Wrong answer. The correct one is: [answer_text]"
# ]

# default correct_responses = [
#     "Great job!",
#     "Well done!",
#     "You're doing great!",
#     "That's correct!",
#     "That's right!"
# ]

# label quiz_start:
#     # Initialize score and question index
#     $ score = 0
#     $ question_index = 0

#     # Create a shuffled, temporary copy of the questions for this quiz session
#     $ quiz_questions = renpy.random.sample(all_questions, len(all_questions))

#     # Show the first question
#     call screen quiz_screen
#     return # This return is important, it prevents the game from continuing automatically


# label correct_answer:
#     # Increment the score
#     $ score += 1

#     # Show a random "correct" response
#     $ renpy.say(None, renpy.random.choice(correct_responses))

#     # Move to the next question
#     jump next_question


# label wrong_answer:
#     # Show a random "wrong" response
#     $ renpy.say(None, renpy.random.choice(wrong_responses))

#     # Move to the next question
#     jump next_question


# label next_question:
#     # Move to the next question in the list
#     $ question_index += 1

#     # Check if there are more questions left
#     if question_index < len(quiz_questions):
#         # If yes, show the quiz screen again for the new question
#         call screen quiz_screen
#     else:
#         # If no, jump to the end of the quiz
#         jump quiz_end
#     return


# label quiz_end:
#     # Hide the quiz screen if it's still showing
#     hide screen quiz_screen

#     # Show the final score
#     "Quiz finished!"
#     "You scored [score] out of [len(quiz_questions)] points."

#     "Let's continue with the story."
#     return

# # screen quiz_choices(question_text, images, choices, q_index):
# #     vbox:
# #         spacing 20

# #         text "[question_text]" size 40 xalign 0.5

# #         # Show all images for the question
# #         hbox:
# #             spacing 10
# #             for img in images:
# #                 add img xalign 0.5 yalign 0.5

# #         text "Choose your answer:" size 30 xalign 0.5

# #         # Custom buttons for answers
# #         for i, choice in enumerate(choices):
# #             textbutton choice:
# #                 style "quiz_choice_button"
# #                 action Function(renpy.call_in_new_context, "quiz_answer", q_index, i)

# # style quiz_choice_button is default:
# #     background "#5c7aff"
# #     hover_background "#98cdff"
# #     insensitive_background "#333333"
# #     color "#fff"
# #     size 28
# #     xalign 0.5
# #     yalign 0.5
# #     padding (10, 10)

# # $ player_score = 0

# # label quiz_question:
# #     python:
# #         renpy.log("quiz_question called with current_q_index: {}".format(current_q_index))
# #     $ question = questionsEN[current_q_index]
# #     show screen quiz_choices(question["question"], question["images"], question["choices"], current_q_index)
# #     return

# # label quiz_answer(q_index, selected):
# #     python:
# #         renpy.log("quiz_answer called with q_index: {} and selected: {}".format(q_index, selected))
# #     $ question = questionsEN[q_index]
# #     if selected == question["answer"]:
# #         $ player_score += 1
# #         $ renpy.say(None, renpy.random.choice(correctanswersEN))
# #     else:
# #         $ answer_text = question["choices"][question["answer"]]
# #         $ renpy.say(None, renpy.random.choice(wronganswersEN).replace("[answer_text]", answer_text))

# #     $ current_q_index += 1

# #     if current_q_index < len(questionsEN):
# #         jump quiz_question
# #     else:
# #         jump quiz_end

