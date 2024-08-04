drinks = {"CLCoffee latte": {'[1] s':110, '[2] m':125 ,'[3] l':140},
        "CPCappucino": {'[1] s' :110, '[2] m':125 ,'[3] l':140},
        "CMCaffe Mocha": {'[1] s':125, '[2] m':140 ,'[3] l':155},
        "CAMACCaramel Macchiato": {'[1] s':135, '[2] m':150 ,'[3] l':165},
        "WCMWhite Chococolate Mocha": {'[1] s':135, '[2] m':150 ,'[3] l':160},
        "CACaffe Americano": {'[1] s':100, '[2] m':115 ,'[3] l':130}}
quit = 'n'
coffee_program = ""
def coffee():
    try:
        coffee_program = ""
        while coffee_program != 'n':
            display_menu()
            coffee_program = input("[CL]Coffee latte  [CP]Cappucino  [CM]Caffe Mocha [CAMAC]Caramel Macchiato  [WCM]White Chococolate Mocha  [CA]Caffe Americano : ").lower().strip()
            if coffee_program != quit:
                if coffee_program =='cl':
                    print(sorted(drinks["CLCoffee latte"].keys()))
                    Choose_size = input("Select your size : ")
                    for i in Choose_size:
                        if i == "1":
                            print("Your coffee price is {} Baht".format(drinks["CLCoffee latte"]['[1] s']))
                        if i == "2":
                            print("Your coffee price is {} Baht".format(drinks["CLCoffee latte"]['[2] m']))
                        if i == "3":
                            print("Your coffee price is {} Baht".format(drinks["CLCoffee latte"]['[3] l']))
            if coffee_program =='cp':
                    print(sorted(drinks["CPCappucino"].keys()))
                    Choose_size = input("Select your size : ")
                    for i in Choose_size:
                        if i == "1":
                            print("Your coffee price is {} Baht".format(drinks["CPCappucino"]['[1] s']))
                        if i == "2":
                            print("Your coffee price is {} Baht".format(drinks["CPCappucino"]['[2] m']))
                        if i == "3":
                            print("Your coffee price is {} Baht".format(drinks["CPCappucino"]['[3] l']))
            if coffee_program =='cm':
                    print(sorted(drinks["CMCaffe Mocha"].keys()))
                    Choose_size = input("Select your size : ")
                    for i in Choose_size:
                        if i == "1":
                            print("Your coffee price is {} Baht".format(drinks["CMCaffe Mocha"]['[1] s']))
                        if i == "2":
                            print("Your coffee price is {} Baht".format(drinks["CMCaffe Mocha"]['[2] m']))
                        if i == "3":
                            print("Your coffee price is {} Baht".format(drinks["CMCaffe Mocha"]['[3] l']))
            if coffee_program =='camac':
                    print(sorted(drinks["CAMACCaramel Macchiato"].keys()))
                    Choose_size = input("Select your size : ")
                    for i in Choose_size:
                        if i == "1":
                            print("Your coffee price is {} Baht".format(drinks["CAMACCaramel Macchiato"]['[1] s']))
                        if i == "2":
                            print("Your coffee price is {} Baht".format(drinks["CAMACCaramel Macchiato"]['[2] m']))
                        if i == "3":
                            print("Your coffee price is {} Baht".format(drinks["CAMACCaramel Macchiato"]['[3] l']))    
            if coffee_program =='wcm':
                    print(sorted(drinks["WCMWhite Chococolate Mocha"].keys()))
                    Choose_size = input("Select your size : ")
                    for i in Choose_size:
                        if i == "1":
                            print("Your coffee price is {} Baht".format(drinks["WCMWhite Chococolate Mocha"]['[1] s']))
                        if i == "2":
                            print("Your coffee price is {} Baht".format(drinks["WCMWhite Chococolate Mocha"]['[2] m']))
                        if i == "3":
                            print("Your coffee price is {} Baht".format(drinks["WCMWhite Chococolate Mocha"]['[3] l'])) 
            if coffee_program =='ca':
                    print(sorted(drinks["CACaffe Americano"].keys()))
                    Choose_size = input("Select your size : ")
                    for i in Choose_size:
                        if i == "1":
                            print("Your coffee price is {} Baht".format(drinks["CACaffe Americano"]['[1] s']))
                        if i == "2":
                            print("Your coffee price is {} Baht".format(drinks["CACaffe Americano"]['[2] m']))
                        if i == "3":
                            print("Your coffee price is {} Baht".format(drinks["CACaffe Americano"]['[3] l'])) 
            coffee_program = input('Do you want to ordering again? enter n for quit :')
    except ValueError as err :
        print(err)
    except Exception as err : 
        print(err)

def display_menu():
    inflie = open('Menu.txt','r')
    s = inflie.read()
    print(s)
    inflie.close()

coffee()
