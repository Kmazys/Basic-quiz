




playing = input("You stand upon the sanctuary of the fallen. To enter you must answer 3 questions if you fail , you die! Do you wish to continue? ")

if playing.lower() != "yes":
    quit()

print("As you wish... ")
Score = 0
answer = input("It cannot be seen, it cannot be felt, cannot be heard, cannot be smelt. It lies behind stars and under the hills and empty holes it fills."
               " Comes first follows after, ends life, kills laughter? What is it? ")

if answer.lower() == "darkness":
    print("You are correct")

else:
    print("WRONG! Die!")
    quit()


answer = input("It's right behind you and creeps on the ground, it follows you home, does not make a sound. What is it? ")

if answer.lower() == "shadow":
    print("You are correct")
else:
    print("WRONG! Die!")
    quit()


answer = input("They have no flesh, nor feathers, nor scales, nor bone. Yet they have fingers and thumbs of their own. What are they? ")

if answer.lower() == "gloves":
    print("You are correct, you may enter...")
else:
    print("WRONG! DIE!")
    quit()