class Matrix:
    """
    Class to contain a cost-value matrix used for maximum value/capacity
    problems
    """

    def __init__(self,rows,columns):
        """
        Creates a virtual 2-d array and initializes values to zero

        Inputs: 
        rows: the number of rows to be added to the array
        columns: the number of columns to be added to the array
        """
        self._row = []
        self._array = []
        self._items = []
        
        #create an empty row len(columns) units long
        for i in range(columns):
            self._row.append(0)

        #add an empty row len(columns) units long for every row required
        for i in range(rows):
            self._array.append(self._row[0:])

    def setBox(self,row,column,value):
        """
        Sets the box at position [row][column] in the matrix to value
        """
        self._array[row][column] = value

    def getBox(self,row,column):
        """
        Returns the value of the box at position [row][column] in the matrix
        """
        return self._array[row][column]

    def getLength(self):
        """
        returns the number of rows in the array
        """
        return len(self._array)

    def getWidth(self):
        """"
        returns the number of columns in the array
        """
        return len(self._row)

    def getItems(self, weights):
        """
        return the optimal list of items as determined by the array 
        value will be 0 if not included, and 1 if inluded

        Input:
        weights: the list of weights of the items
        """

        i = self.getLength()-1 #will be the number of items
        w = (self.getWidth()-1) #will be the capacity
        for d in range(0, self.getLength()):
            self._items.append(0)

        while (i >= 0 and w >=0):
            #If the value in the array is not equal to the value of the 
            #last item at the current capacity left, then it is included in the
            #optimal list
            #if there is not last item, then it is included if it's value at the
            #current weight is greater than 0
            if ((i==0 and self.getBox(i,w) > 0) or \
                    (self.getBox(i,w) != self.getBox(i-1,w))):
                self._items[i] = 1
                w = w-weights[i]
            i -= 1
        return self._items
            
def max_val_group(cap,weights,values):
    """
    Determines the group of units, based on lists of inputted weights and values
    with the highest value, and returns a list of which units should be included
    in the group to have the maximum value

    Inputs:
    cap: the maximum capacity possible for the group
    weights: a list of the weights of items to be added to the group
    values: a list of the values of items to be added to the group
    
    NOTE: for any number i in range 0 to the length of either the weights or
    values lists weights[i] and values[i] refers to the same item to be added to
    the group

    Output:
    A list of equal length to the weights and values list, with each value being
    either 0 or 1. If the value is 1 then the unit is a part of the maximum 
    value group.

    Running Time:
    O(nC), where n is the number of items that can be added to the solution, and
    C is the inputted capacity that the solution group needs to fit in.
    This is the running time because it uses dynamic programming with n*C 
    subproblems, shown below by the nested for loops
    """
    num_items = len(values)
    #matrix to contain the cost/value values
    cost_val = Matrix(num_items,cap+1)

    #Goes over every item 
    for item in range(0,num_items):
        #With every possible size up to the capacity
        for size in range(0,cap+1):
            if weights[item] > size:
                #this item is too heavy for this size, so keep the previous 
                #item's value
                cost_val.setBox(item,size, cost_val.getBox(item-1,size))
            else:
                #add the item if it gives us a higher value than skipping it
                cost_val.setBox(item,size, (max(cost_val.getBox(item-1,size), \
                    values[item] + cost_val.getBox(item-1,size-weights[item]))))
    
    return cost_val.getItems(weights)
