message = "Hello World, I'm practice Python language"

# dir(<element>) helper. This function shows us all the methods available to work with the data type of the associated argument.
# print(dir(message))

print(message.upper())
print(message.lower())

# String concat
tlor_fav_movie = "The return of the king"

print("My TLOR favorite movie is: " + tlor_fav_movie)
print(f"My TLOR favorite movie is: {tlor_fav_movie}")
print("My TLOR favorite movie is: {0}".format(tlor_fav_movie))