'''
a CSV (comma separated values) file is a simple file format. The data
contained in the file written in plain text and each dimension of data
is separated by a comma.

Here is an example for a csv containing the planets in our solar system

index, name, size, distance from sun
1, Mercury, 3031.9, 38992000
2, Venus, 7520.8, 67240000
3, Earth, 7917.5, 92960000
4, Mars, 4212.3, 141600000
5, Jupiter, 86881.0, 483800000
6, Saturn, 72367.0, 890800000
7, Uranus, 31518.0, 1784000000
8, Neptune, 30599.0, 2793000000
'''

# Your goal is to fill in this method to parse a CSV file.
def parseCSV(fileName):
    # open file
    file = open(fileName, "r")
    #read file
    contents = file.read()
    #close file
    file.close()

    csvContents = []

    #1. Use the split method using the newling character (\n)
    #   on the file contents to divide each line into a list


    #2. Iterate through each line of the file and use the split
    #   method to divide it by the comma character and append the list
    #   to csvContents


    return csvContents

if __name__ == "__main__":
    #3. Run the program. You should get a success message if everything
    #   is correct. Otherwise you will get an error.
    csv = parseCSV("100-contacts.csv")

    # USED FOR TESTING YOUR CODE
    # DO NOT MODIFY!
    file = open("solution", "r")
    lst2 = file.read()
    file.close()
    assert(str(csv) == lst2)
    print("SUCCESS!!!")