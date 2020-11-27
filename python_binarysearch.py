# https://www.youtube.com/watch?v=zeULw-a7Mw8
data = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
target = 4

def linear_search ( data, target ):
    for i  in range ( len ( data ) ):
        if ( data [ i ] == target ):
            return True
        else:
            return False

def binary_search_iterative ( data, target ):
    low = 0
    high = len ( data ) - 1

    while low <= high:
        mid = ( low + high ) // 2
        if target == data [ mid ]:
            return True
        elif target < data [ mid ]:
            high = mid - 1
        else:
            low = mid + 1
    return False

def binary_search_recursive ( data, target, low, high ):
    if low > high:
        return False
    else:
        mid = ( low + high ) // 2
        if target == data [ mid ]:
            return True
        elif target < data [ mid ]:
            return binary_search_recursive ( data, target, low, mid - 1 )
        else:
            return binary_search_recursive ( data, target, mid + 1, high )

print ( binary_search_iterative ( data, target ) )
print ( binary_search_recursive ( data, target, 0, len ( data ) ) )
