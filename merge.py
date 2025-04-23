def merge_sort(mm):
    n = len(mm)
    hisse=1
    while hisse<n:
        temp=[]
        sol=0
        while sol+hisse<n:
            sag = sol + hisse
            sol_son=sag-1
            sag_son = sol_son+hisse if sol_son+hisse<n else n-1
            i=sol
            j=sag
            while i<=sol_son and j<=sag_son:
                if mm[i]<mm[j]:
                     temp.append(mm[i])
                     i=i+1
                else:
                    temp.append(mm[j])
                    j=j+1
            while i<=sol_son:
                temp.append(mm[i])
                i=i+1
            while j<=sag_son:
                temp.append(mm[j])
                j=j+1
            sol=sol+2*hisse
        hisse=hisse*2
        for t in range(0,sag_son+1):
            mm[t] = temp[t]
massiv = [3,2,5,1,7,4,16,15,14,13,12,11,9,6,10,8]
merge_sort(massiv)
print(massiv)