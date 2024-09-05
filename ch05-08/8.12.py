genome = input("Enter the genome: ");
genome = genome.upper()

triplet = ["TAG", "TAA", "TGA"]
genes = [999999, 999999, 999999]

c = 0
index = 0
x = -3
while 1:
    for letter in genome:
        if (letter != 'A' and letter != 'C' and letter != 'T' and letter != 'G'):
            print("Inappropriate letters")
            x = -1
            break

    x = genome.find("ATG", x + 3)
    if (x == -1):
        break

    genes[0] = genome.find("TAG", x + 3)
    genes[1] = genome.find("TAA", x + 3)
    genes[2] = genome.find("TGA", x + 3)

    for i in range(0, 3):
        if (genes[i] == -1):
            genes[i] = 999999
            index = min(genes)
    if (index > 999998):
        continue
    inputGenes = genome[x + 3:index]

    if (inputGenes.count("ATG") == 0 and x % 3 == index % 3):

        print(inputGenes + "")

        c = c + 1;
if (c == 0):
    print("No gene is found")