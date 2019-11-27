def almostIncreasingSequence(sequence):
    a = []
    b = []
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:       
            cur = sequence.pop(i)
            for j in sequence:
                a.append(j)
            sequence.insert(i,cur)
            temp = sequence.pop(i+1)
            for k in sequence:
                b.append(k)
            sequence.insert(i+1,temp)
            break
    
    if len(a) == 0 or len(b) == 0:        
        if sorted(sequence) == sequence and len(set(sequence)) == len(sequence):
            return True
        else:
            return False
    else:
        if (sorted(a) == a and len(set(a)) == len(a)) or (sorted(b) == b and len(set(b)) == len(b)):
            return True
        else:
            return False
