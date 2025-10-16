transform reaction_float_fade:
    alpha 0.0
    parallel:
        ease 0.1 alpha 1.0
        0.5
        ease 0.3 alpha 0.0
    parallel:
        ease 0.2 yoffset -50

transform reaction_fade:
    alpha 0.0
    yoffset 40
    parallel:
        ease 0.15 alpha 1.0
        0.8
        ease 0.35 alpha 0.0
    parallel:
        ease 0.2 yoffset 50

screen scorewindow(score) :
    frame :
        xpos 1400
        ypos 50
        xsize 250
        ysize 100
        padding (15, 5, 0, 0)
        vbox:
            label "Score:"
            text "[quiz_score]"

screen question_img(item):
    if item.get('image', None):
        add item['image']:
            align (0.45, 0.4)
            
screen quizchoice(items):
    vbox:
        align (0.9, 0.4)
        spacing 20
        for i, choice in enumerate(items['choices']):
            textbutton choice:
                style "quiz_choice_button"
                action Return(choice)

style quiz_choice_button:
    xsize 700

screen reaction_popup(is_correct):
    tag transient
    if is_correct:
        python:
            import random
            rand_x = random.randint(100, 700)
            rand_y = random.randint(200, 700)
        add "reactions/yippee@3.png":
            xpos rand_x
            ypos rand_y
            xanchor 0.5
            yanchor 0.5
            at reaction_float_fade
    else:
        add "reactions/hehe.png":
            xpos 450
            yalign 0.1
            at reaction_fade
            if question_image is not None:
                xpos 350
            
    timer 2 action Hide("reaction_popup")

    
