

from tokenize import String


def Add (numbers:String):

    #customize delimter
    delimiter = ","
    if "//" in numbers:
        start_idx = numbers.find("//") + len("//")
        end_idx = numbers.find("\n")
        delimiter = numbers[start_idx:end_idx]


    hall_of_shames = ""
    list_char = numbers.split(delimiter)    
    sum = 0
    for item in list_char:
        
        #handle new lines
        if "\n" in item:
            item = item.strip("\n")
            item = item.strip()

        
        #check for integers
        try:
            item = int(item)
            if item > 1000:
                continue
        except ValueError:
            continue
    
        sum = sum + item
            
        #handle negative
        if item < 0:    
            hall_of_shames = hall_of_shames + str(item) +", "
            continue

        
    if len(hall_of_shames) > 0:
        raise Exception("Negatives not allowed" + ": " + hall_of_shames[0:len(hall_of_shames)-2])

    return sum

#test
if __name__ == "__main__":
    

    list_input_and_expect = [ ["1,2,5", 8 ], ["", 0], ["1\n,2,3", 6],  ["1,\n2,4",7 ], ["1   \n,2,3", 6],
                              ["//$\n1$2$3",6], ["//@\n2@3@8",13], ["//@\n-2@-3@8", "an exception"], 
                              ["//@\n-2@-3@8@-123@-22@8@-30", "an exception"],
                              ["//***\n1***2***3",6] ]
                              

    failed_cases = 0
    for item in list_input_and_expect:
        
        try:
            result = Add(item[0])

            if result != item[1]:
                print("Expected " + str(item[1]) + " but recieved " + str(result))
                failed_cases += 1
            
        except Exception as error:
            print("Expected " + item[1] + " and exception was thrown with message: ")
            print(error)
            print("\n")


    if not (failed_cases):
        print("ALL G BRODA")
