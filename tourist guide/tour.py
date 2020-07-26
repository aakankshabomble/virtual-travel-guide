import webbrowser

from urllib3.util import url

cities = ["mumbai", "Ahmedabad"]

my_dict = {"mumbai": ["Holy place", "outdoor", "malls", "Nightlife", "Instagram spots", "Markets"],
           "Ahmedabad": ["Holy places", "outdoors", "mall", "Night_life", "Instagram_spots", "Market"]}

place = ["Holy places", "outdoors", "mall", "Night_life", "Instagram_spots", "Market"]
area = ["Holy place", "outdoor", "malls", "Nightlife", "Instagram spots", "Markets"]

mumbai = {"Holy places": ["Mumbadevi temple", "Sidhivinayak temple", "Hajiaali darga", "Mount marry church"],
          "outdoors": ["Gateway of india", "Kanheri caves", "Sanjay Gandhi National Park",
                       "Hanging garden", "Nehru planeprium"],
          "mall": ["Phoenix Marketcity, Kurla", "Infinity Mall, Malad", "R City Mall, Ghatkopar",
                   "Inorbit Mall, Malad", "Palladium, Lower Parel", "Growel's 101, Kandivali "],
          "Night_life": ["Trilogy, Juhu", "Tryst Nightclub, Lower Parel", "21 Fahrenheit Ice Lounge, Andheri",
                         "PDT, Lower Parel", "Tap Resto Bar, Andheri", "AER, worli"],
          "Instagram_spots": ["Street of Kala Ghoda", "Candies, Bandra", "Horniman Circle", "AER, worli",
                              "Tamasha, Lower Parel", "Gateway of India", "Asiatic Library",
                              "Prince of Wales Museum", "GrandMamas Cafe"],
          "Market": ["Colaba Causeway", "Chor Bazaar", "Crawford Market", "Zaveri Market",
                     "Kala ghoda Art Pada Pavement Gallery", "Linking Road Market"]
          }

Ahmedabad = {"Holy place": ["Swaminarayan Temple", "Dada Hari Wav", "Huthresing Jain Temple", "Sidi Saiyyed Mosque",
                            "Vaishno Devi temple"],
             "outdoor": ["Sabarmati Adhr(Residence of Mahatma Gandhi)", "Kankaria Lake", "Jhulta Minar",
                         "Kamla Nehru Zoo", "Adalaj Stepwell "],
             "malls": ["Alpha One Mall", "Ahmadabad One", "Himalayan Mall, Acropolis Mall"],
             "Nightlife": ["Tryst the lounge", "Cyclone Discotheques", "Kavach",
                           "Escape Discotheque", "Nirvana Lounge", "The Lotus Poo"],
             "Instagram spots": ["Amdavad ni Gufa", "Sarkheji Roza", "Dada Hari Stepwell", "Sidi Saiyyed Mosque",
                                 "Parimal Garden", ],
             "Markets": ["Law Garden Night Markets ", "Lal Darwaja", "Banascraft", "Dhalgarwad",
                         "Rani no Hajiro", ]
             }

mode = ["Bus", "Train", "Aeroplane", "Private vehicle"]
dict_mode = {"Bus": ["bus"], "Train": ["train"], "Aeroplane": ["aeroplane"], "Private vehicle": ["private vehicle"]}

print("***********************")
print("*WELCOME TO TRIP PLANNER*")
print("***********************\n")

name = input("Hello there ! \nWhat's your good name ? ")
print("\n Hello " + name + " nice to meet you !")
print("We are available in these amazing cities right now")
i = 1
for c in my_dict.keys():
    print(str(i) + "." + str(c))
    i += 1
print()

city = int(input("which city you are intrested in visiting...?? "))
my_city = cities[city - 1]
print()
print("that's an amazing choice so you want to visit " + my_city + "\n\n ")
i = 1
for m in dict_mode.keys():
    print(str(i) + "." + str(m))
    i += 1
print()
mot = int(input("how would you like to travel..?"))
my_mode = mode[mot - 1]
print()
i = 1
print("you have opted for " + my_mode)
print("ohhkk...that's cool\n\n\n")

"""print("\nNow lets go ahead and book the tickets ")
flightbooked = False
def book_flight():
    print("\nWhich of the following sites do you prefer?")
    site = int(input("1.Clear Trip\n2.Goibibo\n3.Yatra.com\nChoice: "))
    if site == 1:
        url = "https://www.cleartrip.com/flights/international/results?from=BOM&to=" + my_city + "&depart_date=29/12/2018&adults=1&childs=0&infants=0&class=Economy&airline=&carrier=&intl=y&sd=1524084890374&page=loaded"
    elif site == 2:
        url = "https://www.goibibo.com/flights/air-BOM-" + my_city + "-20180513-20180517-1-0-0-E-I/"
    elif site == 3:
        url = "https://www.yatra.com/international-flights/mumbai-to-" + my_city + "-flights"


info2 = input("Proceed to webiste?(Y/N) ")
if info2 == 'y' or info2 == 'Y':
    webbrowser.open_new_tab(url)
    book = input("\nDid you find your desired seat? (Y/N): ")
    if book == 'n' or book == 'N':
        book_flight()
    else:
        flight_booked = True
        print("\nOkay that's great!")
else:
    print("\nOkay we'll do that later!")

book_flight()

if (flightbooked==False):
    choice=input("\nWould you like to book the Flight tickets now? (Y/N): ")
    if(choice=='Y' or choice=='y'):
        print("\nOkay let's go!")
        book_flight()
print()
print("We genuinely hope you have an amazing trip and return home with plenty of unforgettable moments! Hope you'll think of us next time when you wish to travel once again. See you later, "+name+"!")"""

print(my_city + " has following choices to visit")
i = 1
for v in my_dict[my_city]:
    print(str(i) + "." + str(v))
    i += 1
print()

if city == 1:
    choice = int(input("Which places you are intrested in..?"))
    my_mumbai = place[choice - 1]
    print()
    print("that's interesting :) " + my_mumbai)
    i = 1
    for p in mumbai[my_mumbai]:
        print(str(i) + "." + str(p))
        i += 1
    print()

else:
    userc = int(input("Which places you are intrested in..?"))
    my_ahmedabad = area[userc - 1]
    print()
    print("that's interesting :) " + my_ahmedabad)
    i = 1
    for s in Ahmedabad[my_ahmedabad]:
        print(str(i) + "." + str(s))
        i += 1
    print()

"""info = input("should we plan your trip to " + my_city + "..?(Y/N)")
if info == 'y' or info == 'Y':
    nope = int(input("\nSo," + name + ". You must be bringing along a few people atleast,right..? To help us plan your trip better, please tell us how many peoples are comimg with you..?"))
    if nope == 0:
        print("\nohhh! So its more like a solo trip")
elif info == 'n' or info == 'N':
    print("\nohh! So its the " + str(nope + 1) + " members going together ! All of you will have great time. ")
    days = input("\nSo for how many days you want we come " + my_city + " ?")
    if days == 1:
        print("You can enjoy day time at holy places and night time at clubs or else you can dicide wherever you want to visit")
    elif days == 2:
        print("You can enjoy your day one outdoors and day two exploring markets and clubing at night ")
    elif days == 3:
        print(" Enjoy your day one at holy sites, day two at markets and instagram spots and day three shopping in markets and malls.")
else:
    print("it seems that you have already planed a trip")"""
