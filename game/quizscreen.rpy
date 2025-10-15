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
            
screen choice(items):
    vbox:
        align (0.9, 0.4)
        spacing 20
        for i, choice in enumerate(items['choices']):
            textbutton choice:
                style "quiz_choice_button"
                action Return(choice)

style quiz_choice_button:
    xsize 700
    
