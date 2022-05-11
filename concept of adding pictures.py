# This is the cocept of adding pictures to the window.

# By list we can create an array of picture and call it whenever necessary.

# But declaring one by one will be long. so by loop we acn automate the adding

#adding.Add pic is shown in char anime. This is just for creating  the array.


right=[None]*9 # creating None as an element of list and multiplying the element of the list to 9 times so  that it can easily be replaced later on.

for pi in range(1,10):#we have 9 elements in list.
    right[pi-1]=("H"+str(pi))#here at index  0 we are having H1 and at index 9 we r having H10. pi-1 represents the index whrer the H10 to be stored.

print(right)

##We iterate in alist as much we have elements in a list. So giving None will not be benficial since it replace by H1 only.

# So by multiplying list right by 9 we can have 9 from index 0-9
