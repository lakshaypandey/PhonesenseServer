from datetime import datetime

#Each get function takes List of lines as argument 
#Each returns list of dictionaries as result


def get_MACs():

#Returns in a list of lists in the sequence AC,GH,BH,LC,LB
    
    fout = open("AP MAC.csv",'r')
    data = fout.readlines()
    fout.close()
    AC_List=[]
    GH_List=[]
    BH_List=[]
    LC_List=[]
    LB_List=[]
    val=[]
    for i in data:
        i=i.rstrip()
        val= i.rsplit(",")
        check=val[0][0:2]
        if (check=='AC'):
            AC_List.append(val[1])
        elif(check=='GH'):
            GH_List.append(val[1])
        elif(check=='BH'):
            BH_List.append(val[1])
        elif(check=='LC'):
            LC_List.append(val[1])
        elif(check=='LB'):
            LB_List.append(val[1])
    return AC_List,GH_List,BH_List,LC_List,LB_List




def get_wifi(a):

#input is a list of lines
#output is list of dicts keys are time,bssid,ssid

    temp={}
    final_result=[]
    val=[]
    for i in a:
        if( len(i) == 0 ): continue
        temp={}
        i=i.rstrip()
        val= i.rsplit(",")
        temp['Timestamp'] = datetime.fromtimestamp(int(val[0])/1000)
        temp['BSSID'] = val[1]
        temp['SSID'] = val[2]
        final_result.append(temp)
    return final_result


def get_battery(a):

#level,scale,chargePlug,batteryPct,timestamp format we get
# return a list of dicts, jeys level,scale,chargeplug,batterypct,time

    temp={}
    final_result=[]
    val=[]
    for i in a:
        if( len(i) == 0 ): continue
        temp={}
        i=i.rstrip()
        val= i.rsplit(",")
        temp['Level'] = int(val[0])
        temp['Scale'] = int(val[1])
        temp['ChargingStatus'] = int(val[2])
        temp['Batterypct'] = float(val[3])
        temp['Timestamp'] = datetime.fromtimestamp(int(val[4])/1000)
        final_result.append(temp)
    return final_result



def get_bluetooth(a):

#input list of lines of the sequence name,address,time
# return a list of dicts, jeys level,scale,chargeplug,batterypct,time

    temp={}
    final_result=[]
    val=[]
    for i in a:
        if( len(i) == 0 ): continue
        temp={}
        i=i.rstrip()
        val= i.rsplit(",")
        temp['SSID'] = val[0]
        temp['BSSID'] = val[1]
        temp['Timestamp'] = datetime.fromtimestamp(int(val[2])/1000)

        final_result.append(temp)
    return final_result



def get_gsm(a):

#input list of lines of the mcc,mnc,cellid,lac,networktype,networkstatus,{ids},rssi,timestamp
# return a list of dicts, keys level,scale,chargeplug,batterypct,time

    temp={}
    final_result=[]
    val=[]
    for i in a:
        if( len(i) == 0 ): continue
        temp={}
        i=i.rstrip()
        val= i.rsplit(",")
        temp['MCC'] = val[0]
        temp['MNC'] = val[1]
        temp['CellID'] = val[2]
        temp['Lac'] = val[3]
        temp['NetworkType'] = val[4]
        temp['NetworkStatus'] = val[5]
        temp['NetworkCellIDs'] = eval(val[6])
        temp['RSSI'] = int(val[7])
        temp['Timestamp'] = datetime.fromtimestamp(int(val[8])/1000)
        final_result.append(temp)
    return final_result

def get_phonestate(a):

#input list of lines of the timestamp,state
# return a list of dicts, keys time,state

    temp={}
    final_result=[]
    val=[]
    for i in a:
        if( len(i) == 0 ): continue
        temp={}
        i=i.rstrip()
        val= i.rsplit(",")
        temp['Timestamp'] = datetime.fromtimestamp(int(val[0])/1000)
        temp['State'] = val[1]
        final_result.append(temp)
    return final_result

def get_location(a):

#input list of lines of the lat,long,timestamp
# return a list of dicts, keys time,lat,long

    temp={}
    final_result=[]
    val=[]
    for i in a:
        if( len(i) == 0 ): continue
        temp={}
        i=i.rstrip()
        val= i.rsplit(",")
        temp['Timestamp'] = datetime.fromtimestamp(int(val[2])/1000)
        temp['Longitude'] = float(val[1])
        temp['Latitude'] = float(val[1])
        final_result.append(temp)
    return final_result

"""
fout = open("BatteryState_352985051054183.bst",'r')
data = fout.readlines()
fout.close()
Result = get_battery(data)

for i in Result:
    print i
"""

