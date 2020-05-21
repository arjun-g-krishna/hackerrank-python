if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    first = second = -2147483648
    for i in range(n):
        if arr[i]>first :
            second=first
            first=arr[i]
        elif arr[i]>second and arr[i] != first:
            second=arr[i]
    print  second       
