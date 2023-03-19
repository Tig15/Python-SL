# try block lets you test a block of code for errors.
try:
    print(x)
except:
    print("An Exception Occured") 

# except block lets you handle the error.

# else block lets you execute code when there is no errors.
try:
    print("Hey")
except:
    print("Something Went Wrong!")
else: 
    print("Nothing Went Wrong") 

# finally block lets you excute code, regardless of the result of the try- and except block.
try:
    print(y)
except:
    print("Something went wrong") 
finally:
    print("try block ")

#
try:
    f = open("zex.txt") 
    try:
        f.write("Aman Srivastava") 
    except:
        print("Something went wrong when writing to file")
    finally:
        f.close()
except:
    print("Something went wrong when opening a file")                            