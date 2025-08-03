# Hello, and welcome to the Phrase Randomiser.
# This simple script exists to take a whole load of phrases and memes and randomly choose them.
# This is basically me playing around with lists and the random library to see what I can do while learning Python.
# This collection of memes, phrases, and slogans can (and likely will) be very handy for some, so please feel free to copy this code or add to it :3
# One thing you can use this for is to pipe it into cowsay (or simular) with "<path to this script>/phraserandomiser.py | cowsay"
# Anyway, have fun, contribute more at https://github.com/abbiistabbii/pythonscripts/blob/main/phraserandomiser.py!

import random

phraselist = ["Master Skywalker, did you know that in terms of human pokemon breeding...",
"NOTHING BEATS A JET2 HOLIDAY!",
"You truly are the King of Kings.",
"Well there's no cock like Horse Cock!",
"Emacs cured my Autism!",
"Nice Cock!",
"Cunty Buttlicks!",
"Arsebiscuits!",
"hewo...mimster obabnab?",
"DO I LOOK LIKE SOMEONE WHO CARES WHAT GOD THINKS?",
"YOUR NAME SHALL ALSO GO ON ZE LIST, WHAT IS IT?",
"I BLAME SOCIETY!",
"owo what's this?",
"God has let me live another day and I am going to make that everyone else's problem",
"Thanks! I hate this!",
"FUCK YOU I LOVE THIS!",
"uwu kimochiiiiii~",
"We have to steal the Declaration of Independence",
"What hath God wrought?",
"Epstein didn't kill himself",
"No Gods, No Masters",
"No Balls, No Masters!",
"Gun Diathan, Gun Tigheran!",
"As fearr Gaidhlig briste na Gaidhlig anns a chiste!",
"I've...seen things you people wouldn't believe",
"Fuck the OSA!",
"Something something Daaaaaaaaaark Siiiiiiiiiiide something",
"In the poop? In the poop.",
"FUCK ME YOURSELF YOU FUCKING COWARD",
"Except the Shrimp",
"Remember kids, Woke is literally just a relabeling of the word 'Degenerate' as the Nazis used it in the 1930s!",
"BANG! AND THE DIRT IS GONE!",
"Never gonna give you up, never gonna let you down...",
"Come to the Brian the Manwhore Memorial!",
"WELCOME TO THE PISS ZONE!",
"The law is on the books, but it would take all their resources to enforce it!",
"Free Palestine, Free Tibet.",
"Fuck Vladimir Putin!",
"Fuck Donald Trump!",
"Trans rights!",
"Trans Rights are Human Rights",
"Fuck TERFS and SWERFS",
"God may love you but Satan does that thing with his tongue owo",
"Everyday I'm suffering! AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
"Hail Linus!",
"Gonnae no dae that",
"Milk Lemonaid Chocolate!",
"You have been doing this for a while, aye?",
"From the moment I understood the weakness of my flesh, it disgusted me. I craved the strength and certainty of steel.",
"owo",
"uwu",
"BLOOD FOR THE BLOOD GOD!",
"SKULLS FOR THE SKULL THRONE!",
"MILK FOR THE CORNFLAKES!",
"PISS FOR THE PISS JUG!",
"Glory, Glory tae the Hibees! Glory, Glory tae the Hibees! Glory Glory tae the Hibees, they are the Hibee bois!",
"Be Gay, Do Crime!",
"Bi gèidh, dean eucoirean!",
"Fuck Keir Starmer the Queer Harmer",
"Fuck Anti Queer Keir",
"MILF: Man I love Frogs",
"WHY ARE YOU GETTING CLOTHES FROM THE SOUP STORE?!",
"Do you know what C Equals?",
"Aurora Borealis? At this time of year! At this time of day! In this part of the country! Localized entirely within your kitchen?!?",
"According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.",
"I am going to punch your face...in the face",
"I like trains.",
]

endnumber = len(phraselist)
randomnumber = random.randint(0, endnumber-1)

print(phraselist[randomnumber])



