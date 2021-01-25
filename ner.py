
import re
import sys


LOCATIONS     = []            
ORGANIZATIONS = []
PERSON       = []
DATES       = []


with open('date_lexicon.txt', encoding='utf-8') as d:
    for line in d:
        DATES.append(line.rstrip())

with open('locations_lexicon.txt', encoding='utf-8') as d:
    for line in d:
        LOCATIONS.append(line.rstrip())

with open('person_lexicon.txt', encoding='utf-8') as d:
    for line in d:
        if len(line.rstrip()) > 2:
            PERSON.append(line.rstrip())

with open('organization_lexicon.txt', encoding='utf-8') as d:
    for line in d:
        ORGANIZATIONS.append(line.rstrip())




filename = sys.argv[1]
lineNum = 1



with open(filename, encoding='utf-8') as f:
    for line in f:

        #####################################
        #Person

        # All one word names
        for oneName in re.findall(r'[^0-9][^0-9]([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)[.\s\',][^A-ZÇĞİÖŞÜ-]',line):
            if oneName in PERSON:
                if oneName not in DATES:
                    if oneName not in LOCATIONS:
                        print("Line {}:".format(lineNum),"PERSON", oneName)
                        

        # Name and Surname
        for oneName in re.findall(r'[^0-9][^0-9](([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s([A-ZÇĞİÖŞÜ][a-zçğıöşü]+))[.\s\',][^A-ZÇĞİÖŞÜ]',line):
            check = False
            for oneName2 in re.findall(r'[^0-9][^0-9](([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]+)[.\s\',][^A-ZÇĞİÖŞÜ]',line):
                
                if oneName[0] in oneName2[0]:
                    check = True
                    if oneName2[1] not in PERSON:
                        check = False
                    break
            if check == False:
                if oneName[1] in PERSON:
                    if oneName not in DATES:
                        if oneName not in LOCATIONS:
                            if ("Hanım" in oneName[2]) or ("Abla" in oneName[2]) or ("Bey" in oneName[2]) or ("Abi" in oneName[2]) or ("Hoca" in oneName[2]):
                                print("Line {}:".format(lineNum),"PERSON", oneName[1])
                                
                            elif ('Köy' not in oneName[2]) and ('Dağ' not in oneName[2]) and ('Mahalle' not in oneName[2]) and ('Sokak' not in oneName[2]) and ('Cadde' not in oneName[2]) and ('Apartman' not in oneName[2]) and ('Büro' not in oneName[2]) and ('Köprü' not in oneName[2]) and ('Saray' not in oneName[2]) and ('Mezarlı' not in oneName[2]) and ('Köşk' not in oneName[2]) and ('Şelale' not in oneName[2]) and ('Kale' not in oneName[2]) and ('Kule' not in oneName[2]) and ('Adası' not in oneName[2]) and ('Plaj' not in oneName[2]) and ('Manastır' not in oneName[2]) and ('Türbe' not in oneName[2]) and ('Yayla' not in oneName[2]) and ('Irmağı' not in oneName[2]) and ('Dere' not in oneName[2]) and ('Müze' not in oneName[2]) and ('Cezaevi' not in oneName[2]) and ('Park' not in oneName[2]) and ('Camii' not in oneName[2]) and ('Cami' not in oneName[2]) and ('Tapına' not in oneName[2]) and ('Kilise' not in oneName[2]) and ('Mescid' not in oneName[2]) and ('Anıt' not in oneName[2]) and ('Katedral' not in oneName[2]) and ('Heykel' not in oneName[2]) and ('Çayı' not in oneName[2]) and ('Nehri' not in oneName[2]) and ('Göl' not in oneName[2]) and ('İmparatorlu' not in oneName[2]) and ('spor' not in oneName[2]) and ('AŞ' not in oneName[2]) and ('LTD' not in oneName[2]) and ('Radyo' not in oneName[2]) and ('TV' not in oneName[2]) and ('HD' not in oneName[2]) and ('SK' not in oneName[2]) and ('FC' not in oneName[2]):
                                #print(oneName)
                                print("Line {}:".format(lineNum),"PERSON", oneName[0])
                                
        

        # For Two Name People
        for oneName in re.findall(r'[^0-9][^0-9](([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]+)[.\s\',][^A-ZÇĞİÖŞÜ]',line):
            if (oneName[1] in PERSON) and (oneName[2] in PERSON):
                print("Line {}:".format(lineNum),"PERSON", oneName[0])
                

        # Special Case - All Surname Upper
        # Name SURNAME
        for oneName in re.findall(r'[^0-9][^0-9](([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s([A-ZÇĞİÖŞÜ]{2,}))[.\s\',][^A-Z]',line):
            check = False
            for oneName2 in re.findall(r'(([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s[A-ZÇĞİÖŞÜ]{2,})[.\s\',][^A-ZÇĞİÖŞÜ]',line):
                if oneName[0] in oneName2[0]:
                    check = True
                    if oneName2[1] not in PERSON:
                        check = False
                    break
            if check == False:
                if oneName[1] in PERSON:
                    if ('AŞ' not in oneName[2]) and ('SK' not in oneName[2]) and ('LTD' not in oneName[2]) and ('JK' not in oneName[2]) and ('FC' not in oneName[2]):
                        print("Line {}:".format(lineNum),"PERSON", oneName[0])
                        

        # Name Name SURNAME
        for oneName in re.findall(r'[^0-9][^0-9](([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s[A-ZÇĞİÖŞÜ]{2,})[.\s\',][^A-ZÇĞİÖŞÜ]',line):
            if (oneName[1] in PERSON) and (oneName[2] in PERSON):
                print("Line {}:".format(lineNum),"PERSON", oneName[0])
                

        # For names have ' or - such as John D'Largy or Hector Sausage-Hausen
        for oneName in re.findall(r'[^0-9][^0-9](([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*)\s[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*[\'-][A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*)[.\s\',][^A-ZÇĞİÖŞÜ]',line):
            if oneName[1] in PERSON:
                print("Line {}:".format(lineNum),"PERSON", oneName[0])
                

        # Shortcut Name
        # M. Pekey
        # Mert H. Pekey
        for oneName in re.findall(r'(\w+)\s([A-ZÇĞİÖŞÜ]\.\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]+)[.\s\',][^A-ZÇĞİÖŞÜ]',line):
            if oneName[0] not in PERSON:
                if oneName[1] not in ORGANIZATIONS:
                    print("Line {}:".format(lineNum),"PERSON", oneName[1])
                    

        for oneName in re.findall(r'(([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s[A-ZÇĞİÖŞÜ]\.\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]+)[.\s\',][^A-ZÇĞİÖŞÜ]',line):
            if oneName[1] in PERSON:
                print("Line {}:".format(lineNum),"PERSON", oneName[0])
                


        if ('Av.' in line) or ('Dr.' in line) or ('Mr.' in line) or ('Ms.' in line) or ('Mrs.' in line) or ('Miss' in line):
            
            for pers in re.findall(r'(Dr.\s(([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+\s?)+)[.\s\',][^A-ZÇĞİÖŞÜ])',line):
                if pers[1].split(' ')[0] not in PERSON: # To be safe not to print the  twice with the previous rule
                    myname= pers[1]
                    if myname[-1] == ' ':
                        print("Line {}:".format(lineNum),'PERSON', myname[:-1])
                        
                    else:
                        print("Line {}:".format(lineNum),'PERSON',myname)
                        
            for pers in re.findall(r'(Av.\s(([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+\s?)+)[.\s\',][^A-ZÇĞİÖŞÜ])',line):
                if pers[1].split(' ')[0] not in PERSON: # To be safe not to print the  twice with the previous rule
                    myname= pers[1]
                    if myname[-1] == ' ':
                        print("Line {}:".format(lineNum),'PERSON', myname[:-1])
                        
                    else:
                        print("Line {}:".format(lineNum),'PERSON',myname)
                        

            for pers in re.findall(r'((?:(?:Mr.)|(?:Ms.)|(?:Mrs.)|(?:Miss))\s(([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+\s?)+)[.\s\',][^A-ZÇĞİÖŞÜ])',line):
                if pers[1].split(' ')[0] not in PERSON: # To be safe not to print the organization twice with the previous rule
                    myname= pers[1]
                    if myname[-1] == ' ':
                        print("Line {}:".format(lineNum),'PERSON', myname[:-1])
                        
                    else:
                        print("Line {}:".format(lineNum),'PERSON',myname)
                        


        # İsvec Dışişleri Bakanı
        if ('Cumhurbaşkanı' in line) or ('Başbakan' in line) or ('Dışişleri Bakanı' in line) or ('İçişleri Bakanı' in line) or ('Başkanı' in line):
            for i in re.findall(r'((([A-ZÇĞİÖŞÜ][a-zçğıöşü]+\s)+)(?:(?:Cumhurbaşkanı)|(?:Başbakan)|(?:Dışişleri Bakanı)|(?:İçişleri Bakanı)|(?:Başkanı))\w*)[\'\s.,]',line):
                if i[1][0:-1] in LOCATIONS:
                    print("Line {}:".format(lineNum),"PERSON",i[0])
                    
            for i in re.findall(r'(([A-ZÇĞİÖŞÜ.]{2,})\s(?:(?:Cumhurbaşkanı)|(?:Başbakan)|(?:Dışişleri Bakanı)|(?:İçişleri Bakanı)|(?:Başkanı))\w*)[\'\s.,]',line):
                if i[1] in LOCATIONS:
                    print("Line {}:".format(lineNum),"PERSON",i[0])
                    

                
   
        ##########################################
        #Location

        # One Word Location in Lexicon
        for oneLoc in re.findall(r'([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)[.\s\',][^A-ZÇĞİÖŞÜ]',line):
            if oneLoc in LOCATIONS:
                if oneLoc not in PERSON:
                    if oneLoc not in DATES:
                        print("Line {}:".format(lineNum),"LOCATION", oneLoc)
                        


        # Two Word Location in Lexicon
        for oneLoc in re.findall(r'([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+\s[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)[.\s\',][^A-ZÇĞİÖŞÜ]',line):
            if oneLoc in LOCATIONS:
                print("Line {}:".format(lineNum),"LOCATION", oneLoc)
                

        #Three Word Location - United Arab Emirates - Amerika Birleşik Devletleri
        for oneLoc in re.findall(r'([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+\s[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+\s[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)[.\s\',][^A-ZÇĞİÖŞÜ]',line):
            if oneLoc in LOCATIONS:
                print("Line {}:".format(lineNum),"LOCATION", oneLoc)
                

        # Special Cases - 've' in the Location name
        for oneLoc in re.findall(r'((?:[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+\s?)+ve\s[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+\s?)[.\s\'][^A-ZÇĞİÖŞÜ]',line):
            if oneLoc in LOCATIONS:
                print("Line {}:".format(lineNum),"LOCATION", oneLoc)
                

        # Special Case - Abbreviation - ABD, BAE or A.B.D, B.A.E
        for oneLoc in re.findall(r'([A-ZÇĞİÖŞÜ.]{2,})',line):
            if oneLoc in LOCATIONS:
                print("Line {}:".format(lineNum),"LOCATION", oneLoc)
                

        
        if ('Köy' in line) or ('Dağ' in line) or ('Mahalle' in line) or ('Sokak' in line) or ('Cadde' in line) or ('Apartman' in line) or ('İş Merkezi' in line) or ('Büro' in line) or ('Köprü' in line) or ('Saray' in line) or ('Mezarlı' in line) or ('Köşk' in line) or ('Şelale' in line) or ('Antik Kent' in line) or ('Antik Şeh' in line) or ('Kale' in line) or ('Kule' in line) or ('Adası' in line) or ('Plaj' in line) or ('Manastır' in line) or ('Türbe' in line) or ('Yayla' in line) or ('Irmağı' in line) or ('Dere' in line) or ('Müze' in line) or ('Cezaevi' in line) or ('Park' in line) or ('Camii' in line) or ('Cami' in line) or ('Tapına' in line) or ('Kilise' in line) or ('Mescid' in line) or ('Anıt' in line) or ('Katedral' in line) or ('Heykel' in line) or ('Çayı' in line) or ('Nehri' in line) or ('Göl' in line) or ('İmparatorlu' in line) or ('Patrikhane' in line) or ('Çay Bahçe' in line):
            for i in re.findall(r'(((?:[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+\s)+)(?:(?:Köyü)|(?:Dağı)|(?:Mahalle)|(?:Cadde)|(?:Apartman)|(?:İş Merkezi)|(?:Büro)|(?:Köprü)|(?:Sarayı)|(?:Köşk)|(?:Şelalesi)|(?:Antik Kent)|(?:Kalesi)|(?:Kulesi)|(?:Adası)|(?:Plaj)|(?:Manastır)|(?:Türbe)|(?:Yayla)|(?:Irmağı)|(?:Deresi)|(?:Müze)|(?:Cezaevi)|(?:Park)|(?:Camii)|(?:Cami)|(?:Antik Şehri)|(?:Tapına)|(?:Kilise)|(?:Mescid)|(?:Anıt)|(?:Katedral)|(?:Heykel)|(?:Çayı)|(?:Nehri)|(?:Gölü)|(?:Göller)|(?:İmparatorlu)|(?:Patrikhane)|(?:Çay Bahçe))\w*)[\'\s.,]',line):
                
                if i[0] not in LOCATIONS:
                    print("Line {}:".format(lineNum),"LOCATION",i[0])
                    
            for i in re.findall(r'(((?:[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+\s)+)Mezarlı[ğk]\w*)[\'\s.,]',line):
                
                if i[0] not in LOCATIONS:
                    print("Line {}:".format(lineNum),"LOCATION",i[0])
                    
            for i in re.findall(r'(((?:[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+\s)+)Soka[kğ]\w*)[\'\s.,]',line):
                
                if i[0] not in LOCATIONS:
                    print("Line {}:".format(lineNum),"LOCATION",i[0])
                    
            

        #########################
        #Date and Time

        # 2000 yilinda
        if 'yıl' in line:
            for date in re.findall(r'\d{4}(?=\s+yıl\w+)',line):
                print("Line {}:".format(lineNum),'TIME', date)
                
            

        # 01/01/2000 - 01-01-2000 - 01.01.2000 01\01\2000
        for date in re.findall(r'\d{2}[-/.\\]\d{2}[-/.\\]\d{4}',line):
            print("Line {}:".format(lineNum),'TIME', date)
            


        # 10 Ocak tarihi
        for date in re.findall(r'((\d{1,2})\s([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+))[.\s\',][^0-9]',line):
            if date[2] in DATES:
                if int(date[1]) > 0 and int(date[1]) < 32:
                    print("Line {}:".format(lineNum),'TIME', date[0])
                    

         # 2005 Ocak tarihi
        for date in re.findall(r'((\d{4})\s([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+))[.\s\',][^0-9]',line):
            if date[2] in DATES:
                if int(date[1]) > 1700 and int(date[1]) < 2050:
                    print("Line {}:".format(lineNum),'TIME', date[0])
                    


        # 5 Ekim 2000
        for date in re.findall(r'(\d{1,2}\s([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s[0-9]{4})',line):
            if date[1] in DATES:
                print("Line {}:".format(lineNum),'TIME', date[0])
                

        # Month names can be written in lowercase with 'ay' word
        if 'ay' in line:
            for date in re.findall(r'([A-Za-zçğıöşüÇĞİÖŞÜ][a-zçğıöşü]+)(?=\s+ay\w+)',line):
                if date[1] in DATES:
                    print("Line {}:".format(lineNum),'TIME', date[0])
                    

        
        # 2000'deki - But be careful for the case 5 Kasim 2000'deki
        for date in re.findall(r'(([\w.]+)?\s?(\d{4})[\']\w+)',line):
            if date[1] not in DATES:
                print("Line {}:".format(lineNum),'TIME', date[2])
                

        # Ocak 2020'de
        for date in re.findall(r'[^\d]\s(([A-ZÇĞİÖŞÜ][a-zçğıöşüA-ZÇĞİÖŞÜ]+)\s[0-9]{4})',line):
            if date[1] in DATES:
                print("Line {}:".format(lineNum),'TIME', date[0])
                

        # Date Ranges such as Ocak - Mart arasi
        for date in re.findall(r'(([A-Za-zÇĞİÖŞÜçğıöşü][a-zçğıöşüA-ZÇĞİÖŞÜ]+)\s?-\s?([A-ZÇĞİÖŞÜa-zçğıöşü][a-zçğıöşüA-ZÇĞİÖŞÜ]+))',line):
            if (date[1] in DATES) and (date[2] in DATES):
                print("Line {}:".format(lineNum),'TIME', date[0])
                

        # Gün - Salı günü or pazartesi günü
        if 'gün' in line:
            for date in re.findall(r'([A-Za-zçğıöşüÇĞİÖŞÜ]+)\sgün\w+',line):
                if date in DATES:
                    print("Line {}:".format(lineNum),'TIME', date)
                    

        # Dakika Saniye gibi zaman terimleri
        if ('Dk' in line) or ('Dakika' in line) or ('Saniye' in line) or ('Salise' in line) or ('dakika' in line) or ('saniye' in line) or ('salise' in line) or ('dk' in line) or ('sn' in line):
            for date in re.findall(r'([^0-9]((\d{1,2})\s[Dd]akika\w*)[\s\',.])',line):
                if int(date[2]) < 60 and int(date[2]) >= 0:
                    print("Line {}:".format(lineNum),'TIME', date[1])
                    
            for date in re.findall(r'([^0-9]((\d{1,2})\s[Dd]k\w*)[\s\',.])',line):
                if int(date[2]) < 60 and int(date[2]) >= 0:
                    print("Line {}:".format(lineNum),'TIME', date[1])
                    
            for date in re.findall(r'([^0-9]((\d{1,2})\s[Ss]aniye\w*)[\s\',.])',line):
                if int(date[2]) < 60 and int(date[2]) >= 0:
                    print("Line {}:".format(lineNum),'TIME', date[1])
                    
            for date in re.findall(r'([^0-9]((\d{1,2})\s[Ss]alise\w*)[\s\',.])',line):
                if int(date[2]) < 100 and int(date[2]) >= 0:
                    print("Line {}:".format(lineNum),'TIME', date[1])
                    
            for date in re.findall(r'([^0-9]((\d{1,2})\s[Ss]n\w*)[\s\',.])',line):
                if int(date[2]) < 60 and int(date[2]) >= 0:
                    print("Line {}:".format(lineNum),'TIME', date[1])
                    

                
        # Time
        # For 24 Hours Times
        # 13:30, 13.30
        for date in re.findall(r'((\d{2})[:.](\d{2}))',line):
            if int(date[1]) < 24 and int(date[1]) >= 0:
                if int(date[2]) >= 0 and int(date[2]) < 60:
                    print("Line {}:".format(lineNum),'TIME', date[0])
                    

        #For AM - PM
        # 00:20 AM, 1:20 PM
        for date in re.findall(r'((\d{1,2})[:.](\d{2})(\s[AP][M]))[\s.\',]',line):
            if int(date[1]) <= 12 and int(date[1]) >= 0:
                if int(date[2]) >= 0 and int(date[2]) < 60:
                    print("Line {}:".format(lineNum),'TIME', date[0])
                    

        for date in re.findall(r'[\s]((\d{1,2})(\s[AP][M]))[\s.\',]',line):
            if int(date[1]) <= 12 and int(date[1]) >= 0:
                print("Line {}:".format(lineNum),'TIME', date[0])
                

        # Saat 1'de
        for date in re.findall(r'(([Ss]aat\w* (\d{1,2}))[\s\',])',line):
            if int(date[2]) < 24 and int(date[2]) >= 0:
                print("Line {}:".format(lineNum),'TIME', date[1])
                

        ######################################
        #Organization

        # First the usual two cases

        # One Word Organizations
        for org in re.findall(r'([A-ZÇĞİÖŞÜ][a-zçğıöşü]+)[.\s\',][^A-ZÇĞİÖŞÜ]',line):
            if org not in PERSON and org not in LOCATIONS:
                if org in ORGANIZATIONS:
                    print("Line {}:".format(lineNum),'ORGANIZATION', org)
                    
        
        for org in re.findall(r'([A-ZÇĞİÖŞÜ]+)[.\s\',][^A-ZÇĞİÖŞÜ]',line):
            if org not in PERSON and org not in LOCATIONS:
                if org in ORGANIZATIONS:
                    print("Line {}:".format(lineNum),'ORGANIZATION', org)
                    

        # Two Word Organizations
        for org in re.findall(r'([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*)[\'\s.,][^A-ZÇĞİÖŞÜ]',line):
            if org not in PERSON and org not in LOCATIONS:
                if org in ORGANIZATIONS:
                    print("Line {}:".format(lineNum),'ORGANIZATION', org)
                    
        # Thr Word Organizations
        for org in re.findall(r'([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]*)[\'\s.,][^A-ZÇĞİÖŞÜ]',line):
            if org not in PERSON and org not in LOCATIONS:
                if org in ORGANIZATIONS:
                    print("Line {}:".format(lineNum),'ORGANIZATION', org)
                    
        # Shortcut Organization
        # F. Bahçe
        # 
        for oneName in re.findall(r'(\w+)\s([A-ZÇĞİÖŞÜ]\.\s[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)[.\s\',][^A-ZÇĞİÖŞÜ]',line):
            if oneName[1] in ORGANIZATIONS:
                print("Line {}:".format(lineNum),"ORGANIZATION", oneName[1])
                

        # Special case - 've' or '-' or 'of' can be in Organization Name
        for org in re.findall(r'((?:[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+\s?)+(?:(?:ve)|(?:-)|(?:of))\s?(?:[A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+\s?)+)[.\s\'][^A-ZÇĞİÖŞÜ]',line):
            if org in ORGANIZATIONS:
                print("Line {}:".format(lineNum),"ORGANIZATION", org)
                


        # Üniversitesi/Holding/Vakfı/Federasyonu/Enstitüsü/Kurumu/Bankası/
        if ('Üniversite' in line) or ('Holding' in line) or ('Vakfı' in line) or ('Federasyonu' in line) or ('Enstitüsü' in line) or ('Kurumu' in line) or ('Bankası' in line) or ('Gazetesi' in line) or ('gazetesi' in line) or ('dergisi' in line) or ('Dergisi' in line) or ('Müdürlüğü' in line) or ('Derneği' in line) or ('Kulübü' in line) or ('Yayınevi' in line):
            
            for org in re.findall(r'((([A-ZÇĞİÖŞÜ0-9][A-ZÇĞİÖŞÜa-zçğıöşü0-9]+\s)+(?:(?:Üniversitesi)|(?:Holding)|(?:Gazetesi)|(?:Vakfı)|(?:Federasyonu)|(?:Enstitüsü)|(?:Kurumu)|(?:Bankası)|(?:gazetesi)|(?:Müdürlüğü)|(?:Derneği)|(?:Kulübü)|(?:Yayınevi)))[\'\w\s,.]+)',line):
                if org[1] not in ORGANIZATIONS: # To be safe not to print the organization twice with the previous rule
                    print("Line {}:".format(lineNum),'ORGANIZATION', org[1])
                    
            

        # TV Channel
        if ('TV' in line) or ('HD' in line):
                
            for org in re.findall(r'(((([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s)+(?:(?:TV)|(?:HD)))[\'\w\s.]+)',line):
                if org[1] not in ORGANIZATIONS: # To be safe not to print the organization twice with the previous rule
                    print("Line {}:".format(lineNum),'ORGANIZATION', org[1])
                    


        # Futbol Takımı
        if ('SK' in line) or ('JK' in line) or ('FC' in line) or ('spor' in line):
                
            for org in re.findall(r'(((([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s)+(?:(?:SK)|(?:FC)|(?:JK)))[\'\s.]+)',line):
                if org[1] not in ORGANIZATIONS: # To be safe not to print the organization twice with the previous rule
                    print("Line {}:".format(lineNum),'ORGANIZATION', org[1])
                    
                
            for org in re.findall(r'(((([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s?)+[^\s][Ss][Pp][Oo][Rr])[\'\w\s.]+)',line):
                if org[1] not in ORGANIZATIONS: # To be safe not to print the organization twice with the previous rule
                    print("Line {}:".format(lineNum),'ORGANIZATION', org[1])
                    

        # Shortcut Organization Names
        # THY
        for org in re.findall(r'([A-ZÇĞİÖŞÜ.]{2,})',line):
            if org not in LOCATIONS:
                if org in ORGANIZATIONS:
                    print("Line {}:".format(lineNum),"ORGANIZATION", org)
                    

        # L.T.D. Ş.T.İ., A.Ş., L.T.D
        if ('LTD' in line) or ('L.T.D.' in line) or ('A.Ş.' in line) or ('AŞ' in line):
            for org in re.findall(r'((([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s+L\.T\.D\.\sŞ\.T\.İ\.)[\',\s]+)',line):
                print("Line {}:".format(lineNum),'ORGANIZATION', org[1])
                
            for org in re.findall(r'((([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s+LTD\sŞTİ)[\',\s]+)',line):
                print("Line {}:".format(lineNum),'ORGANIZATION', org[1])
                
            for org in re.findall(r'((([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s+A\.Ş\.)[\',\s]+)',line):
                print("Line {}:".format(lineNum),'ORGANIZATION', org[1])
                
            for org in re.findall(r'((([A-ZÇĞİÖŞÜ][A-ZÇĞİÖŞÜa-zçğıöşü]+)\s+AŞ)[\',\s]+)',line):
                print("Line {}:".format(lineNum),'ORGANIZATION', org[1])
                


        lineNum+=1


