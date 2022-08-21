import pandas as pd
import time

if __name__ == '__main__':
    startTime = time.time()
    data = pd.read_excel('Liste.xlsx')
    allAddresses = data['TAM ADRES'].tolist()
    allSurnames = data['SOYAD'].tolist()
    totalEntries = len(allAddresses)
    surnameCounts = [0] * totalEntries
    surnamesInThisHouse = {}  # key: adres, value: adresteki soyadlar listesi
    addressesWithNSurnames = {}  # key: surnameCount, value: list of addresses with this surnameCount
    numberPeopleInThisHouse = {}  # key: adres, value: adresteki kişi sayısı
    addressesWithNPeople = {}  # key: peopleCount, value: list of addresses with this peopleCount
    maxSurname = 0
    addressWithMaxSurname = ""
    maxPeople = 0
    addressWithMaxPeople = ""
    with open("out.txt", "w") as file:
        file.write("")
    for i in range(totalEntries):
        if allAddresses[i] not in surnamesInThisHouse.keys():
            surnamesInThisHouse[allAddresses[i]] = []
            surnamesInThisHouse[allAddresses[i]].append(allSurnames[i])
        else:
            if allSurnames[i] not in surnamesInThisHouse[allAddresses[i]]:
                surnamesInThisHouse[allAddresses[i]].append(allSurnames[i])

        if allAddresses[i] not in numberPeopleInThisHouse.keys():
            numberPeopleInThisHouse[allAddresses[i]] = 1
        else:
            numberPeopleInThisHouse[allAddresses[i]] += 1

    for i in surnamesInThisHouse:
        tempMaxSurname = len(surnamesInThisHouse[i])
        if tempMaxSurname > maxSurname:
            maxSurname = tempMaxSurname
            addressWithMaxSurname = i
        if tempMaxSurname not in addressesWithNSurnames.keys():
            addressesWithNSurnames[tempMaxSurname] = []
            addressesWithNSurnames[tempMaxSurname].append(i)
        else:
            addressesWithNSurnames[tempMaxSurname].append(i)

    for i in numberPeopleInThisHouse:
        tempMaxPeople = numberPeopleInThisHouse[i]
        if tempMaxPeople > maxPeople:
            maxPeople = tempMaxPeople
            addressWithMaxPeople = i
        if tempMaxPeople not in addressesWithNPeople.keys():
            addressesWithNPeople[tempMaxPeople] = []
            addressesWithNPeople[tempMaxPeople].append(i)
        else:
            addressesWithNPeople[tempMaxPeople].append(i)

    with open("out.txt", "a") as file:
        file.write(f"Bir evdeki maksimum soyad sayısı: {maxSurname}")
        file.write("\n")
        file.write(f"Maksimum soyada sahip ev: {addressWithMaxSurname}")
        file.write("\n")
        file.write(f"Bir evdeki maksimum kişi sayısı: {maxPeople}")
        file.write("\n")
        file.write(f"Maksimum kişinin kaldığı ev: {addressWithMaxPeople}")
        file.write("\n")

    with open("out.txt", "a") as file:
        file.write("\n")
        file.write("PEOPLE")
        file.write("\n")
    for i in reversed(range(maxPeople + 1)):
        if i in addressesWithNPeople.keys():
            if i > 1:
                with open("out.txt", "a") as file:
                    file.write("***********************************************************************************")
                    file.write("\n")
                    file.write(f"İçinde {i} kişinin kaldığı toplam {len(addressesWithNPeople[i])} adres var.")
                    file.write("\n")
                    file.write(f"İçinde {i} kişinin kaldığı adresler:\n")
                    for j in addressesWithNPeople[i]:
                        file.write(j)
                        file.write(f"  ---  Bu adreste {len(surnamesInThisHouse[j])} soyad var.")
                        file.write("\n")
                    file.write("\n")
                    file.write("***********************************************************************************")
                    file.write("\n")

    """
    with open("out.txt","a") as file:
        file.write("\n")
        file.write("SURNAMES")
        file.write("\n")
    for i in reversed(range(maxSurname+1)):
        if i in addressesWithNSurnames.keys():
            if i > 1:
                with open("out.txt", "a") as file:
                    file.write("***********************************************************************************")
                    file.write("\n")
                    file.write(f"There are {len(addressesWithNSurnames[i])} addresses with {i} surnames.")
                    file.write("\n")
                    file.write(f"Addresses with {i} surnames are \n")
                    for j in addressesWithNSurnames[i]:
                        file.write(j)
                        file.write(f"  ---  There are {numberPeopleInThisHouse[j]} people here")
                        file.write("\n")
                    file.write("\n")
                    file.write("***********************************************************************************")
                    file.write("\n")
    """

    endTime = time.time()
    with open("out.txt", "a") as file:
        totalTime = endTime - startTime
        file.write(f"Hesaplama süresi: {totalTime:.2f} saniye.")
        file.write("\n")
    print(f"Total time taken: {endTime - startTime}")