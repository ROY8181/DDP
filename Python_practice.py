# list comprehension 
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    coordinate = []
    for i in range(0,x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                if i+j+k != n:
                    coordinate.append([i,j,k])
    print(coordinate)
# find run-up score
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x = list(arr)
    x.sort()
print(x[2])

#leap year
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
            
    
    return leap
