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
    elif choice == "Clothing":
       msg = "which product do you want?"
       title = "product is"
       choices = ["Levis", "Wrangler", "UCB", "peter england"]
       choice = choicebox(msg, title, choices)
    elif choice == "Footwear":
       msg = "which product do you want?"
       title = "product is"
       choices = ["Nike", "Puma", "Reebok", "Adidas"]
       choice = choicebox(msg, title, choices)
    if choice == "Puma":
      msg = "Which dealer do you want  to choose?"
      title = " price is"
      choices = ["vineet:-$50", "nishant:-$40", "arnav:-$57"]
      choice = choicebox(msg, title, choices)
    elif choice == "Mobiles":
       msg = "which product do you want?"
       title = "product is"
       choices = ["Apple", "MI", "Oppo", "Vivo", "One Plus"]
       choice = choicebox(msg, title, choices)
    else :
       msg = "which product do you want?"
       title = "product is"
       choices = ["Backpacks", "Suit cases", "Gym tools", "Bat", "Foot ball"]
       choice = choicebox(msg, title, choices)
    msgbox("you choose: " + str(choice), "you shopped")

    msg = "Do you want to continue?"
    title = "please confirm"

    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)

