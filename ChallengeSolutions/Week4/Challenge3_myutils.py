import math, os, json

"""
Utility functions for other python programs
"""

def header(htext, capitalize = True, charnum = 100, char = "-"):
    """
    Prepares a standard program header using given text.
    htext is text that must be provided. 
    capitalize can be True/False only (boolean).
    charnum can be modified if needed (default = 100); char as well (default = -), but avoid using /
    """
    htext = str(htext).strip()
    if capitalize:
        htext = htext.upper()
    lentxt = len(htext)
    if lentxt > charnum:
        charnum = lentxt
    spacenum = (charnum - lentxt) // 2
    # print("-" * 100 + "\n\n" + " " * 42 + "FUNCTION ANALYZER" + "\n\n" + "-" * 100 + "\n")
    return print(char * charnum + "\n\n" + " " * spacenum + htext + "\n\n" + char * charnum + "\n")


def sortdict(dic, sortk = False, sortv = False, sortrev = False):
    """
    Sorts given dictionary alphabetically[A-Z]. (default is by key)
    Could change bool flags sortk, sortv and sortrev for:
    Key sort or Value sort, and/or reverse sort[Z-A].
    Output is sorted dictionary as per parameters.
    """
    try:
        dic = dict(dic)
        sortk = bool(sortk)
        sortv = bool(sortv)
        sortrev = bool(sortrev)
    except:
        return None
    if not sortk and not sortv:
        return dic
    elif sortk and sortv:
        return dic

    dc = dic.copy()
    #dcrev = {Value: Key for Key, Value in dc.items()}
    dck = list(dc.keys())
    #dcv = list(dc.values())
    #sort = sorted(dc.items(), key=lambda x: x[1], reverse=True)
    sorteddc = {}
    
    if sortrev:
        if sortk:
            sklst = sorted(dck, reverse = True)
            for x in sklst:
                sorteddc.update({x: dc[x]})
        elif sortv:
            sort = sorted(dc.items(), key=lambda x: x[1], reverse=True)
            for k, v in sort:
                sorteddc.update({k:v})
    elif sortk:
        sklst = sorted(dck)
        for x in sklst:
            sorteddc.update({x: dc[x]})
    elif sortv:
        sort = sorted(dc.items(), key=lambda x: x[1])
        for k, v in sort:
            sorteddc.update({k:v})

    return sorteddc


def dicttable(d,  heading = "", padding = 5, hasheaders = False, reverse = False, clear = False, sortk = False, sortv = False, sortrev = False):
    """
    Takes dictionary as input and creates a decorated table using keys and values.
    Default (side) padding is 5 spaces (left and right).
    All items in table will be centered.
    Column headers are optional. If column header is first item, set flag to True.
    Table heading is optional and reverse flag swaps keys/values in output table. Clear clears screen.
    """
    if type(d) != dict:
        return print("\nERROR: Function requires a dictionary as input!\n\a")
    elif len(d) == 0:
        return print("\nNO RESULT!\n\a")

    try:
        padding = int(padding)
        heading = str(heading)
        hasheaders = bool(hasheaders)
        reverse = bool(reverse)
        clear = bool(clear)
        sortk = bool(sortk)
        sortv = bool(sortv)
        sortrev = bool(sortrev)

    except:
        return print("\nERROR: Check parameter data types. padding must be int, heading must be str, ALL flags must be Boolean!\n\a")
    if padding < 1:
        padding = 1
    if clear:
        os.system('cls')
    maxlen_k = maxlen_v = prevklen = prevvlen = 0
    dc = d.copy()
    if reverse:
        dc = {value:key for key, value in dc.items()}
    for k, v in dc.items():
        if len(str(k).strip()) > maxlen_k:
            maxlen_k = len(str(k).strip())
        if len(str(v).strip()) > maxlen_v:
            maxlen_v = len(str(v).strip())
    
    diff = len(str(heading).strip()) - ((maxlen_k + maxlen_v + padding * 4)+1)

    s = s1 = s2 = s3 = s4 = 0
    if diff > 0:
        padding += (diff//4)
        s = diff % 4
        if s == 1:
            s4 = 1
        elif s == 2:
            s4 = 1
            s1 = 1
        elif s == 3:
            s4 = 1
            s1 = 1
            s3 = 1
        else:
            pass

    rlen = maxlen_k + maxlen_v + padding * 4


    if len(str(heading).strip()) != 0:
        print("+" + "-" * (rlen+1+s) + "+")
        x = u"\u00A6" + " " * (rlen+1+s) + u"\u00A6"
        print(x)
        padl = math.floor(((rlen+1)-len(str(heading).strip()))/2)
        padr = math.ceil(((rlen)-len(str(heading).strip()))/2)
        y = u"\u00A6" + " " * (padl+s1+s2) + heading.strip() + " " * (padr+s3+s4) + u"\u00A6"
        if len(x)>len(y):
            padr = math.ceil(((rlen+1)-len(str(heading).strip()))/2)
        elif len(x)<len(y):
            padr = math.ceil(((rlen-1)-len(str(heading).strip()))/2)
        print(u"\u00A6" + " " * (padl+s1+s2) + heading.strip() + " " * (padr+s3+s4) + u"\u00A6")
        print(u"\u00A6" + " " * (rlen+1+s) + u"\u00A6")
    rsk = maxlen_k - len(str(list(dc.keys())[0]).strip())
    rsv = maxlen_v - len(str(list(dc.values())[0]).strip())
    test = rsk > 0 or rsv > 0
    if hasheaders == True:
        print("+" + "=" * (s1+s2+maxlen_k + padding * 2) + "+" + "=" * (s3+s4+maxlen_v + padding * 2) + "+")
        print("|" + " " * (s1+s2+maxlen_k + padding * 2) + "|" + " " * (s3+s4+maxlen_v + padding * 2) + "|")
        
        if rsk > 0 and rsv > 0:
            print("|" + " " * (s1+padding+math.floor(rsk/2)) + str(list(dc.keys())[0]).strip() + " " * (s2+padding+math.ceil(rsk/2)) + "|", end="")
            print(" " * (s3+padding+math.floor(rsv/2)) + str(list(dc.values())[0]).strip() + " "* (s4+padding + math.ceil(rsv/2)) + "|")
            print("|" + " " * (s1+s2+maxlen_k + padding * 2) + "|" + " " * (s3+s4+maxlen_v + padding * 2) + "|")
            print("+" + "=" * (s1+s2+maxlen_k + padding * 2) + "+" + "=" * (s3+s4+maxlen_v + padding * 2) + "+")
            del dc[list(dc.keys())[0]]
            prevklen = maxlen_k
            prevvlen = maxlen_v
            maxlen_k = maxlen_v = 0
            for k, v in dc.items():
                if len(str(k).strip()) > maxlen_k:
                    maxlen_k = len(str(k).strip())
                if len(str(v).strip()) > maxlen_v:
                    maxlen_v = len(str(v).strip())
            prevklen -= maxlen_k
            prevvlen -= maxlen_v

        elif test:
            if rsk > 0:
                print("|" + " " * (s1+padding+math.floor(rsk/2)) + str(list(dc.keys())[0]).strip() + " " * (s2+padding+math.ceil(rsk/2)) + "|", end="")
                print(" " * (s3+padding) + str(list(dc.values())[0]).strip() + " "* (s4+padding) + "|")
                print("|" + " " * (s1+s2+maxlen_k + padding * 2) + "|" + " " * (s3+s4+maxlen_v + padding * 2) + "|")
                print("+" + "=" * (s1+s2+maxlen_k + padding * 2) + "+" + "=" * (s3+s4+maxlen_v + padding * 2) + "+")
                del dc[list(dc.keys())[0]]
                prevklen = maxlen_k
                prevvlen = maxlen_v
                maxlen_k = maxlen_v = 0
                for k, v in dc.items():
                    if len(str(k).strip()) > maxlen_k:
                        maxlen_k = len(str(k).strip())
                    if len(str(v).strip()) > maxlen_v:
                        maxlen_v = len(str(v).strip())
                prevklen -= maxlen_k
                prevvlen -= maxlen_v
            elif rsv > 0:
                print("|" + " " * (s1+padding) + str(list(dc.keys())[0]).strip() + " " * (s2+padding) + "|", end="")
                print(" " * (s3+padding+math.floor(rsv/2)) + str(list(dc.values())[0]).strip() + " "* (s4+padding + math.ceil(rsv/2)) + "|")
                print("|" + " " * (s1+s2+maxlen_k + padding * 2) + "|" + " " * (s3+s4+maxlen_v + padding * 2) + "|")
                print("+" + "=" * (s1+s2+maxlen_k + padding * 2) + "+" + "=" * (s3+s4+maxlen_v + padding * 2) + "+")
                del dc[list(dc.keys())[0]]
                prevklen = maxlen_k
                prevvlen = maxlen_v
                maxlen_k = maxlen_v = 0
                for k, v in dc.items():
                    if len(str(k).strip()) > maxlen_k:
                        maxlen_k = len(str(k).strip())
                    if len(str(v).strip()) > maxlen_v:
                        maxlen_v = len(str(v).strip())
                prevklen -= maxlen_k
                prevvlen -= maxlen_v
        else:
            print("|" + " " * (s1+padding) + str(list(dc.keys())[0]).strip() + " " * rsk + " " * (s2+padding) + "|", end="")
            print(" " * (s3+padding) + str(list(dc.values())[0]).strip() + " " * rsv + " "* (s4+padding) + "|")
            print("|" + " " * (s1+s2+maxlen_k + padding * 2) + "|" + " " * (s3+s4+maxlen_v + padding * 2) + "|")
            print("+" + "=" * (s1+s2+maxlen_k + padding * 2) + "+" + "=" * (s3+s4+maxlen_v + padding * 2) + "+")
            del dc[list(dc.keys())[0]]
            prevklen = maxlen_k
            prevvlen = maxlen_v
            maxlen_k = maxlen_v = 0
            for k, v in dc.items():
                if len(str(k).strip()) > maxlen_k:
                    maxlen_k = len(str(k).strip())
                if len(str(v).strip()) > maxlen_v:
                    maxlen_v = len(str(v).strip())
            prevklen -= maxlen_k
            prevvlen -= maxlen_v
    else:
        print("+" + u"\u2014" * (s1+s2+maxlen_k + padding * 2) + "+" + u"\u2014" * (s3+s4+maxlen_v + padding * 2) + "+")

    dc = sortdict(dc, sortk, sortv, sortrev)

    for k, v in dc.items():
        rsk = maxlen_k - len(str(k).strip())
        rsv = maxlen_v - len(str(v).strip())

        print("|" + " " * (s1+padding+math.floor(prevklen/2)+math.floor(rsk/2)) + str(k).strip() + " " * (math.ceil(rsk/2)) + " "* (s2+padding+math.ceil(prevklen/2)) + "|", end="")
        print(" " * (s3+padding+math.floor(prevvlen/2)+math.floor(rsv/2)) + str(v).strip() + " " * (math.ceil(rsv/2)) + " "* (s4+padding+math.ceil(prevvlen/2)) + "|")
        print("+" + u"\u2014" * (s1+s2+prevklen+maxlen_k + padding * 2) + "+" + u"\u2014" * (s3+s4+prevvlen+maxlen_v + padding * 2) + "+")
    return dc

# dt = {"Alpha": "1", "Beta": "2", "Epsilon": "3"}
# dicttable(dt, hasheaders = True, heading = "Greek", reverse = False, clear = True)

def lookupsubset(dc, kORv, v = False, head = False, exact = False, heading = "", padding = 5, clear = False, sortk = False, sortv = False, sortrev = False):
 
    d2 = dc.copy()
    outdic = {}
    kORv = str(kORv).strip().lower()

#    if v:
#        d2 = {value: key for key, value in d2.items()}
    if head:
        outdic = {str(list(d2.keys())[0]).strip(): str(list(d2.values())[0]).strip()}
        
    # str(x).strip().lower()
    try:
        if exact:
            if v:
                for key, value in d2.items():
                    if str(value).strip().lower() == kORv:
                        outdic.update({str(key).strip(): str(value).strip()})
            else:
                for key, value in d2.items():
                    if str(key).strip().lower() == kORv:
                        outdic.update({str(key).strip(): str(value).strip()})
        elif v:
            for key, value in d2.items():
                if kORv in str(value).strip().lower():
                    outdic.update({str(key).strip(): str(value).strip()})        
        else:
            for key, value in d2.items():
                if kORv in str(key).strip().lower():
                    outdic.update({str(key).strip(): str(value).strip()})
        dicttable(outdic, heading, padding, head, False, clear, sortk, sortv, sortrev)
        return outdic
    except:
        dicttable(outdic, heading, padding, head, False, clear, sortk, sortv, sortrev)
        return outdic

def EMPTYFILE(file):
    with open(file, 'w') as f:
        f.write("")
        f.close()
    return 0

def jsontodict(jsonfile):
    with open(jsonfile, 'r') as apdb:
        d = apdb.read()
        dc = json.loads(d)
        apdb.close()
    return dc

def dicttojson(indict, dumpfile, mode='w'):
    """
    Only use for two level or one level dictionary.
    """
    with open(dumpfile, mode) as newdb:
        x = json.dumps(indict)
        dw = x.replace(": {", ": {\n\t\t")
        dw = dw.replace(", \"", ",\n\t\t\"")
        dw = dw.replace("},", "\n\t},")
        dw = dw.replace("},\n\t\t", "},\n\t")
        dw = dw.replace("{\"", "{\n\t\"")
        dw = dw.replace("}}", "\n\t}\n}")
        if "{" not in str(indict.values()): # - for 1 level dict!
            dw = dw.replace(dw[-1], f"\n{dw[-1]}")
            dw = dw.replace("\t\t", "\t")
        newdb.write(dw + "\n")
        newdb.close()
    return 0

def dcextract(dc, key2, kheader="", vheader=""):
    """
    Converts 2 level dictionary into 1 level.
    Uses 2nd level key as input for lookup.
    If headers are required, enter them. Key(k) header is for left column, Val(v) header is for right column.
    Can merge dictionaries.
    """
    outdc = {}
    kheader = str(kheader).strip()
    vheader = str(vheader).strip()
    if len(kheader) > 0 and len(vheader) > 0:
        outdc.update({kheader: vheader})
    elif len(kheader) > 0:
        outdc.update({kheader: ""})
    elif len(vheader) > 0:
        outdc.update({vheader: ""})
    

    if type(dc) != dict:
        return print("\nERROR: Function requires a dictionary as input!\n\a")
    if "{" not in str(dc.values()):
        for k, v in dc.items():
            outdc.update({k, v})
        return outdc
    
    dcc = dc.copy()
    o = "NULL"

    for k, v in dcc.items():
        td = dict(v)
        if key2 in td.keys():
            o = td[key2]
        outdc.update({k: o})

    return outdc


# dicttojson(dt, './Playaround/test.json')
# dicttojson(jsontodict('./Playaround/airports.json'), './Playaround/test.json')
# jsontodict('./Playaround/airports.json')
# json.loads(x)-> json ==> pydict
# json.dumps(x)-> pydict ==> json
# use print(dict(sorted(d.items(), reverse = False/True)))
# sort by value (with lambda) -> {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
# EMPTYFILE('./Playaround/test.json')
# isinstance(x, int) checks type of input
# sort = sorted(dc.items(), key=lambda x: x[1], reverse=True) - Sort by value
# dict(sorted(dc.items(), reverse = True)) - Sort by key
"""
sys.stdout = open(".\Playaround\\airport_table.txt", "w")
#dicttable(cleandb, f"Table of {len(db)} Airport ICAO Codes and their Names".upper(), hasheaders=True, clear=True, reverse = False)
sys.stdout.close()
sys.stdout = sys.__stdout__
"""