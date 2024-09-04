print("Enter your top 5 favourite movies of all time")
print("Friend 1")
#get their favouite movies from friend 1
movies=[]
for i in range(5):
    friend_1 = input(f"Enter your {i+1} favourite movie: ").capitalize()
    movies.append(friend_1)
#using while loop for "Continue until they is atleast 3 movies they both like"

while True:
    count=0
    print("Friend 2")
    #get their favouite movies from friend 1
    for i in range(5):
        friend_2 = input(f"Enter your {i+1} favourite movie: ").capitalize()
        #check If the friend 2's fav movie is in the first friend's list
        if friend_2 in movies:
            print(f"You both like {friend_2}")
            count+=1
            if count == 3:
                quit()
    print("TRY AGAIN")


