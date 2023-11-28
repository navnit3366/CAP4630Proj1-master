"""
    CAP4630 Intro to A.I. Project 1: Python Basics
    A demonstration of competency with a number of data structures basics and Python 2.7

    1. User is prompted for filename of input data (correct answer: "States.csv". Validation of filename input does not occur, was not required.)
    2. Data read in from States.csv is quantitative and qualitative data on the 50 US states, confirmed to user via console
    3. Menu provided with actions that can be acted on the US states data. Input validation occurs. Available menu choices:
        1) Print to console a full list of all data stored on the US states
        2) Sort the US states data by state name, using QuickSort
        3) Sort the US states data by population, using Radix sort
        4) Find a US state record using a search string
            a. Binary search, if data currently sorted by state name
            b. Sequential search, if data currently NOT sorted by state name
        5) Quit program
    
    Author: Matthew Dowdie
    Version: Jan 20, 2019
    Email: n00721843@ospreys.unf.edu
"""

from State import State
import csv
import sys

print "CAP4640 Project 1\nInstructor: Xudong Liu\nStudent: Matthew Dowdie\n"

#Globals
ListOfStates = []
SortState = "Unsorted" # as in "the sort state of the list of states"

# States.csv import
with open(raw_input("Enter the file name: "),'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for record in reader:
        ListOfStates.append( State(record["State"],record["Capital"],record["Abbreviation"],int(record["Population"]),record["Region"],int(record["US House Seats"])) )
print "\nThere were " + str(len(ListOfStates)) + " state records read.\n"


#Menu option 1 - Print out a report on all states
def PrintStateReport(ListOfStates):
    """
    Prints to the console a formatted report containing all stored data on US states imported. This data is presented in the order the data is currently stored in -- no operation occurs in this function to change the US states data or its storage.

    :param  ListOfStates  List of instantiated State objects.
    """
    #1a - create report headers; format: ["Header Title", Header Length]
    columns = [["State Name",len("State Name")], ["Capital City",len("Capital City")], ["State Abbr",len("State Abbr")], ["State Population",len("State Population")], ["Region",len("Region")], ["US House Seats",len("US House Seats")]]
    
    #1b - determine column widths based on input data
    for record in ListOfStates:
        columns[0][1] = max(columns[0][1],len(record.StateName))
        columns[1][1] = max(columns[1][1],len(record.CapitalCity))
        columns[2][1] = max(columns[2][1],len(record.Abbreviation))
        columns[3][1] = max(columns[3][1],len(record.PopWithCommas))
        columns[4][1] = max(columns[4][1],len(record.Region))
        columns[5][1] = max(columns[5][1],len(str(record.USHouseSeats)))

    #1c - print header text
    for header in columns:
        header[1]+=2
        sys.stdout.write(header[0].ljust(header[1])) #prints header text and spaces to match expected length
    sys.stdout.write("\n")

    #1d - sys.stdout.write(dividing bar b/w header text and state records
    for header in columns:
        for i in range(header[1]):
            sys.stdout.write("-")
    sys.stdout.write("\n")

    #1e - print state records
    for record in ListOfStates:
        sys.stdout.write(record.StateName.ljust(columns[0][1]))
        sys.stdout.write(record.CapitalCity.ljust(columns[1][1]))
        sys.stdout.write(record.Abbreviation.rjust(6).ljust((columns[2][1]))) #the rjust at here reflects expected style shown in Project 1 pdf instructions
        sys.stdout.write(record.PopWithCommas.rjust(12).ljust(columns[3][1])) #the rjust here reflects expected style shown in Project 1 pdf instructions
        sys.stdout.write(record.Region.ljust(columns[4][1]))
        sys.stdout.write(str(record.USHouseSeats).rjust(4).ljust((columns[5][1]))) #the rjust here reflects expected style shown in Project 1 pdf instructions
        sys.stdout.write("\n")
    sys.stdout.write("\n\n") #design doc quirk again
#end PrintStateReport(ListOfStates)

#Menu option 2 - Sort list of states by state name (using Quick sort)
def QuickSort(list):
    """
    Sorts a given list based on its value. Uses popular QuickSort method to do this. Briefly, QuickSort examines given data in halves and subsequent halves, swapping values when it's noticed that a lower number has the higher value, or vice versa.

    :param list List of any kind. Will not function with objects that don't have operators overridden. 
    """
    def partition(list,low,high):
        """
        Internal function. Determines an appropriate pivot point (mid) based on approximate median, then moves other values in the list above or below the pivot point using comparison operators.

        :param  list  List to be partitioned and pivot-sorted.
        :param  low   Lower boundary of the list. Values in the list below this index are not examined.
        :param  high  Higher boudnary of the list. Values in the list above this index are not examined.
        :return       Integer. The index at which the list may be considered sorted up to.
        """
        mid = (low + high)/2
        if list[mid] < list[low]:
            list[mid],list[low] = list[low],list[mid]
        if list[high] < list[low]:
            list[high],list[low] = list[low],list[high]
        if list[mid] < list[high]:
            list[mid],list[high] = list[high],list[mid]
        pivot = list[high]

        i = low-1
        for j in range(low, high):
            if list[j]<=pivot:
                i+=1
                list[i],list[j] = list[j],list[i]
        list[i+1],list[high]=list[high],list[i+1]
        return (i+1)

    def QuickSortAct(list,low,high):
        """
        Internal function. Recursively partitions the input list and sorts the ever-decreasing-in-size partitions, effectively sorting the entire list.

        :param  list  List to be partitioned and pivot-sorted.
        :param  low   Lower boundary of the list. Values in the list below this index are not examined.
        :param  high  Higher boudnary of the list. Values in the list above this index are not examined.
        """
        if low < high:
            intermediary = partition(list, low, high)
            QuickSortAct(list, low, intermediary)
            QuickSortAct(list, intermediary+1, high)

    QuickSortAct(list,0,len(list)-1)
#end QuickSort(list)

#Menu option 3 - Sort list of states by population (using Radix sort)
def RadixSortStates():
    """
    Sorts global variable ListOfStates (which contains all data imported into the program on US states) based on US states' population counts, using Radix sort. Briefly, Radix sort puts a given list of numbers in order by iteratively sorting each digits place (1, 10, 100, etc.) into separate digit piles (0, 1, 2, 3, to 9), which are naturally in numerical order when the piles are finally arranged from start to finish. This particular implementation uses a recursive function to handle each given digits place.

    :return No return value of any kind. Acts on global variables ListOfState and SortState only.
    """
    global ListOfStates
    
    def RadixSortStatesAct(ListOfStates, DigitsPlaceToActOn): #digits place here is 1, 10, 100, etc.
        """
        Internal function. For a given digits place (parameter DigitsPlaceToActOn), sorts input list of state (parameter ListOfStates) into 10 piles based on digits in given digits place (0-9), and returns the list sorted accordingly.

        :param  ListOfStates        List of instantiated State objects.
        :param  DigitsPlaceToActOn  Integer. Used to identify digits place the sort will be based on this iteration. Expected values: 1, 10, 100, 1000, etc.
        :return                     List of instantiated State objects.
        """
        digitsList = [ [], [], [], [], [], [], [], [], [], []] #2d list. first level is 0-9 for digits, second level will be for records found with them
        intermediaryList = []
        for record in ListOfStates:
            digitsList[(record.Population/DigitsPlaceToActOn)%10].append(record)

        for digitPlace in digitsList:
            for record in digitPlace:
                intermediaryList.append(record)

        return intermediaryList
    
    highestPopulationNumber = max(record.Population for record in ListOfStates)
    currentDigitsPlace = 1
    while highestPopulationNumber/currentDigitsPlace > 0: # for each digits place which exists in the highest population number in the data
        ListOfStates = RadixSortStatesAct(ListOfStates,currentDigitsPlace) #sort based on current digits place
        currentDigitsPlace*=10
    global SortState
    SortState = "RadixSort"
#end RadixSortStates(ListOfStates)

#Menu option 4 - Individual state report
def GetState(): #returns State object, or string "State Name not found"
    """
    Conducts a search for a given US state on the basis of its name. User input is called for within the function itself. If global SortState notes that the US states data is currently in alphabetical order based on name, the search conducted is a Binary search. Otherwise, the search conducted is sequential.

    :return State object, or string "Error: State {Name} not found\n"
    """
    SearchString = raw_input("Enter the state name: ")
    global ListOfStates
    global SortState
    #4a binary search, if current list order is state name ABC
    if(SortState=="QuickSort"):
        print "Binary search\n"
        leftboundary = 0
        rightboundary = len(ListOfStates)-1

        while leftboundary <= rightboundary:
            currentSearchPosition = (leftboundary+rightboundary)/2
            if ListOfStates[currentSearchPosition].StateName < SearchString:
                leftboundary = currentSearchPosition+1
            elif ListOfStates[currentSearchPosition].StateName > SearchString:
                rightboundary = currentSearchPosition-1
            else:
                return ListOfStates[currentSearchPosition]
        return "Error: State " + SearchString + " not found\n"

    #4b sequential search, if list order is not currently state name ABC
    else:
        print "Sequential search\n"
        for record in ListOfStates:
            if record.StateName == SearchString:
                return record
        return "Error: State " + SearchString + " not found\n"
#end GetState()

# Menu loop
def MainMenu():
    """
    Manages the main menu loop. Presents menu options, takes user input for selecting menu options, calls associated menu option functions, conducts validation on user input, and allows program exit upon selection.
    """

    def Prompt(text):
        """
        Internal function. Prompts user for menu selection. Validates data, ensuring user input passed along is an integer in range 1-5.

        :param  text  String. The prompt text printed to console before the program waits for user input.
        :return       Integer in range 1-5.
        """
        try:
            userResponse = int(raw_input(text))
            if (userResponse < 1) or (userResponse > 5):
                return Prompt("Invalid choice enter 1-5: ")
            else:
                return userResponse
        except ValueError:
            return Prompt("Invalid choice enter 1-5: ")

    while True:
        menuText = "1. Print a state report\n"
        menuText += "2. Sort by State name\n"
        menuText += "3. Sort by Population\n"
        menuText += "4. Find and print a given state\n"
        menuText += "5. Quit\n"
        menuText += "Enter your choice: "
        userResponse = Prompt(menuText)
        if userResponse == 1:
            print "\n" #expected output style accommodation
            PrintStateReport(ListOfStates)
        elif userResponse == 2:
            QuickSort(ListOfStates)
            global SortState
            SortState = "QuickSort"
            print "\n\nStates sorted by State name.\n"
        elif userResponse == 3:
            RadixSortStates()
            print "\n\nStates sorted by Population.\n"
        elif userResponse == 4:
            print ""
            print GetState()
            print "\n\n"
        elif userResponse == 5:
            print "\nHave a good day!"
            break # Menu option 5 - quit

MainMenu()