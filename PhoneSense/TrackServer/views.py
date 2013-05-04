# Create your views here.
from django.http import HttpResponse
from django.utils import simplejson
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.core import serializers

from datetime import datetime

from PhoneSense.TrackServer.models import *
from PhoneSense.TrackServer.utils import IMEIParser, DataParser, DatabaseManager


def home(request):
    return render_to_response('index.html')


def init(request):
    return HttpResponse(simplejson.dumps({'status':'SUCCESS'}), mimetype='application/json')


def register(request):
    return render_to_response('data_collect.html')


def source(request):
    return render_to_response('source.html')


def documentation(request):
    return render_to_response('Documentation.html')


@csrf_exempt
def NewDataCollection(request):

    if request.method == 'POST':

        DATA_SENSORS = ""
        if( request.POST.get('Data_Types_Wifi_chckbx') ):
            DATA_SENSORS += 'Wifi:'+request.POST.get('Wifi_Freq')+';'

        if( request.POST.get('Data_Types_Bluetooth_chckbx') ):
            DATA_SENSORS += 'Bluetooth:'+request.POST.get('Bluetooth_Freq')+';'

        if( request.POST.get('Data_Types_GSM_chckbx') ):
            DATA_SENSORS += 'GSM:'+request.POST.get('GSM_Freq')+';'

        if( request.POST.get('Data_Types_GPS_chckbx') ):
            DATA_SENSORS += 'GPS:'+request.POST.get('GPS_Freq')+';'

        if( request.POST.get('Data_Types_PhoneState_chckbx') ):
            DATA_SENSORS += 'Phone:'+request.POST.get('PhoneState_Freq')+';'

        if( request.POST.get('Data_Types_element_Battery_chckbx') ):
            DATA_SENSORS += 'Battery:'+request.POST.get('Battery_Freq')+';'

        NEW_COLLECTION = DataCollection(
                                        CollectionName = request.POST.get('Study_Name'),
                                        User_FirstName = request.POST.get('User_Name_1'),
                                        User_LastName = request.POST.get('User_Name_2'),
                                        DataSensors = DATA_SENSORS,
                                        UploadFrequency = int(request.POST.get('Upload_Freq'))
                                       )

        FileData = request.FILES['File_upload'].read()
        FileContent = ContentFile(FileData)
        FileName = request.FILES['File_upload'].name
        NEW_COLLECTION.IMEI_FILE.save(FileName, FileContent)

        NEW_COLLECTION.save()

        IMEIParser.StoreIMEIData( FileData, DATA_SENSORS , NEW_COLLECTION.UploadFrequency ) 
        
        return HttpResponse("Your Data Collection request has been successfully registered ! Thanks !!")


@csrf_exempt
def Handshake(request):

    if request.method == 'POST':

        USER = User(
                    DeviceID = request.POST.get('deviceid'),
                    EmailID = request.POST.get('email'),
                    CellNumber = request.POST.get('cellnumber'),
                    WifiMAC = request.POST.get('wifimac'),
                    BtMAC = request.POST.get('btmac')
                   )

        USER.save()

        DEVICE = CollectionDevice.objects.get( IMEI=USER.DeviceID )

        return HttpResponse( DEVICE.DataSensors+'Upload:'+str(DEVICE.UploadFrequency) )


@csrf_exempt
def FileUpload(request):

    DATA_FILE = DataFile( DeviceID = request.GET.get('deviceid') )

    RawFileContent = request.FILES['file'].read()
    FileContent = ContentFile(RawFileContent)
    FileName = (request.FILES['file'].name).split('.')
    DATA_FILE.FILE.save(FileName[0]+'_'+str(datetime.now().strftime("%Y%m%d%H%M%S"))+'.'+FileName[1], FileContent)
    
    DATA_FILE.save()

    DatabaseManager.InsertData_DB( FileName[1], RawFileContent , DATA_FILE.DeviceID )
        
    return HttpResponse("SUCCESS")


@csrf_exempt
def API(request):

    DEVICE_ID = request.GET.get('deviceid')
    DataType = request.GET.get('datatype')
    From = datetime.strptime(request.GET.get('from'), '%Y-%m-%dT%H:%M:%S')
    To = datetime.strptime(request.GET.get('to'), '%Y-%m-%dT%H:%M:%S')

    ResultData = None

    if( DataType == "wifi" ):
        ResultData = WiFi.objects.filter( DeviceID=DEVICE_ID , Timestamp__range=(From,To) )

    ResultJson = serializers.serialize("json", ResultData)

    return HttpResponse(ResultJson, mimetype='application/json')

    
