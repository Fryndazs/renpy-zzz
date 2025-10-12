screen scorewindow(score) :
    frame :
        xpos 1400
        ypos 50
        xsize 250
        ysize 80
        vbox:
            label "Score:"
            text "[score]"

screen answerwindow(answers, answer_actions, question_text=None, image_path=None):
    frame:
        xpos 1400
        ypos 200
        xsize 500
        ysize 350
        vbox:
            if question_text is not None:
                text question_text
            if image_path is not None:
                add image_path xalign 0.5
            for i, a in enumerate(answers):
                textbutton a action answer_actions[i]