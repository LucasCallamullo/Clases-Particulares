
fd = 'envios25.txt'
fd = 'envios100SC.txt'
# fd = 'envios100HC.txt'
# fd = 'envios500b.txt'



m = open(fd, "rt")





line = m.readline()

# resultado 1...
if "HC" in line:
    control = "Hard Control"
else:
    control = "Soft Control"

# procesar el resto de las lineas...
while True:
    line = m.readline()
    print(line)
    if line == "":
        break