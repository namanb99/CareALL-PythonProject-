#from abc import ABC, abstractclassmethod
import itertools
import statistics
youngRec = {}      #ratings and userid for young ones
oldRec = {}        #ratings and userid for old ones
oldApp = {}        #assigned person to old user
youngApp = {}      #list of people assigned to young one

youngRating = {1, 2, 3, 4, 5}                #ratings from
oldRating = {1, 2, 3, 4, 5}                  # 1 to 5


class User():                               #base-class
    counter = itertools.count(100)

    def __init__(self):
        super(User, self).__init__()
        self.name = ""
        self.phone = ""
        self.userId = next(self.counter)
        self.info = [self.name, self.phone]

    def setInfo(self, name, phone):
        self.name = name
        self.phone = phone

    def getInfo(self):
        return self.info


class UserYoung(User):                      #inherited-class
    def __init__(self):
        super(UserYoung, self).__init__()
        self.ratings = 5

    def setRatings(self, ratings):
        self.ratings = ratings

    def getRatings(self):
        return self.ratings


class UserOld(User):                       #inherited-class
    def __init__(self):
        super(UserOld, self).__init__()
        self.ratings = 2.0

    def setRatings(self, ratings):
        self.ratings = ratings

    def getRatings(self):
        return self.ratings

def setYoungRec(rate, id):
    youngRec.setdefault(rate, [])
    youngRec[rate].append(id)


def setOldRec(rate, id):
    oldRec.setdefault(rate, [])
    oldRec[rate].append(id)

def allocateOld(yid,oid):
    youngApp.setdefault(yid, [])
    if len(youngApp[yid]) == 4:
        return True
    youngApp[yid].append(oid)

def appointYoung(oid,yid):
    oldApp[oid] = yid


y1 = UserYoung()
y2 = UserYoung()
y3 = UserYoung()
y1.setInfo("Naman Bhatia", 123456)
setYoungRec(2.0, y1.userId)
y2.setInfo("Raman Bhatt", 789456)
setYoungRec(3.0, y2.userId)
y3.setInfo("Shekhar Sharma", 456123)
setYoungRec(5.0, y3.userId)

o1 = UserOld()
o2 = UserOld()
o3 = UserOld()
o4 = UserOld()
o1.setInfo("Ram Prakash", 654987)
setOldRec(1.0, o1.userId)
o2.setInfo("Ramesh", 741852)
setOldRec(1.0, o2.userId)
o3.setInfo("Prasad Kumar", 852963)
setOldRec(3.0, o3.userId)
o4.setInfo("Prakash Jha", 745698)
setOldRec(4.0, o4.userId)

temp = True

while(True):
    print("***Welcome***\n1: New User(Young-age)\n2: New User(Old-age)\n3: Old User(Young-age)\n4: Old User(Old-age)\n5: Show current appointments\n6: Exit")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        y = UserYoung()
        name = input(":Enter your name: ")
        phone = input("Enter your phone no: ")
        y.setInfo(name, phone)
        setYoungRec(y.getRatings(), y.userId)
        print("Your user-id is: %d" % y.userId)

    if ch == 2:
        o = UserOld()
        name = input(":Enter your name: ")
        phone = input("Enter your phone no: ")
        o.setInfo(name, phone)
        setOldRec(o.getRatings(), o.userId)
        print("Your user-id is: %d" % o.userId)

    if ch == 3:
        ch1 = int(input("Enter your id: "))
        print("Hire the person from below list by entering the corresponding user-id")
        print(oldRec)
        ch2 = int(input("Enter the id you want to choose: "))
        if(allocateOld(ch1, ch2)):
            print("Your limit is full")
            continue
        appointYoung(ch2, ch1)

    if ch == 4:
        ch1 = int(input("Enter your id: "))
        print("Hire the person from below list by entering the corresponding user-id")
        print(youngRec)
        ch2 = int(input("Enter the id you want to choose: "))
        if (allocateOld(ch2, ch1)):
            print("Your limit is full")
            continue
        appointYoung(ch1, ch2)

    if ch == 5:
        print("Here are is the list of all the young ones taking care of the old people\nKey->Young-user's id and Value->Old-user's id")
        print(youngApp)
        print("Here are all the old ones taken care by the young ones\nKey->Old-user's id and Value->Young-user's id")
        print(oldApp)

    if ch == 6:
        exit()

