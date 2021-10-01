def remove_nl(str):
    if "\n" in str:
        ret = str[0:-1]
        return ret
    else:
        return str

def pto_int(ls):
    ret = []
    if (len(ls) != 4):
        for x in ls:
            ret.append(int(x))
    else:
        ret.append(ls[0][1:-1])
        ret.append(int(ls[1]))
        ret.append(int(ls[2]))
        ret.append(int(ls[3]))

    return ret

def read_csv(csv_file_path):

    f = open(csv_file_path, 'r')
    lines = f.readlines()
    
    X = []

    for line in lines:
        temp = remove_nl(line)
        temp2 = pto_int(temp.split(','))
        X.append(temp2)
    
    f.close()

    return X
    #"""
    #    Given a path to a csv file, return a matrix (list of lists)
    #    in row major.
    #"""
    #raise NotImplementedError()
