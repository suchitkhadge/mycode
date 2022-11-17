


marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

while (exit != "1"):
    char_name = input(" Which character do you want to know about? (Starlord, Mystique, Hulk:\n").lower().title()
    char_stat = input (" What statistic do you want to know about? (real name, powers, archenemy:\n").lower() 
    
    if (char_stat == "real name"):
        print(char_name,"'s ", char_stat, " is: ", marvelchars.get(char_name).get(char_stat).title())
    else:
        print(char_name,"'s ", char_stat, " is: ", marvelchars.get(char_name).get(char_stat))
    exit = input("Press 1 to exit or any other key to continue?  ")    
        
