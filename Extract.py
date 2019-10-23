import polib ## MADE BY GAMBIE


mo = polib.mofile('global.mo')

mo.save_as_pofile('IGNORE.po')
po = polib.pofile('IGNORE.po.')
poNEW = polib.POFile()
rename="TEST"


US = open("US.txt", "w",encoding='UTF-8')
USSR = open("USSR.txt", "w",encoding='UTF-8')
UK = open("UK.txt", "w",encoding='UTF-8')
GERM = open("KRIEG.txt", "w",encoding='UTF-8')
PA = open("AIS.txt", "w",encoding='UTF-8')
IJN = open("IJN.txt", "w",encoding='UTF-8')
FR = open("FR.txt", "w",encoding='UTF-8')
PANAM = open("PANUS.txt", "w",encoding='UTF-8')
ITAL = open("ITAL.txt", "w",encoding='UTF-8')
EU = open("EU.txt", "w",encoding='UTF-8')
COM = open("COMM.txt", "w",encoding='UTF-8')
##



for entry in po:
    if 'IDS_PFS' in str(entry.msgid): ## FR
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            FR.write(entry.msgstr)
            FR.write('\n')
            

           

        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid): 
            FR.write(entry.msgstr)
            FR.write('\n')
            

           

 
    if 'IDS_PIS' in str(entry.msgid): ## ITAL
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            ITAL.write(entry.msgstr)
            ITAL.write('\n')
           
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid): 
            ITAL.write(entry.msgstr)
            ITAL.write('\n')
     
       

    if 'IDS_PGS' in str(entry.msgid): ## GERM
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            GERM.write(entry.msgstr)
            GERM.write('\n')
           
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid): 
            GERM.write(entry.msgstr)
            GERM.write('\n')
      
            
    if 'IDS_PUS' in str(entry.msgid): ## COMMON
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            COM.write(entry.msgstr)
            COM.write('\n')
         
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid): 
            COM.write(entry.msgstr)
            COM.write('\n')
               
   

    if 'IDS_PWS' in str(entry.msgid): ## EU
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            EU.write(entry.msgstr)
            EU.write('\n')
       
         
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid): 
            EU.write(entry.msgstr)
            EU.write('\n')
           
      
            
    if 'IDS_PZS' in str(entry.msgid): ## PAN ASIA
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            PA.write(entry.msgstr)
            PA.write('\n')

        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid) : 
            PA.write(entry.msgstr)
            PA.write('\n')
  

    if 'IDS_PVS' in str(entry.msgid): ## PAN US
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            PANAM.write(entry.msgstr)
            PANAM.write('\n')
    
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid) : 
            PANAM.write(entry.msgstr)
            PANAM.write('\n')
  
            
    if 'IDS_PJS' in str(entry.msgid): ## IJN
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            IJN.write(entry.msgstr)
            IJN.write('\n')
     
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid) : 
            IJN.write(entry.msgstr)
            IJN.write('\n')
  
    if 'IDS_PRS' in str(entry.msgid): ## USSR
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            USSR.write(entry.msgstr)
            USSR.write('\n')
      
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid) : 
            USSR.write(entry.msgstr)
            USSR.write('\n')
        
    if 'IDS_PBS' in str(entry.msgid): ## UK
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            UK.write(entry.msgstr)
            UK.write('\n')
     
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid) : 
            UK.write(entry.msgstr)
            UK.write('\n')
           
   

    if 'IDS_PAS' in str(entry.msgid): ## US
        
        print (len(entry.msgid), entry.msgid, entry.msgstr)
        
        if len(entry.msgid) == 11: 
            US.write(entry.msgstr)
            US.write('\n')
        
        if len(entry.msgid) == 16 and '_FULL' in str(entry.msgid) : 
            US.write(entry.msgstr)
            US.write('\n')
   
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
        

##poNEW.save('L:/Rename/newfile.po')
        



US.close() 
USSR.close() 
UK.close() 
GERM.close() 
PA.close() 
IJN.close() 
FR.close()
PANAM.close()
ITAL.close()
EU.close()
COM.close()



