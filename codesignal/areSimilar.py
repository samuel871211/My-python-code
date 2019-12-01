def areSimilar(a, b):
    count = 0
    if sorted(a) == sorted(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        if count > 2:
            return False
        else:
            return True
    return False
