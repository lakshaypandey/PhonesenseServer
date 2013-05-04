from PhoneSense.TrackServer.models import CollectionDevice


def StoreIMEIData( FILE_DATA , SensorList , UploadFreq ):

    IMEI_LIST = FILE_DATA.split('\n')
    IMEI_LIST = [ IMEI.strip() for IMEI in IMEI_LIST ]

    for IMEI_NUMBER in IMEI_LIST:

        DEVICE = CollectionDevice(
                                  IMEI = IMEI_NUMBER,
                                  DataSensors = SensorList,
                                  UploadFrequency = UploadFreq
                                 )
        DEVICE.save()