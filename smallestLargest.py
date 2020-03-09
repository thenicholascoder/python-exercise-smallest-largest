#variables/storages 
largest = None
smallest = None

#starting an indefinite loop
while True:

    #get input and store it to inp
    inp = input("Enter a number: ")

    #filter/compare it using if condition
    if inp == "done" : break

    #using try if ever it traceback error
    try:
        num = float(inp)

    #if it blows up this will run
    except:
        print("Invalid input")
        continue

    #i used is because it is stronger than "==" and it is for primer
    if smallest is None:
        #store the current num to smallest
        smallest = num

    #condition if current number is greater than "largest" storage 
    if num > largest :
        #overwrite the largest
        largest = num

    #condition else if current number is less than the "smallest" storage
    elif num < smallest :
        #overwrite the smallest
        smallest = num

#creating a function to pass the smallest and largest which is already made by program
def smallestLargest(largest,smallest):
    print("Maximum is", int(largest))  
    print("Minimum is", int(smallest))

#invoke the function
smallestLargest(largest,smallest)
