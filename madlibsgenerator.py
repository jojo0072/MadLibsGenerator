# 3 versions camping, hospital, forest
import random
def main():
    print("Madlibs\n")
    madlibs=[madlibs_camping, madlibs_hospital, madlibs_forest]
    choice=random.choice(madlibs)
    print(choice())
def madlibs_camping():
    words_template=["Enter a person's name: ", "Enter a noun: ", "Enter a feeling: ", "Enter a verb: ", "Enter a feeling: ", "Enter an animal: ", "Enter a verb: ", "Enter a color: ", "Enter a verb(ending with -ing): ", "Enter an adverb (ending with ly): ", "Enter a number: ", "Enter a measure of time: ", "Enter a color: ", "Enter an animal: ", "Enter a number: ", "Enter a silly word: ", "Enter a noun: "]
    words=[]
    for x in words_template:
            y=input(x)
            words.append(y)                        
    persons_name, noun_1, feeling_1, verb_1, feeling_2, animal_1, verb_2, color_1, verb_ing, adverb_ly, number_1, measure_of_time, color_2, animal_2, number_2, silly_word, noun_2=words
    story=f"""\nStory: \nThis weekend I am going camping with {persons_name}.\nI packed my lantern, sleeping bag, and {noun_1}.\nI am so {feeling_1} to {verb_1} in a tent.\nI am {feeling_2} we might see a {animal_1}, they are kind of dangerous.\nWe are going to hike, fish, and {verb_2}.\nI have heard that the {color_1} lake is great for {verb_ing}.\n Then we will {adverb_ly} hike through the forest for {number_1} {measure_of_time}.\nIf I see a {color_2} {animal_2} while hiking, I am going to bring it home as a pet!\n At night we will tell {number_2} {silly_word} stories and roast {noun_2} around the campfire!! """
    return story
                
def madlibs_hospital():
    words_template=["Enter a number: ", "Enter a measure of time: ", "Enter a mode of transportation: ", "Enter an adjective: ", "Enter an adjective: ", "Enter a noun: ", "Enter a color: ", "Enter a part of the body: ", "Enter a verb: ", "Enter a number: ", "Enter a noun: ", "Enter a noun: ", "Enter a part of the body: ", "Enter a verb: ", "Enter a noun: ", "Enter an adjective: ", "Enter a silly word: ", "Enter a noun: "]
    words=[]
    for x in words_template:
            y=input(x)
            words.append(y)                        
    number_1, measure_of_time, mode_of_transportation, adjective_1, adjective_2, noun_1, color, part_of_the_body_1, verb_1, number_2, noun_2, noun_3, part_of_the_body_2, verb_2, noun_4, adjective_3, silly_word, noun_5=words
    story=f"""\nStory: \nIt was about {number_1} {measure_of_time} ago when I came to the hospital in a {mode_of_transportation}.\nThe hospital is a/an {adjective_1} place, there are a lot of {adjective_2} {noun_1} here.\nThere are nurses here who have {color} {part_of_the_body_1}.\nIf someone wants to come into my room,  I told them that they have to {verb_1} first.\nI have decorated my room with {number_2} {noun_2}.\nToday a doctor came into my room and they were wearing a {noun_3} on their {part_of_the_body_2}.\nI heard that all doctors {verb_2} {noun_4} every day for breakfast.\nThe most {adjective_3} thing about being in the hospital is the {silly_word} {noun_5}!"""
    return story
             
def madlibs_forest():
  words_template=["Enter a person's name: ", "Enter an adjective: ", "Enter a color: ", "Enter an animal: ", "Enter a place: ", "Enter an adjective: ", "Enter magical creatures you know: ", "Enter an adjective: ", "Enter magical creatures you know: ", "Enter a room in a house: ", "Enter a noun: ", "Enter a noun: ", "Enter a noun: ", "Enter an adjective: ", "Enter a noun: ", "Enter an number: ", "Enter a measure of time: ", "Enter a verb (ending with -ing): ", "Enter an adjective: ", "Enter a noun: "]
  words=[]
  for x in words_template:
            y=input(x)
            words.append(y)                        
  persons_name, adjective_1, color, animal, place, adjective_2, magical_creatures_1, adjective_3, magical_creatures_2, room_in_a_house, noun_1, noun_2, noun_3, adjective_4, noun_4, number, measure_of_time, verb_ing, adjective_5, noun_5=words
  story="""\nStory: \nDear {persons_name},\nI am writing to you from a {adjective_1} castle in an enchanted forest.\nI found myself here one day after going for a ride on a {color} {animal} in {place}.\nThere are {adjective_2} {magical_creatures_1} and {adjective_3} {magical_creatures_2} here!\nIn the {room_in_a_house}, there is a pool full of {noun_1}.\nI fall asleep each night on a {noun_2} of {noun_3} and dream of {adjective_4} {noun_4}.\nIt feels as though I have lived here for {number} {measure_of_time}.\nI hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective_5} {noun_5}!!"""
  return story  
  
main()