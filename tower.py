def tower(disk,source,auxi,dest):
    if(disk==1):
        print("Move {} from {} to {} .format")
        return
    else:
        tower(disk-1,source,dest,auxi)
        print("Move {} from {} to {}".format(disk,source,dest))
        tower(disk-1,auxi,source,dest)
disk= int(input("Enter the number:"))
print("Steps involved are:")
tower(disk,'A','B','C')
