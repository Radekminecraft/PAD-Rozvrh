from Class import Class
from unidecode import unidecode
def getDayByNumber(number):
    days = ["pondeli", "utery", "streda", "ctvrtek", "patek"]
    return days[number]
def getClasses(file):
    days = {}
    lines = file.readlines()
    for line in range(len(lines)):
        classes = lines[line].strip().split(";")
        dayClasses = []
        for clazz in classes:
            clazzSplit = clazz.split("-")
            name = clazzSplit[0]
            time = clazzSplit[1].split("|")
            dayClasses.append(Class(time[0], time[1], name))
        days[getDayByNumber(line)] = dayClasses
    return days
def getClassByDate(day, hour, minute, classes):
    #Day, time format D/HH/MM
    if hour > 23 or hour < 0 or minute > 59 or minute < 0:
        return "Zadal jsi neplatný čas"
    time = int(str(hour) + str(minute))
    clazzez = classes.get(day)
    if(clazzez == None):
        return "Zadej den mezi pondělím a pátkem!"
    for clazz in clazzez:
        if time >= int(clazz.timeStart) and time <= int(clazz.timeEnd):
            return clazz
    if time < int(clazzez[0].timeStart) or time > int(clazzez[len(clazzez)-1].timeEnd):
        return "Není škola"
    return "Přestávka"
rozvrh = open("rozvrh.txt", "r")
classes = getClasses(rozvrh)
day = unidecode(input("Zadej den (pondělí - pátek): ")).lower()
time = input("Zadej čas (HH:MM): ")
timeSplit = time.split(":")
clazz = getClassByDate(day, timeSplit[0], timeSplit[1], classes)
if isinstance(clazz, Class):
    print(clazz.name)
else:
    print(clazz)