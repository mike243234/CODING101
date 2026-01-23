Cabin = input("What is your cabin type: ")
def cabin_deluxe(Cabin):
  if Cabin == "Lux":
    print("upper-deck cabin with a balcony.")
  elif Cabin == "A":
    print("above the car deck, equipped with a window.")
  elif Cabin =="B":
    print("windowless cabin above the car deck.")
  elif Cabin =="C":
    print("windowless cabin below the car deck.")
  else:
    print("Invalid Cabin class")
  return Cabin
new_cabin = cabin_deluxe(Cabin)
