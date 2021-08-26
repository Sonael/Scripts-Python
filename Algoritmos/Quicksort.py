# Written by Magnus Lie Hetland

                #arr,  p,    r
def partition(list, start, end):
    #x
    pivot = list[end]
    #i
    bottom = start-1
    top = end

    done = 0
    while not done:

        while not done:
            # i
            bottom = bottom + 1
            #      i      r           para o laço
            if bottom == top:
                done = 1
                break
            #lista no indice i       ultimo item na lista
            if list[bottom] > pivot:
                #lista no ultimo indice  recebe lista no indice i 
                list[top] = list[bottom]
                break

        while not done:
            #r      r-1
            top = top-1
            # r for igual a i
            if top == bottom:
                done = 1
                break
            # top for maior do que x
            if list[top] < pivot:
                list[bottom] = list[top]
                break

    list[top] = pivot
    return top

 def quicksort(list, start, end):
   if start < end:
        split = partition(list, start, end)
        quicksort(list, start, split-1)
        quicksort(list, split+1, end)
   else:
        return

 if __name__=="__main__":
    import sys
    list = map(int,sys.argv[1:])
    start = 0
    end = len(list)-1
    quicksort(list,start,end)
    print ' '.join(map(str,list))
