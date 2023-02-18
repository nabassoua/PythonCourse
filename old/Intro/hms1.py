def hms(n):
    hours=n//3600
    minutes=((n/3600)-hours)*60
    full_minutes=int(minutes)
    seconds=round((minutes-full_minutes)*60)
    
    #initially they are singular
    h="heure"
    m="minute"
    s="seconde"
    
    #modify them to plural when value greater than 1
    
    if (hours > 1):
        h = h.replace("re","res")
    if (full_minutes > 1):
        m = m.replace("te","tes")
    if (seconds > 1):
        s = s.replace("de","des")
    
        
    print("{} {} {} {} {} {}".format(hours,h,full_minutes,m,seconds,s))
        
    
