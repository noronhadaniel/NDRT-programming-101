def StringWithoutDuplicates(string):
    outstring = ""
    for x in string:
        if x not in outstring:
            outstring += x
    
    return outstring

string = "mississippi"

print(StringWithoutDuplicates(string))
