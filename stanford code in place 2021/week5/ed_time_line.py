import json
from dateutil import parser
from pytz import timezone
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    ed_data=open_file()
    hours=get_hours(ed_data)
    print(hours)
    plot(hours)
    
        
def open_file():
    ed_data=json.load(open("ed.json"))
    return ed_data

        
def get_hours(ed_data):
    hour_dict={}
    for line in ed_data:
        time=line['created_at']
        hours=hour(time)
        if hours not in hour_dict:
            hour_dict[hours]=1
        else:
            hour_dict[hours]+=1
    return hour_dict

def hour(time):
    time=parser.parse(time)
    time=time.astimezone(timezone("US/PACIFIC"))
    return time.hour
        
    
def plot(hours):
    data={'x':list(hours.keys()),'y':list(hours.values())}
    print(data)
    sns.barplot(x='x',y='y',data=data)
    plt.savefig('plot.png')

    """a png file be stored in the current working directory"""

if __name__=="__main__":
    main()
