import polib ## MADE BY GAMBIE


mo = polib.mofile('global.mo')

mo.save_as_pofile('IGNORE.po')
po = polib.pofile('IGNORE.po.')
poNEW = polib.POFile()
rename="TEST"








USin = open("US.txt", "r",encoding='UTF-8')
USSRin = open("USSR.txt", "r",encoding='UTF-8')
UKin = open("UK.txt", "r",encoding='UTF-8')
GERMin = open("KRIEG.txt", "r",encoding='UTF-8')
PAin = open("AIS.txt", "r",encoding='UTF-8')
IJNin = open("IJN.txt", "r",encoding='UTF-8')
FRin = open("FR.txt", "r",encoding='UTF-8')
PANAMin = open("PANUS.txt", "r",encoding='UTF-8')
ITALin = open("ITAL.txt", "r",encoding='UTF-8')
EUin = open("EU.txt", "r",encoding='UTF-8')
COMin = open("COMM.txt", "r",encoding='UTF-8')
##



for entry in po:
    if 'IDS_PFS' in str(entry.msgid): ## FR
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=FRin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)

        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid): 
          
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=FRin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)    
        else:
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=entry.msgstr,
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)

 
    if 'IDS_PIS' in str(entry.msgid): ## ITAL
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=ITALin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid): 
         
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=ITALin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)      
        else:
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=entry.msgstr,
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)

    if 'IDS_PGS' in str(entry.msgid): ## GERM
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=GERMin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid): 
            
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=GERMin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)      
        else:
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=entry.msgstr,
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)
            
    if 'IDS_PUS' in str(entry.msgid): ## COMMON
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=COMin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid): 
           
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr= COMin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)      
        else:
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=entry.msgstr,
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)

    if 'IDS_PWS' in str(entry.msgid): ## EU
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=EUin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid): 
           
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=EUin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)      
        else:
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=entry.msgstr,
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)
            
    if 'IDS_PZS' in str(entry.msgid): ## PAN ASIA
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=PAin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid) : 
           
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=PAin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)    
        else:
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=entry.msgstr,
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)

    if 'IDS_PVS' in str(entry.msgid): ## PAN US
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
         
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=PANAMin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid) : 
           
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=PANAMin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)    
        else:
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=entry.msgstr,
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)
            
    if 'IDS_PJS' in str(entry.msgid): ## IJN
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=IJNin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid) : 
         
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=IJNin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)    
        else:
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=entry.msgstr,
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)

    if 'IDS_PRS' in str(entry.msgid): ## USSR
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 

            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=USSRin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid) : 
         
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=USSRin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)    
        else:
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=entry.msgstr,
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)
            
    if 'IDS_PBS' in str(entry.msgid): ## UK
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
           
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=UKin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid) : 
         
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=UKin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)    
        else:
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=entry.msgstr,
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)

    if 'IDS_PAS' in str(entry.msgid): ## US
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
  
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=USin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid) : 
       
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=USin.readline(),
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)    
        else:
            entry = polib.POEntry(
                    msgid=entry.msgid,
                    msgstr=entry.msgstr,
                    occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
                )

            poNEW.append(entry)
        
##        else:
##            print (entry.msgid, entry.msgstr)
##        
##
##
##            entry = polib.POEntry(
##                msgid=entry.msgid,
##                msgstr=rename,
##                occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
##            )
##            poNEW.append(entry)
        
    else:    
        poNEW.append(entry)
        entry = polib.POEntry(
            msgid=entry.msgid,
            msgstr=entry.msgstr,
            occurrences=[('welcome.py', '12'), ('anotherfile.py', '34')]
        )
##poNEW.save('L:/Rename/newfile.po')
        
poNEW.save_as_mofile('globalNew.mo')


USin.close() 
USSRin.close() 
UKin.close() 
GERMin.close() 
PAin.close() 
IJNin.close() 
FRin.close()
PANAMin.close()
ITALin.close()
EUin.close()
COMin.close() 
