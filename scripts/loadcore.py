import pandas as pd
from core.models import Member
def run():
    data = pd.read_csv('memberdeets.csv')
    columns = [i for i in data][1:]
    
    for i in range(80):
        name=data[columns[0]][i]+' '+data[columns[1]][i]
        position,deptName,desc=data[columns[2]][i],data[columns[3]][i],data[columns[4]][i]
        if position in ["Chairperson","Head"]:
            m = Member(name=name,position=position,deptName=deptName,posnum=1,desc=desc)
        else:
            m = Member(name=name,position=position,deptName=deptName,posnum=2,desc=desc)
        m.save()

