'''
    1) Total sales data graph
    2) Time interval for delivery
    3) Individual users data analysis
    4) Category wise sells data graph 
'''


import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
import io
from os.path import dirname, join


def sells_graph(dataFrame):
    counter = {}

    dataList = list(dataFrame.iloc[1:, 6])

    for i in dataList:
        if i in counter.keys():
            counter[i] += 1
        else:
            counter[i] = 1

    list2 =[]
    for i in counter.keys():
        if counter[i] < 30:
            list2.append(i)

    for i in list2:
        del counter[i]


    categoryFrequency = list(counter.values())
    categoryName = list(counter.keys())

    plt.pie(categoryFrequency,labels=categoryName, autopct='%2.1f%%')
    plt.show()






def deliveryTime(dataFrame):
    differenceInDay = []
    orderDay = []
    dispatchedDay = []

    orderDate = list(dataFrame.iloc[1:, 0])
    orderDate = pd.to_datetime(orderDate)

    dispatchedDate = list(dataFrame.iloc[1:, 3])
    dispatchedDate = pd.to_datetime(dispatchedDate)


    for i in orderDate:
        orderDay.append(datetime.datetime.date(i).month)

    for i in dispatchedDate:
        dispatchedDay.append(datetime.datetime.date(i).month)


    for i in range(len(orderDay)):
        val = dispatchedDay[i] - orderDay[i]
        differenceInDay.append(abs(val))

    print(differenceInDay)



def categoryData(dataFrame):

    HE = {'Goldline': 0, 'Soft': 0}
    SHE = {'Heera': 0, 'HR': 0, 'Velevet': 0, 'Memory': 0, 'Pure': 0}
    ME = {'FM': 0, 'Eco': 0, 'Bouncer': 0}
    LE = {'Silver': 0, 'Crystal': 0}
    list1 = []

    dataList = list(dataFrame.iloc[1:, 6])

    for i in range(len(dataList)):
        var = dataList[i].split()[0]
        list1.append(var)

    for i in list1:
        if i == "Goldline":
            HE['Goldline'] += 1
        elif i == 'Soft':
            HE['Soft'] += 1
        else:
            continue
    print(HE)

    for i in list1:
        if i == 'Heera':
            SHE['Heera'] += 1
        elif i == 'HR':
            SHE['HR'] += 1
        elif i == 'Velevet':
            SHE['Velevet'] += 1
        elif i == 'Memory':
            SHE['Memory'] += 1
        elif i == 'Pure':
            SHE['Pure'] += 1
        else:
            continue

    print(SHE)

    for i in list1:
        if i == 'FM':
            ME['FM'] += 1
        elif i == 'Eco':
            ME['Eco'] += 1
        elif i == 'Bouncer':
            ME['Bouncer'] += 1
        else:
            continue

    print(ME)

    for i in list1:
        if i == 'Silver':
            LE['Silver'] += 1
        elif i == 'Crystal':
            LE['Crystal'] += 1
        else:
            continue

    print(LE)


    plt.pie(HE.values(),labels=['Goldline','Soft'],autopct='%2.2f%%')
    plt.title("High End Category")
    plt.show()

    plt.pie(SHE.values(),labels=['Heera', 'HR', 'Velevet', 'Memory', 'Pure'],autopct='%2.2f%%')
    plt.title("Super High End Category")
    plt.show()

    plt.pie(ME.values(),labels=['FM', 'Eco', 'Bouncer'],autopct='%2.2f%%')
    plt.title("Medium End Category")
    plt.show()

    plt.pie(LE.values(),labels=['Silver', 'Crystal'],autopct='%2.2f%%')
    plt.title("Lower End Category")
    plt.show()


def indicidulUserGraph(user):
    
    filename = join(dirname(__file__), 'DailyDispatch.xls')
    dataFrame = pd.read_excel(filename)
    dataFrame = dataFrame.dropna(how='all')
    
    dict1 = {}
    quantity = []
    variety = []

    data = dataFrame.iloc[1:,[1,4,6]]
    data = pd.DataFrame(data)
    data.columns = ["Quantity","Name","Variety"]

    for i in range(len(data)):
        if data.iloc[i]['Name']== user:
            variety.append(data.iloc[i]['Variety'])
            quantity.append(abs(data.iloc[i]['Quantity']))

    for i in range(len(variety)):
        if variety[i] in  dict1.keys():
            dict1[variety[i]]  += quantity[i]
        else:
            dict1[variety[i]] = quantity[i]

    l1 = list(dict1.values())
    l2 = list(dict1.keys())
    plt.pie(l1,labels=l2,autopct="%2.1f%%")
    bio = io.BytesIO()
    plt.savefig(bio, format="png")
    b = bio.getvalue()
    return b
    
    
    #return plt.show()


# if __name__ == '__main__':
#     dataFrame = pd.read_excel('DailyDispatch.xlsx')
#     dataFrame = dataFrame.dropna(how='all')
    

#     #sells_graph(dataFrame)
#     #categoryData(dataFrame)
     # indicidulUserGraph()
#     #deliveryTime(dataFrame)