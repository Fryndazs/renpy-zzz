init python:
    correct_answers = [
        "Great job!",
        "Well done!",
        "You're doing great!",
        "That's correct!",
        "That's right!"
    ]
    wrong_answers = [
        "Oops, that's not right.",
        "Not quite, try again.",
        "That's incorrect.",
        "Nuh-uh, that's wrong.",
        "Sorry, that's not the answer.",
    ]
    quizdata_en = [
        {
            'question': "Who is the person that leads the creative process of a film and tells the actors what to do?",
            'choices': [
                "Producer",
                "Screenwriter",
                "Director",
                "Editor"
            ],
            'image' : None,
            'answer': "Director"
        },
        {
            'question': "What term is used for a movie's main song or collection of songs?",
            'choices': [
                "Screenplay",
                "Casting",
                "Special Effects",
                "Soundtrack"
            ],
            'image' : None,
            'answer': "Soundtrack"
        },
        {
            'question': "The standard term for the professional actors and actresses who perform the roles in a film is the:",
            'choices': [
                "Crew",
                "Cast",
                "Extras",
                "Audience"
            ],
            'image' : None,
            'answer': "Cast"
        },
        {
            'question': "Which film genre focuses on fictional events that take place in outer space or the future?",
            'choices': [
                "Western",
                "Horror",
                "Science Fiction",
                "Musical"
            ],
            'image' : None,
            'answer': "Science Fiction"
        },
        {
            'question': "What is a \"sequel\"?",
            'choices': [
                "A film that is made before the first film",
                "A film based on a book",
                "A completely unrelated film",
                "A film that continues the story of an earlier film"
            ],
            'image' : None,
            'answer': "A film that continues the story of an earlier film"
        },
        {
            'question': "A \"cameo\" in a movie refers to:",
            'choices': [
                "A brief appearance by a well-known actor",
                "A type of special effect",
                "A scene that is cut from the final film",
                "A musical number performed by the cast"
            ],
            'image' : None,
            'answer': "A brief appearance by a well-known actor"
        },
        {
            'question': "What is the primary purpose of the closing credits (or end credits) shown at the very end of a movie?",
            'choices': [
                "To show bloopers and outtakes",
                "To provide a summary of the film's plot",
                "To list every person involved in the film",
                "To reveal the film's box office earnings"
            ],
            'image' : None,
            'answer': "To list every person involved in the film"
        },
        {
            'question': "Which professional is primarily responsible for writing the entire script, including dialogue and action?",
            'choices': [
                "Director",
                "Screenwriter",
                "Cinematographer",
                "Editor"
            ],
            'image' : None,
            'answer': "Screenwriter"
        },
        {
            'question': "Which famous film studio logo features a small boy fishing from a crescent moon?",
            'choices': [
                "Pixar Animation",
                "Walt Disney Pictures",
                "DreamWorks Pictures",
                "Studio Ghibli"
            ],
            'image' : "dreamworks.png",
            'answer': "DreamWorks Pictures"
        },
        {
            'question': "Which film studio logo is this?",
            'choices': [
                "Warner Bros.",
                "Universal Pictures",
                "Paramount Pictures",
                "20th Century Fox"
            ],
            'image' : "warnerbros.png",
            'answer': "Warner Bros."
        }
    ]

transform quizleft :
    xalign -0.1
    yalign 0
transform imgleft :
    xalign -0.25

label quiz_english:
    $ quiz_lang = "en"
    $ quiz_score = 0
    show screen scorewindow(quiz_score)
    h "Great! Let's get started with the quiz."
    jump quizstartEN

label quizstartEN:
    show harumasa at quizleft with move
    python:
        for question_items in quizdata_en:
            question_text = question_items['question']
            question_image = question_items['image']
            
            if question_image is not None:
                renpy.show_screen("question_img", question_items)
                renpy.show("harumasa", at_list=[imgleft])
                renpy.with_statement(move)
            else:
                renpy.hide_screen("question_img")

            renpy.say(h, question_text, interact=False)
            result = renpy.call_screen("quizchoice", question_items)
            if result == question_items['answer']:
                quiz_score += 1
                resp = renpy.random.choice(correct_answers)
                renpy.show_screen("reaction_popup", is_correct=True)
                renpy.sound.play("correct.mp3")
            else:
                resp = renpy.random.choice(wrong_answers)
                resp = f"{resp}\nThe correct answer is: {question_items['answer']}"
                renpy.show_screen("reaction_popup", is_correct=False)
                renpy.sound.play("wrong.mp3")
            renpy.say(h, resp)
    jump quizendEN

label quizendEN:
    hide screen question_img
    show harumasa at center with move
    h "That's the end of the quiz!"
    h "Your final score is [quiz_score] out of [len(quizdata_en)]."
    if quiz_score == len(quizdata_en):
        h "Perfect score! Amazing job!"
    elif quiz_score >= len(quizdata_en) * 0.7:
        h "Great work! You really know your stuff."
    elif quiz_score >= len(quizdata_en) * 0.4:
        h "Not bad, but there's room for improvement."
    else:
        h "Looks like you need to brush up on your movie knowledge."
    hide screen scorewindow
    jump end_day

return