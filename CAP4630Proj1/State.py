class State(object):
    """
    An Object class for storing and comparing US states. Properties: name, capital city, state abbreviation, population, region, and number of House of Representative seats. Includes the gamut of operator overrides, such that comparisons reference a state's name.
    
    Author: Matthew Dowdie
    Version: Jan 20, 2019
    Email: n00721843@ospreys.unf.edu
    """

    StateName = ""
    @property
    def StateName(self):
        return self._StateName
    @StateName.setter
    def StateName(self,state):
        self._StateName = state

    CapitalCity = ""
    @property
    def CapitalCity(self):
        return self._CapitalCity
    @CapitalCity.setter
    def CapitalCity(self,cap):
        self._CapitalCity = cap

    Abbreviation = ""
    @property
    def Abbreviation(self):
        return self._Abbreviation
    @Abbreviation.setter
    def Abbreviation(self,abbr):
        self._Abbreviation = abbr

    Population = 0
    @property
    def Population(self):
        return self._Population
    @Population.setter
    def Population(self,popul):
        self._Population = popul
        self._PopWithCommas = '{:,}'.format(popul)

    PopWithCommas = ""
    @property
    def PopWithCommas(self):
        return self._PopWithCommas
    @PopWithCommas.setter
    def PopWithCommas(self,popul):
        self._PopWithCommas = popul


    Region = ""
    @property
    def Region(self):
        return self._Region
    @Region.setter
    def Region(self,reg):
        self._Region = reg

    USHouseSeats = 0
    @property
    def USHouseSeats(self):
        return self._USHouseSeats
    @USHouseSeats.setter
    def USHouseSeats(self,inval):
        self._USHouseSeats = inval


    def __init__(self,name,capital,abbr,popul,region,houseseats):
        """
        Initializer method. Instantiates all properties of the class.

        :param name        String   Name of US state.
        :param capital     String   Name of capital city of US state.
        :param abbr        String   Official abbreviation of a US state.
        :param popul       Integer  Population count of a US state.
        :param region      String   Region of the US where given state is considered to be part of.
        :param houseseats  Integer  US House of Representatives count for given US state.
        """
        self.StateName = name
        self.CapitalCity = capital
        self.Abbreviation = abbr
        self.Population = popul
        self.PopWithCommas = '{:,}'.format(popul)
        self.Region = region
        self.USHouseSeats = houseseats


    def __gt__(a,b):
        """
        "Greater Than" override. Based on State Names.

        "Does a occur after b when placed in alphabetical order?"
        
        :param a  State object
        :param b  State object
        :return   Boolean
        """
        if a.StateName > b.StateName:
            return True
        return False

    def __lt__(a,b):
        """
        "Less Than" override. Based on State Names.

        "Does a occur before b when placed in alphabetical order?"
        
        :param a  State object
        :param b  State object
        :return   Boolean
        """
        if a.StateName < b.StateName:
            return True
        return False

    def __le__(a,b):
        """
        "Less Than or Equal To" override. Based on State Names.

        "Does a occur before b when placed in alphabetical order, or perhaps ties with b?"
        
        :param a  State object
        :param b  State object
        :return   Boolean
        """
        if a.StateName <= b.StateName:
            return True
        return False

    def __ge__(a,b):
        """
        "Greater Than or Equal To" override. Based on State Names.

        "Does a occur after b when placed in alphabetical order, or perhaps ties with b?"
        
        :param a  State object
        :param b  State object
        :return   Boolean
        """
        if a.StateName >= b.StateName:
            return True
        return False

    def __eq__(a,b):
        """
        "Equal To" override. Based on State Names.

        "Do a and b share the same state name?"
        
        :param a  State object
        :param b  State object
        :return   Boolean
        """
        if a.StateName == b.StateName:
            return True
        return False

    def __ne__(a,b):
        """
        "Not Equal To" override. Based on State Names.

        "Do a and b have different state names?"
        
        :param a  State object
        :param b  State object
        :return   Boolean
        """
        if a.StateName != b.StateName:
            return True
        return False

    def __str__(self):
        """
        Returns string representation of each property of an instantiated State object.

        :return String. Label and value of each property in order, separated with newlines.
        """

        output = "State Name:        "
        output += self._StateName
        output += "\nCapital City:      "
        output += self._CapitalCity
        output += "\nState Abbr:        "
        output += self._Abbreviation
        output += "\nState Population:  "
        output += self._PopWithCommas
        output += "\nRegion:            "
        output += self._Region
        output += "\nUS House Seats:    "
        output += str(self._USHouseSeats)
        return output