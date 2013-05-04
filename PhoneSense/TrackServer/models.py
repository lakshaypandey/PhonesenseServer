from django.db import models


class DataCollection(models.Model):

    CollectionName = models.CharField( max_length=100, null=True )
    User_FirstName = models.CharField( max_length=100, null=True )
    User_LastName = models.CharField( max_length=100, null=True )
    IMEI_FILE = models.FileField( upload_to='IMEI' , null=True )
    DataSensors = models.TextField( null=True )
    UploadFrequency = models.PositiveIntegerField( null=True )


class CollectionDevice(models.Model):

    IMEI = models.CharField( max_length=100, primary_key=True )
    DataSensors = models.TextField( null=True )
    UploadFrequency = models.PositiveIntegerField( null=True )


class User(models.Model):

    DeviceID = models.CharField( max_length=100, null=True )
    EmailID = models.EmailField( max_length=100, null=True )
    CellNumber = models.CharField( max_length=100, null=True )
    WifiMAC = models.CharField( max_length=100, null=True )
    BtMAC = models.CharField( max_length=100, null=True )


class WiFi(models.Model):

    Timestamp = models.DateTimeField()
    DeviceID = models.CharField( max_length=100, null=True )
    BSSID = models.CharField( max_length=100, null=True )
    SSID = models.CharField( max_length=100, null=True )
    RSSI = models.IntegerField( null=True )


class Bluetooth(models.Model):

    Timestamp = models.DateTimeField()
    DeviceID = models.CharField( max_length=100, null=True )
    BSSID = models.CharField( max_length=100, null=True )
    SSID = models.CharField( max_length=100, null=True )


class Cellular(models.Model):

    Timestamp = models.DateTimeField()
    DeviceID = models.CharField( max_length=100, null=True )
    MCC = models.CharField( max_length=100, null=True )
    MNC = models.CharField( max_length=100, null=True )
    CellID = models.CharField( max_length=100, null=True )
    Lac = models.CharField( max_length=100, null=True )
    NetworkType = models.CharField( max_length=100, null=True )
    NetworkStatus = models.CharField( max_length=100, null=True )
    NetworkCellIDs = models.CharField( max_length=500, null=True )
    RSSI = models.IntegerField( max_length=100, null=True )


class GPS(models.Model):

    Timestamp = models.DateTimeField()
    DeviceID = models.CharField( max_length=100, null=True )
    Latitude = models.FloatField(null=True)
    Longitude = models.FloatField(null=True)
    Accuracy = models.IntegerField(null=True)


class Photo(models.Model):

    Timestamp = models.DateTimeField()
    DeviceID = models.CharField( max_length=100, null=True )
    FILE = models.FileField( upload_to='images' , null=True )


class Phone(models.Model):
        
    Timestamp = models.DateTimeField()
    DeviceID = models.CharField( max_length=100, null=True )
    State = models.CharField( max_length=100, null=True )

class Battery(models.Model):

    Timestamp = models.DateTimeField()
    DeviceID = models.CharField( max_length=100, null=True )
    Level = models.IntegerField( null=True )
    ChargingStatus = models.IntegerField( null=True )
    Scale = models.IntegerField( null=True )
    Batterypct = models.FloatField( null=True )


class DataFile(models.Model):

    DeviceID = models.CharField( max_length=100, null=True )
    FILE = models.FileField( upload_to='sensor' , null=True )