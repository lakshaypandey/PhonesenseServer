from PhoneSense.TrackServer.models import *

import DataParser


def InsertData_DB( Type, RawData , DEVICE_ID ):

    if( Type == "wst" ): Records = DataParser.get_wifi(RawData.split('\n'))
    if( Type == "pst" ): Records = DataParser.get_phonestate(RawData.split('\n'))
    if( Type == "bst" ): Records = DataParser.get_battery(RawData.split('\n'))
    if( Type == "btst" ): Records = DataParser.get_bluetooth(RawData.split('\n'))
    if( Type == "gst" ): Records = DataParser.get_gsm(RawData.split('\n'))
    if( Type == "lst" ): Records = DataParser.get_location(RawData.split('\n'))

    for record in Records:

        DataObject = None

        if( Type == "wst" ):
            DataObject = WiFi( DeviceID=DEVICE_ID , **record )

        if( Type == "pst" ):
            DataObject = Phone( DeviceID=DEVICE_ID , **record )

        if( Type == "bst" ):
            DataObject = Battery( DeviceID=DEVICE_ID , **record )

        if( Type == "btst" ):
            DataObject = Bluetooth( DeviceID=DEVICE_ID , **record )

        if( Type == "gst" ):
            DataObject = Cellular( DeviceID=DEVICE_ID , **record )

        if( Type == "lst" ):
            DataObject = GPS( DeviceID=DEVICE_ID , **record )

        DataObject.save()