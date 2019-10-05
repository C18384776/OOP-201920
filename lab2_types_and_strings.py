#course: Object-oriented programming, year 2, semester 1
#academic year: 201920
#author: B. Schoen-Phelan
#date: 29-09-2019
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    #def play_with_strings(self):
        # working with strings
        # message = input("Enter your noun: ")
        # print("Originally entered: "+ message)

        # print only first and last of the sentence
        # print("First letter :" + message[0] + " Last letter :" + message[-1])

        # use slice notation
        # print(message[:4])

        # escaping a character
        # print("He said \"that\'s fantastic\"")

        # find all a's in the input word and count how many there are
        #     message = "Mary had a little lamb"
        #     print(message.find('a'))
        #     print(message.count('l'))

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace()
        #     message = "Mary had a little lamb"
        #     print(message.replace('a', '-'))

        # printing only characters at even index positions
        #     message = input("Enter your noun: ")
        #     for i in range(1, 6, 2):
        #         print(message[i])

    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        # print("Originally entered: "+ message)

        # hand the input string to a list and print it out
        # message = message.split(' ')
        #
        # print(message)

        # append a new element to the list and print
        # message.append(' aWord')
        # print(message)

        # remove from the list in 3 ways
        # message.pop(1) #Removes second word, just pop() will remove last item
        # print(message)

        # check if the word cake is in your input list
        # if 'cake' in message:
        #     print("cake is in message")

        # reverse the items in the list and print
        # for i in reversed(message):
        #     print(i)

        # reverse the list with the slicing trick
        # message = message[::-1]
        # print(message)

        # print the list 3 times by using multiplication
        # print(message*3)



tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()