# Lexicon and Rule-based Named Entity Recognition for Turkish Language

* **Author:** Mert Pekey
* **Contact:** mpekey@gmail.com / mpekey@sabanciuniv.edu

## Description

The aim of the project is developing a lexicon and rule-based Named Entity Recognition for Turkish language.

## Usage

```bash
python3 ner.py input_file_path > output_file_path
```

## Named Entities for the Project

* PERSON
* LOCATION
* ORGANIZATION
* TIME

## Lexicons

Lexicons used in the development process of the project scraped from web. They are not going to be shared because of the Copyrigth issues.

**Location Lexicon**: It includes Country, City, Continent, Street, River, Mountain, Lake names

**Organization Lexicon**: It includes Turkish and English popular company names

**Person Lexicon**: It includes Turkish and English human names

## Rules

### PERSON

* Name -> 'Mert'
* Name Surname -> 'Mert Pekey'
* Name Name Surname -> 'Mert Hakan Pekey'
* Name SURNAME-> 'Mert PEKEY'
* Name Name SURNAME -> 'Mustafa Kemal ATATÜRK'
* Names contain punctuation -> 'Mathias d'Arras'
* Initial Letter Name Surname -> 'M.Pekey' or 'Mert H. Pekey'
* Av. Dr. Mr. Ms. Mrs. Miss
* Isviçre Dışişleri Bakanı, Başkan, Cumhurbaşkanı

### LOCATION

* Location -> 'Türkiye' or 'New York' or 'Amerika Birleşik Devletleri'
* 've' in Location Name -> 'Trinidad ve Tobago'
* Abbreviation-> 'ABD' or 'A.B.D.'
* Köy, Dağ, Mahalle, Sokak, Cadde, Apartman etc.

### TIME

* 2000 yılında
* 01/01/2000 - 01-01-2000 - 01.01.2000 - 01\01\2000
* 10 Ocak
* 2005 Ocak
* 5 Ekim 2000
* 'Şubat ayı' or 'şubat ayı' 
* 2000'deki
* Ocak 2020'de
* Ocak - Mart arası
* Salı günü or pazartesi günü
* Dakika/dakika/dk/Dk - Saniye/saniye/sn/Sn
* 13:30 or 13.30
* 00:20 AM or 1:20 PM
* Saat 1'de

### ORGANIZATION

* Organization Names
* F. Bahçe
* 've' or '-' or 'of' in Organization Name
* Üniversitesi/Holding/Vakfı/Federasyonu/Enstitüsü/Kurumu/Bankası
* TV Channel
* Football Team
* Abbreviation-> 'THY'
* L.T.D. Ş.T.İ., A.Ş., L.T.D

## Sample Result

Line 1: ORGANIZATION Fenerbahçe
Line 3: ORGANIZATION Fenerbahçe Spor Kulübü
Line 7: TIME Çarşamba
Line 7: TIME 15:00
Line 9: ORGANIZATION Fenerbahçe
Line 11: TIME 00.00
Line 12: PERSON Ali Koç
Line 12: TIME 17 Ocak
Line 12: ORGANIZATION Fenerbahçe
Line 14: LOCATION Londra
Line 14: LOCATION İstanbul
Line 17: PERSON Mesut Özil
Line 17: PERSON Mesut Özil
Line 17: LOCATION Almanya
Line 17: LOCATION Zonguldak
Line 17: LOCATION Devrek
Line 17: LOCATION Almanya
Line 17: TIME 15 Ekim 1988



