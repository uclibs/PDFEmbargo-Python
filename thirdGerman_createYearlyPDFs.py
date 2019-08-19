# A script to create parse one big Third German Protestant Church Record
# PDF into smaller PDFs based on year, for copyright purposes. 

import pdfrw

page_hash = { 2020: 252,
              2021: 254, 
              2022: 257,
              2023: 258,
              2024: 259,
              2027: 260,
              2029: 261,
              2030: 262,
              2034: 263,
              2036: 264,
              2039: 266,
              2041: 267,
              2042: 268,
              2043: 269,
              2044: 272,
              2045: 273,
              2046: 274,
              2047: 276,
              2048: 278,
              2049: 280,
              2050: 282,
              2051: 283,
              2052: 284,
              2053: 285,
              2054: 287,
              2055: 288,
              2056: 289,
              2057: 290,
              2058: 291,
              2059: 292,
              2060: 293,
              2062: 295,
              2063: 296,
              2064: 297,
              2065: 298,
              2066: 299,
              2067: 300,
              2068: 301,
              2070: 302,
              2071: 303,
              2072: 305,
              2074: 306,
              2076: 307,
              2077: 308,
              2078: 309,
              2080: 310,
              2081: 311,
            }


entirePDF = pdfrw.PdfReader('thirdGermanProtestant_v08_2082_version.pdf')

for year in page_hash.keys():

    output = pdfrw.PdfWriter()
    for i in range (1, page_hash.get(year)):
    	output.addPage(entirePDF.pages[i])

    output.write('thirdGermanProtestant_v08_'+str(year)+'_version.pdf')

