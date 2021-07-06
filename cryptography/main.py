from art import art

print(art)

# Alphabets to increment or decrement
alphabets = "abcdefghijklmnopqrstuvwxyz"

# Checks if user input is to encode or decode 
prompt_user = input("Type 'encode' to encrypt or type 'decode' to decrypt: \n")

# A function for the word program
def cryptography(prompt_user) :
    encrypted_message = ""
    
    # Prompts user to go again if they enter the wrong input i.e text other than encode or decode 
    while prompt_user != "encode" and prompt_user != "decode" :
        prompt_user = input("Wrong input. \nPlease type 'encode' to encrypt or type 'decode' to decrypt: \n")
        prompt_user = prompt_user

    if prompt_user == "encode" :
        
        # collects input
        user_message = input("Type your message: ")
        message_key = input("Type encryption key: ")            

        # initialise encrypted message
        encrypted_message = ""

        # key validation
        # check for space and enter
        if message_key == "" or message_key.isspace() :
            message_key = "0"

        # check for other conditions
        else:
            while not message_key.isnumeric() or not int(message_key) in range(1, 11):
                message_key = input("Please enter a key between 1 to 10: ")
                message_key = message_key

        final_message_key = int(message_key)   


        #encryption processing 
        for char in user_message :
            # check uppercase
            if char == char.upper() :
                encrypted_message += char   
            else:
                new_index = (alphabets.index(char) + final_message_key) % 26
                encrypted_message += alphabets[new_index]

        print(f"Here is your encoded result: {encrypted_message}")


    
    elif prompt_user == "decode" :
        
        # collects input
        user_message = input("Type your message: ")
        message_key = input("Type decryption key: ")           
        
        # initialise decrypted message
        decrypted_message = ""

        # key validation
        # check for space and enter
        if message_key == "" or message_key.isspace() :
            message_key = "0"

        # check for other conditions
        else:
            while not message_key.isnumeric() or not int(message_key) in range(1, 11):
                message_key = input("Please enter a key between 1 to 10: ")
                message_key = message_key

        final_message_key = int(message_key)   


        #decryption processing 
        for char in user_message :
            
            # check uppercase
            if char == char.upper() :
                decrypted_message += char   
            else:
                new_index = (alphabets.index(char) - final_message_key) % 26
                decrypted_message += alphabets[new_index]

        print(f"Here is your decoded result: {decrypted_message}")

cryptography(prompt_user)   


# Prompts the user to try again

user_try_again = input("Type 'yes' if you want to go again, otherwise type 'no' \n")

if user_try_again == "no":
    
    print("Thank you for using our Cryptography service ")

else:
    while user_try_again == "yes" :   
       
        prompt_user = input("Type 'encode' to encrypt or type 'decode' to decrypt: \n")
        
        # recalling the function if the user wants to go again
        cryptography(prompt_user)
        
        user_try_again = input("Type 'yes' if you want to go again, otherwise type 'no' \n")
    
    print("Thank you for using our Cryptography service ")


