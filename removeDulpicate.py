def fun(seq):
    new_seq = [ ]
    for i in seq:
        if i not in new_seq:
            new_seq.append(i)
    return new_seq
print(fun([1,2,3,4,2,1,45,65]))