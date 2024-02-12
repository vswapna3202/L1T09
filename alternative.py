# This program reads in a string and makes each alternate character an upper case character and 
# each alternate character a lower case character. Also with same string makes alternate word lower case
# and upper case

# Converting alternate characters in a sentence to uppercase and lowercase
orig_sentence = "Hello World" #Assign orig_sentence variable with string "Hello World"

converted_sentence = "" #Assign converted_sentence variable to empty String

for i in range(len(orig_sentence)): #Loop using for with index i and in range of length of orig_sentence
 
    if (i%2 == 0): # Check if index is even
        converted_sentence += orig_sentence[i].upper() #convert char at i using upper function
    else:
        converted_sentence += orig_sentence[i].lower() #convert char at i using lower function

print(f"Converted Sentence is: {converted_sentence}") #Print the converted string to console

# Converting alternate words in a sentence to upper and lowercase
orig_sentence = "I am learning to code" #Assign the sentence to orig_sentence variable


converted_sentence="" # Assign empty string to converted_sentence variable

orig_words = orig_sentence.split() # Split orig_sentence and store it in orig_words

converted_words = [] # Assign converted_words variable as empty list

for i in range(len(orig_words)): # Use for loop to loop through all orig_words list 
    if (i%2 != 0): # Check if index i is not even
        converted_words.append(orig_words[i].upper()) #Append upper of orig_words to converted_words
    else:

        converted_words.append(orig_words[i].lower()) #Append lower of orig_words to converted_words

converted_sentence = " ".join(converted_words) # join converted_words list to converted_sentence

print(f"Converted Sentence with alternate words is: {converted_sentence}") #print the converted sentence 
