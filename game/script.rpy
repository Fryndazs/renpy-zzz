define b = Character("Belle", image="belle.png")
define h = Character("Harumasa", image="harumasa.png", color="#3D96A2")

transform belleshort :
    yalign -1.0

transform center :
    xalign 0.5
    yalign 0

transform left :
    xalign 0.05
    yalign 0

transform right :
    xalign 0.85
    yalign 0

label start:

    queue music ["leisure.mp3", "freedom.mp3", "passion.mp3"] fadein 1.0

    scene randomplay outside display :
        size (1920, 1080)
    show harumasa at center
    h "The video store..."

    show harumasa at left
    with move
    show belle at right, belleshort
    with moveinright
    b "Fancy running into you again~"   
    h "...That's what you thought I'd say, right? Not this time!"
    h "I came all this way just to see you."
    menu:
        extend ''
        "That's a surprise.":
            jump choice1_surprise
        "That's scary.":
            jump choice2_scary

    label choice1_surprise:
        b "That's a surprise."
        h "Mhm. I'm actually quite surprised myself."
        jump choice1_done
    label choice2_scary:
        b "That's scary."
        h "Sigh... What's there to be afraid of? It's not like I'm going to eat you."
        jump choice1_done

    label choice1_done:
    h "Let's just say I randomly decided to come by."
    h "Hmm... To be honest, isn't it a bit awkward that we're talking outside like this?"
    h "Aren't you going to invite me in to sit down?"
    b "Okay, come in and have a seat!"
    h "Great, I hope I'm not disturbing your business!"

    scene randomplay counter
    with fade
    show harumasa at center
    h "Ahhh, no matter how many times I visit, I can't help but admire how cozy your shop's atmosphere is."
    h "If I get the chance in the future, I'd like to open a small shop like this too."
    h "Maybe I could even take over a store near you."
    show harumasa at left with moveinleft
    show belle at right, belleshort with moveinright

    menu:
        extend ''
        "You could franchise with me.":
            jump option_franchise
        "We can open a store together.":
            jump option_together

    label option_franchise:
        show belle at right, belleshort
        show harumasa at left
        b "You could franchise with me."
        h "Haha, sure! I didn't know you had ambitions to run a chain of stores..."
        jump second_floor
    label option_together:
        show belle at right, belleshort
        show harumasa at left
        b "We can open a store together."
        h "Keep talking like that, and I might take it seriously."
        jump watch_movies

    label second_floor:
        b "Let's go to the second floor and sit down!"
        h "Sure! So you have a second floor... sounds pretty mysterious."

        scene belleroom
        with fade
        show harumasa at center
        h "Wait, this isn't your room, is it?"

        menu:
            extend ''
            "It is":
                jump true_room
            "It's actually my brother's room.":
                jump false_room
        
        label true_room:
            $ menu_flag = True
            show belle at right, belleshort
            show harumasa at left
            b "It is my room."
            h "I knew it!"
            jump littlechat

        label false_room:
            $ menu_flag = False
            show belle at right, belleshort
            show harumasa at left
            b "It's actually my brother's room."
            h "Hmm... Do I look like someone who's that easy to fool?"
            h "This room is just like you, warm and cozy."
            h "Or rather... it feels like home. It makes me a bit envious."
            h "Ah, let's not dwell on that. This is a rare chance to visit your place - let's talk about something lighter."
            jump littlechat
        
    label littlechat:
        hide belle
        hide harumasa
        "{i}You enjoy chatting with Harumasa about the various little things happening in your lives lately...
        Even though his job as an Executive Officer keeps him busy, his life is still vibrant and fulfilling, which is reassuring.{/i}"
        jump end_day

    # this remains unfinished lmaooo this for quick quiz la
    # put it after watchmovies cuz littlechat seems too long for it
    label quickQuiz:
        show harumasa at center
        h "Oh yeah, I almost forgot!"
        h "What about a quick quiz? If you get it right, I'll treat you to something nice!"
        h "The quiz is simple, it revolves around {b}movies{/b} or {b}video tapes{/b}."
        h "But first, what language would you like the quiz to be in?"
        menu:
            extend ''
            "English":
                jump quiz_english
            "Bahasa Indonesia":
                jump quiz_indonesia
    # ill work on this later i need to sleep tbh
        
    label watch_movies:
        h "By the way, since we have the chance, how about watching a movie together or something?"
        h "Coming to a video store without watching a movie together just doesn't feel right, doesn't it?"

        scene staff couch :
            size (1920, 1080)
        with fade 
        hide harumasa
        hide belle
        "{i}You picked a popular movie with Harumasa and enjoyed it together.
        How to put it? Harumasa's sharp critique should be published in the newspapers!{/i}"
        jump end_day

    label end_day:
        scene randomplay corner :
            size (1920, 1080)
        with fade
        show harumasa at left
        show belle at right, belleshort
        h "Alright, it's getting late. I should be on my way."

        scene randomplay outside evening :
            size (1920, 1080)
        with fade
        show harumasa at left
        show belle at right, belleshort
        h "Thanks for your hospitality today!"
        h "Next time, you should come over to my place!"
        h "Ah... But the troublemaker at my place has a bad temper."
        h "If you come over, you'd better watch out for its claws..."
        b "Haha, I'll be careful then. See ya later!"

    return
