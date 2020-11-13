Name = input("Name \t:")
IDPUBGM = int(input("ID PUBGM \t:"))

IDPemain = ("%s-%s" % (IDPUBGM, Name))

print("IDPemain :",IDPemain)



"""
from datetime import datetime



Name = input("Name \t")
IDPUBGM = int(input("ID PUBGM \t:"))

time = datetime.now()

IDPemain = ("%s%02d%2d%03d-%s" % (time.year, time.month, time.day, IDPUBGM, Name[0]))

print("IDPemain :",IDPemain)
"""