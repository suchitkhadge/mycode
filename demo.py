import random

quiz = {
    "Music": 
        [
        {"Who sang the song 'Hit me baby'? ": ["Adele Kinobi", "Nick June", "Haley Smith"]},
        {"Who sang the song 'Love my baby'? ": ["Adele Kinobi", "Nick June", "Haley Smith", "Nikita"]},
        {"Who sang the song 'How are you'? ": ["Adele Kinobi", "Nick June", "Haley Smith", "Bob Sheeran"]}
        ]


      }

while (exit != "1"):
    level = 0
    genre = input(" Which quiz do you want to take? ")
    print(quiz.get("Music"))
    
    exit = input("Press 1 to exit or any other key to continue?  ")
