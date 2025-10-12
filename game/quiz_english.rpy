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
        "Sorry, that's not the answer."
    ]

label quiz_english:
    $ quiz_lang = "en"
    $ quiz_score = 0
    show screen scorewindow(quiz_score)
    h "Great! Let's get started with the quiz."
    jump q1en

label q1en:
    show harumasa at left with move
    $ question = "Who is the person that leads the creative process of a film and tells the actors what to do?"
    h "[question]"
    $ answers = [
        "Producer",
        "Screenwriter",
        "Director",
        "Editor"
    ]
    menu:
        extend ''
        "Producer":
            $ resp = renpy.random.choice(wrong_answers)
            h "[resp]"            
            jump q2en
        "Screenwriter":
            $ resp = renpy.random.choice(wrong_answers)
            h "[resp]"           
            jump q2en
        "Director":
            $ quiz_score += 1
            $ resp = renpy.random.choice(correct_answers)
            h "[resp]"          
            jump q2en
        "Editor":
            $ resp = renpy.random.choice(wrong_answers)
            h "[resp]"
            jump q2en

label q2en:
    $ question = "What term is used for a movie's main song or collection of songs?"
    h "[question]"
    $ answers = [
        "Screenplay",
        "Casting",
        "Special Effects",
        "Soundtrack"
    ]
    menu:
        extend ''
        "Screenplay":
            $ resp = renpy.random.choice(wrong_answers)
            h "[resp]"           
            jump q3en   
        "Casting":
            $ resp = renpy.random.choice(wrong_answers)
            h "[resp]"            
            jump q3en
        "Special Effects":
            $ resp = renpy.random.choice(wrong_answers)
            h "[resp]"
            jump q3en
        "Soundtrack":
            $ quiz_score += 1
            $ resp = renpy.random.choice(correct_answers)
            h "[resp]"
            
            jump q3en

label q3en:
    $ question = "The standard term for the professional actors and actresses who perform the roles in a film is the:"
    h "[question]"
    $ answers = [
        "Crew",
        "Cast",
        "Extras",
        "Audience"
    ]
    menu:
        extend ''
        "Crew":
            $ resp = renpy.random.choice(wrong_answers)
            h "[resp]"
            jump q4en
        "Cast":
            $ quiz_score += 1
            $ resp = renpy.random.choice(correct_answers)
            h "[resp]"
            
            jump q4en
        "Extras":
            $ resp = renpy.random.choice(wrong_answers)
            h "[resp]"
            jump q4en
        "Audience":
            $ resp = renpy.random.choice(wrong_answers)
            h "[resp]"
            jump q4en

    show screen answerwindow(answers, answer_actions, question_text=question)
    return