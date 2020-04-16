import random

def primary():
  # print("Keep it logically awesome.")

  #This will assign the variable "f" to open the specified file.
  #Then the program will read the entire txt file and store in
  #into the variable "quotes".
  #IT IS IMPORTANT TO CLOSE THE FILE EACH TIME.
  
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last =13
  rnd = random.randint(0, last)
  print(quotes[rnd])
  print(quotes[rnd])

if __name__== "__main__":
  primary()
