init python:
    correct_answers_id = [
        "Wah, genius!",
        "Mantap!",
        "Pinter.",
        "Keren kali bah kau ini.",
        "Iya, benar! Bangga aku sama kamu."
    ]
    wrong_answers_id = [
        "Salah woi...",
        "Hmm, bukan tuh. Coba lagi ya.",
        "Oho, salah ini. Sayang sekali.",
        "Eh salah, hahaha. Coba lagi.",
        "Ahelah salah ieu mah.",
    ]
    quizdata_id = [
        {
            'question': "Siapakah orang yang memimpin proses kreatif sebuah film dan memberitahu aktor apa yang harus dilakukan?",
            'choices': [
                "Produser",
                "Penulis Naskah",
                "Sutradara",
                "Editor"
            ],
            'image' : None,
            'answer': "Sutradara"
        },
        {
            'question': "Istilah apa yang digunakan untuk lagu utama atau kumpulan lagu dalam sebuah film?",
            'choices': [
                "Naskah",
                "Casting",
                "Efek Khusus",
                "Soundtrack"
            ],
            'image' : None,
            'answer': "Soundtrack"
        },
        {
            'question': "Istilah standar untuk aktor dan aktris profesional yang memerankan peran dalam film adalah:",
            'choices': [
                "Kru",
                "Pemeran",
                "Figuran",
                "Penonton"
            ],
            'image' : None,
            'answer': "Pemeran"
        },
        {
            'question': "Manakah genre film yang berfokus pada peristiwa fiksi yang terjadi di luar angkasa atau masa depan?",
            'choices': [
                "Western",
                "Horor",
                "Fiksi Ilmiah",
                "Musikal"
            ],
            'image' : None,
            'answer': "Fiksi Ilmiah"
        },
        {
            'question': "Apakah \"sekuel\" itu?",
            'choices': [
                "Film yang dibuat sebelum film pertama",
                "Film yang didasarkan pada buku",
                "Film yang sama sekali tidak berhubungan",
                "Film yang melanjutkan cerita dari film sebelumnya"
            ],
            'image' : None,
            'answer': "Film yang melanjutkan cerita dari film sebelumnya"
        },
        {
            'question': "\"Kameo\" dalam sebuah film mengacu pada:",
            'choices': [
                "Gerakan kamera khusus",
                "Monolog yang sangat panjang dan dramatis",
                "Penampilan singkat oleh orang terkenal atau sutradara",
                "Pesan tersembunyi di latar belakang adegan"
            ],
            'image' : None,
            'answer': "Penampilan singkat oleh orang terkenal atau sutradara"
        },
        {
            'question': "Apa tujuan utama dari kredit penutup (closing credits) yang ditampilkan di akhir film?",
            'choices': [
                "Untuk menunjukkan bloopers dan adegan lucu",
                "Untuk mempromosikan sekuel",
                "Untuk mencantumkan setiap orang yang mengerjakan film tersebut",
                "Untuk memutar ulang adegan terbaik"
            ],
            'image' : None,
            'answer': "Untuk mencantumkan setiap orang yang mengerjakan film tersebut"
        },
        {
            'question': "Profesional manakah yang bertanggung jawab utama untuk menulis seluruh naskah, termasuk dialog dan aksi?",
            'choices': [
                "Sutradara",
                "Sinematografer",
                "Penulis Naskah",
                "Direktur Seni"
            ],
            'image' : None,
            'answer': "Penulis Naskah"
        },
        {
            'question': "Logo film studio terkenal manakah yang menampilkan seorang anak laki-laki kecil memancing dari bulan sabit?",
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
            'question': "Logo film studio manakah ini?",
            'choices': [
                "Warner Bros.",
                "Pixar Animation",
                "Walt Disney Company",
                "Universal Studios"
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

label quiz_indonesia:
    $ quiz_lang = "id"
    $ quiz_score = 0
    show screen scorewindow(quiz_score)
    h "Oke, kita mulai kuisnya!"
    jump quizstartID

label quizstartID:
    show harumasa at quizleft with move
    python:
        for question_items in quizdata_id:
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
                resp = renpy.random.choice(correct_answers_id)
                renpy.show_screen("reaction_popup", is_correct=True)
                renpy.sound.play("correct.mp3")
            else:
                resp = renpy.random.choice(wrong_answers_id)
                resp = f"{resp}\nJawabannya seharusnya: {question_items['answer']}"
                renpy.show_screen("reaction_popup", is_correct=False)
                renpy.sound.play("wrong.mp3")
            renpy.say(h, resp)
    jump quizendID

label quizendID:
    hide screen question_img
    show harumasa at center with move
    h "Selesai sudah kuisnya!"
    h "Skor akhirmu adalah [quiz_score] dari [len(quizdata_id)]."
    if quiz_score == len(quizdata_id):
        h "Woah! Perfect score! Tumben pinter, hahahah."
    elif quiz_score >= len(quizdata_id) * 0.7:
        h "Ehhh, bagus juga! Ternyata kamu emang tahu soal film, huh?"
    elif quiz_score >= len(quizdata_id) * 0.4:
        h "Lumayan sih... tapi sepertinya film bukan passion kamu? *ketawa kecil*"
    else:
        h "Aduh, ini sih... mungkin kamu perlu nonton film lebih banyak lagi, deh. Hehe."
    hide screen scorewindow
    jump end_day

return
