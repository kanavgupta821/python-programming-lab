#Name-Kanav Gupta
#Division-M
#Roll no.-25
from easygui import *
import sys
while 1:
    msgbox("online shopping")

    msg ="Which online shopping site do you want to choose?"
    title = "shopping sites are"
    choices = ["Amazon", "Flipcart", "Snapdeal", "Myntra", "Jabong"]
    choice = choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    if choice == "Amazon":
     msg = "which category do you want to choose? "
     title = "categories are"
     choices = ["Electronics", "Clothing", "Footwear", "Mobiles", "Sports and luggage"]
     choice = choicebox(msg, title, choices)


    elif choice == "Flipcart":
     msg = "which category do you want to choose? "
     title = "categories are"
     choices = ["Electronics", "Clothing", "Footwear", "Mobiles", "Sports and luggage"]
     choice = choicebox(msg, title, choices)


    elif choice == "Snapdeal":
     msg = "which category do you want to choose? "
     title = "categories are"
     choices = ["Electronics", "Clothing", "Footwear", "Mobiles", "Sports and luggage"]
     choice = choicebox(msg, title, choices)


    elif choice == "Myntra":
     msg = "which category do you want to choose? "
     title = "categories are"
     choices = ["Electronics", "Clothing", "Footwear", "Mobiles", "Sports and luggage"]
     choice = choicebox(msg, title, choices)


    else:
     msg = "which category do you want to choose? "
     title = "categories are"
     choices = ["Electronics", "Clothing", "Footwear", "Mobiles", "Sports and luggage"]
     choice = choicebox(msg, title, choices)


    if choice == "Electronics":
       msg = "which product do you want?"
       title = "product is"
       choices = ["TV", "Laptops", "Computers", "accessories"]
       choice = choicebox(msg, title, choices)
    if choice == "TV":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Kanav:-Rs 34900", "Akshit:-Rs43200", "Arnav:-Rs 53400"]
      choice = choicebox(msg, title, choices)
    elif choice == "Laptops":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Kanav:-Rs 50000", "Akshit:-Rs59000", "Arnav:-Rs 61000"]
      choice = choicebox(msg, title, choices)
    elif choice == "Computers":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Kanav:-Rs 30000", "Akshit:-Rs39000", "Arnav:-Rs 40000"]
      choice = choicebox(msg, title, choices)
    elif choice == "accessories":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Kanav:-Rs 500", "Akshit:-Rs600", "Arnav:-Rs 700"]
      choice = choicebox(msg, title, choices)

    elif choice == "Clothing":
       msg = "which product do you want?"
       title = "product is"
       choices = ["Levis", "Wrangler", "UCB", "peter england"]
       choice = choicebox(msg, title, choices)
    if choice == "Levis":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Akash:-Rs 1500", "Ratan:-Rs 1400", "Ram:-Rs 1800"]
      choice = choicebox(msg, title, choices)
    elif choice == "Wrangler":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Akash:-Rs 1700", "Ratan:-Rs 1200", "Ram:-Rs 1410"]
      choice = choicebox(msg, title, choices)
    elif choice == "UCB":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Akash:-Rs 2200", "Ratan:-Rs 2400", "Ram:-Rs 2700"]
      choice = choicebox(msg, title, choices)
    elif choice == "peter england":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Akash:-Rs 1100", "Ratan:-Rs 1000", "Ram:-Rs 1300"]
      choice = choicebox(msg, title, choices)


    elif choice == "Footwear":
       msg = "which product do you want?"
       title = "product is"
       choices = ["Nike", "Puma", "Reebok", "Adidas"]
       choice = choicebox(msg, title, choices)
    if choice == "Puma":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["vineet:-Rs 5100", "nishant:-Rs 4500", "arnav:-Rs 3600"]
      choice = choicebox(msg, title, choices)
    elif choice == "Nike":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["vineet:-Rs 4900", "nishant:-Rs 3200", "arnav:-Rs 3400"]
      choice = choicebox(msg, title, choices)
    elif choice == "Reebok":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["vineet:-Rs 4500", "nishant:-Rs 6200", "arnav:-Rs 5400"]
      choice = choicebox(msg, title, choices)
    elif choice == "Adidas":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["vineet:-Rs 5900", "nishant:-Rs 4200", "arnav:-Rs 2400"]
      choice = choicebox(msg, title, choices)

    elif choice == "Mobiles":
       msg = "which product do you want?"
       title = "product is"
       choices = ["Apple", "MI", "Oppo", "Vivo", "One Plus"]
       choice = choicebox(msg, title, choices)
    if choice == "Apple":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Karan:-Rs 150000", "Rakshit:-Rs149000", "Nitin:-Rs 91000"]
      choice = choicebox(msg, title, choices)
    elif choice == "MI":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Karan:-Rs 15000", "Rakshit:-Rs14000", "Nitin:-Rs 14100"]
      choice = choicebox(msg, title, choices)
    elif choice == "Oppo":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Karan:-Rs 25000", "Rakshit:-Rs 23000", "Nitin:-Rs 19000"]
      choice = choicebox(msg, title, choices)
    elif choice == "Vivo":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Karan:-Rs 17000", "Rakshit:-Rs16000", "Nitin:-Rs 18000"]
      choice = choicebox(msg, title, choices)
    elif choice == "One Plus":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Karan:-Rs 35000", "Rakshit:-Rs 33000", "Nitin:-Rs 37000"]
      choice = choicebox(msg, title, choices)


    elif choice == "Sports and luggage":
       msg = "which product do you want?"
       title = "product is"
       choices = ["Backpacks", "Suit cases", "Gym tools", "Bat", "Foot ball"]
       choice = choicebox(msg, title, choices)
    if choice == "Backpacks":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Sparsh:-Rs 1200", "Ketan:-Rs 1400", "Sham:-Rs 1000"]
      choice = choicebox(msg, title, choices)
    elif choice == "Suit cases":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Sparsh:-Rs 2800", "Ketan:-Rs 4400", "Sham:-Rs 3700"]
      choice = choicebox(msg, title, choices)
    elif choice == "Gym tools":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Sparsh:-Rs 3400", "Ketan:-Rs 3500", "Sham:-Rs 3200"]
      choice = choicebox(msg, title, choices)
    elif choice == "Bat":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Sparsh:-Rs 1400", "Ketan:-Rs 1900", "Sham:-Rs 1600"]
      choice = choicebox(msg, title, choices)
    elif choice == "Foot ball":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["Sparsh:-Rs 800", "Ketan:-Rs 750", "Sham:-Rs 700"]
      choice = choicebox(msg, title, choices)

    msgbox("you choose: " + str(choice), "you shopped")

    msg = "Do you want to continue?"
    title = "please confirm"

    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)

