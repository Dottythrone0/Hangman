import csv
import random

def read_data_from_file():
    countries = [""]*196
    filename = "countries.txt"
    file = open(filename, "r")
    reader = csv.reader(file)
    counter = 0
    for row in reader:
        countries[counter] = str(row[0])
        counter = counter + 1
    file.close()
    return countries

def pick_random_country(countries):
    Country = random.choice(countries) #picks a random country from countries array
    country = Country.lower()#converts all characters in country name to lowercase

    return country, Country


def get_user_input(country):
    guess = 0
    counter = -1
    character = [""]*len(country)*2
    index = 0
    word = ""
    output = ["_"]*len(country)

    while guess < len(country)*2 and "".join(map(str, output)) != country:
          total = 0
          counter = counter + 1
          character[counter] = input('Please enter a letter you would like to guess ')
          guess = guess + 1
          while len(character[counter]) != 1 or ord(character[counter]) > 122 or ord(character[counter]) < 97 and ord(character[counter]) > 32:
                character[counter] = input('Please enter a single letter, not a word, a number or a capital letter ')       
          for index in range(len(country)):
               if character[counter] == country[index]:
                  output[index] = character[counter]
                  word = " ".join(map(str, output)) #converts output array into string, leaving a space between characters
               else:
                   total = total + 1 #adds one to total each time each character of the country doesen't equal the character entered by the user 
                  
          if total == len(country): #if the character entered by the user isn't in country name
              print("character not found in country name")
              print("You have",len(country)*2 - guess, "guesses left")
          else:
              print(word)
              print("You have",len(country)*2 - guess, "guesses left")
                  

                
               
    return word, guess, output

def display_results(country, guess, output, Country):
    output_string = ""
    output_string = "".join(map(str, output)) #converts output array into a string WITHOUT spaces, so it can be compared to country name
    if output_string == country:
        print("well done you guessed the right country as", Country)
    else:
        print("you lose. The country was", Country)
    
                   




#main program

#call statement to read data from the file into "countries" array
countries = read_data_from_file()
#call statement to pick random country
country, Country = pick_random_country(countries)
#call statement to ask the user to guess their characters and to return their guess after a certain number of entries
word, guess, output = get_user_input(country)
#call statement to display message to the user, detailing them of the result of the game
display_results(country, guess, output, Country)


