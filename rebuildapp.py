    
#!/usr/bin/env python

import os, openpyxl, sys, pprint, shutil

#Definimos la funcion Copiar y reemplazar carpeta completa
def copiarYReemplazar(src, dst):
    if os.path.exists(dst):
             shutil.rmtree(dst)
             shutil.copytree(src, dst)

os.chdir('/Users/lenguajesport/Desktop/lsportdesarrollo/PythonGenerator')
print('Opening workbook...')
wb = openpyxl.load_workbook('nuevaapp.xlsx')
#sheet = wb.get_sheet_by_name('Clubes')
sheet = wb.active

clubes = {}
print('Reading rows...')
x = 0
for cellObj in sheet.columns[3]:
            clubes[x] = cellObj.value
            x = x + 1
            print(clubes)
            print (x)
             
searchedEnsamblado = input('Cual es el nombre de ensamblado de la aplicacion a actualizar? ej: com.ls.ciudad+club ')
print(searchedEnsamblado)
if searchedEnsamblado in clubes.values(): 
    print('existee')

    for fila, ensamblado in clubes.items():
            if ensamblado == searchedEnsamblado:
             print(fila)
             celda = fila + 1

    print(celda)
    clubName  = sheet['B' + str(celda)].value
    directoryName  = sheet['C' + str(celda)].value
    ensambledName = sheet['D' + str(celda)].value
    templateName = sheet['E' + str(celda)].value
    iconSet = sheet['F' + str(celda)].value
    appType = sheet['G' + str(celda)].value
    print(directoryName)
    print(templateName)


    cdRoot = 'cd Desktop/lsportdesarrollo/NewProyects/'
    cdProyect = 'cd ' + directoryName
    print(cdProyect)

    #ahora copiamos los directorios con los recursos graficos
    import distutils
    from distutils import dir_util
    resourcesThirdLabel = '/Users/lenguajesport/Desktop/LenguajeSport/RecursosGraficosActual/3raCapaRecursosClubes/'
    res = '/Cordova/res/'

    #comenzamos con la carpeta res que tierne las imagenes de splash e iconos
    dstNewProyect = '/Users/lenguajesport/Desktop/lsportdesarrollo/NewProyects/'
    srcRes = resourcesThirdLabel+ ensambledName+ res
    dstRes = dstNewProyect+ directoryName + '/res'
    print(srcRes)
    print(dstRes)
    
    copiarYReemplazar(srcRes, dstRes)
                     
    #seguimos con las carpetas en la plataforma android donde se guardan los iconos para notificaciones push
    iconPushNot = '/Cordova/platforms/android/res/'
    srcPushIconHdpi = resourcesThirdLabel + ensambledName + iconPushNot + 'mipmap-hdpi/notification_icon.png'
    srcPushIconLdpi = resourcesThirdLabel + ensambledName + iconPushNot + 'mipmap-ldpi/notification_icon.png'
    srcPushIconMdpi = resourcesThirdLabel + ensambledName + iconPushNot + 'mipmap-mdpi/notification_icon.png'
    srcPushIconXhdpi = resourcesThirdLabel + ensambledName + iconPushNot + 'mipmap-xhdpi/notification_icon.png'
    srcPushIconXxhdpi = resourcesThirdLabel + ensambledName + iconPushNot + 'mipmap-xxhdpi/notification_icon.png'
    srcPushIconXxhdpi = resourcesThirdLabel + ensambledName + iconPushNot + 'mipmap-xxxhdpi/notification_icon.png'

    dstPushIconHdpi = dstNewProyect + directoryName + '/platforms/android/res/mipmap-hdpi/'
    dstPushIconLdpi = dstNewProyect + directoryName + '/platforms/android/res/mipmap-ldpi/'
    dstPushIconMdpi = dstNewProyect + directoryName + '/platforms/android/res/mipmap-mdpi/'
    dstPushIconXhdpi = dstNewProyect + directoryName + '/platforms/android/res/mipmap-xhdpi/'
    dstPushIconXxhdpi = dstNewProyect + directoryName + '/platforms/android/res/mipmap-xxhdpi/'
    dstPushIconXxxhdpi = dstNewProyect + directoryName + '/platforms/android/res/mipmap-xxxhdpi/'

    shutil.copy(srcPushIconHdpi, dstPushIconHdpi)
    shutil.copy(srcPushIconLdpi, dstPushIconLdpi)
    shutil.copy(srcPushIconMdpi, dstPushIconMdpi)
    shutil.copy(srcPushIconXhdpi, dstPushIconXhdpi)
    shutil.copy(srcPushIconXxhdpi, dstPushIconXxhdpi)
    shutil.copy(srcPushIconXxhdpi, dstPushIconXxxhdpi)

    #copiamos la carpeta www principal que tiene el codigo para todas las app
    #resourcesFirstLabel = '/Users/lenguajesport/Desktop/LenguajeSport/RecursosGraficosActual/1raCapaRecursosGenerales/wwwNoHomeBannerPhoneNumber'
    #resourcesFirstLabel = '/Users/lenguajesport/Desktop/LenguajeSport/RecursosGraficosActual/1raCapaRecursosGenerales/wwwNewFinalVersion/wwwTesting'
    #resourcesFirstLabel = '/Users/lenguajesport/Desktop/LenguajeSport/RecursosGraficosActual/1raCapaRecursosGenerales/wwwPhoneNumberProductionBugFixed'
    resourcesFirstLabel = '/Users/lenguajesport/Desktop/LenguajeSport/RecursosGraficosActual/1raCapaRecursosGenerales/' + appType + '/wwwPhoneNumberTestingNotObserverFixedLast'
    dstWww = dstNewProyect + directoryName + '/www'

    copiarYReemplazar(resourcesFirstLabel, dstWww)

    #en la carpeta www-img-club vamos a copiar los tres archivos archivos de background inicio, bakcground sobre el club y club-shield
    imgClub = '/Cordova/www/club/'
    srcImgBackground = resourcesThirdLabel + ensambledName + imgClub + 'background.png'
    srcImgClubShield = resourcesThirdLabel + ensambledName + imgClub + 'club-shield.png'
    srcImgBackgroundAbout = resourcesThirdLabel + ensambledName + imgClub + 'background-about.png'

    dstImg = dstNewProyect + directoryName + '/www/img/club'

    shutil.copy(srcImgBackground, dstImg)
    shutil.copy(srcImgClubShield, dstImg)
    shutil.copy(srcImgBackgroundAbout, dstImg)

    #comienza copiado del template, el css y los iconos de la app
    resourceIconTemplate = '/Users/lenguajesport/Desktop/LenguajeSport/RecursosGraficosActual/2daCapa_Templates/' + templateName + '/' + iconSet +'/template'
    dstIconTemplate = dstNewProyect + directoryName + '/www/img/template'

    copiarYReemplazar(resourceIconTemplate, dstIconTemplate)

    #se copia el archivo css
    srcCssTemplate = '/Users/lenguajesport/Desktop/LenguajeSport/RecursosGraficosActual/2daCapa_Templates/' + templateName + '/template-club.css'
    dstCssTemplate = dstNewProyect + directoryName + '/www/css'

    shutil.copy(srcCssTemplate, dstCssTemplate)

    #tambien se copia la imagen splash intermedia
    imgTemplate = '/Cordova/www/template/'
    srcImgBackground = resourcesThirdLabel + ensambledName + imgTemplate + 'screen-720x1280.png'

    dstImgBackground = dstNewProyect + directoryName + '/www/img/template'

    shutil.copy(srcImgBackground, dstImgBackground)

    #se copia la imagen por default para las noticias en miniatura y en el detalle
    srcImgNewsDefault = resourcesThirdLabel + ensambledName + '/Cordova/www/img/default-new-details.png'
    srcImgNewsList = resourcesThirdLabel + ensambledName + '/Cordova/www/img/default-news-list.png'

    dstImgNewsDefault = dstNewProyect + directoryName + '/www/img'
    dstImgNewsList = dstNewProyect + directoryName + '/www/img'

    shutil.copy(srcImgNewsDefault, dstImgNewsDefault)
    shutil.copy(srcImgNewsList, dstImgNewsList)

    #se copia el archivo page-home.js que tiene la configuracion personalizada de los ads que vamos a mostrar
    srcIPageHomeJs = resourcesThirdLabel + ensambledName + '/Cordova/www/js/pages/page-home.js'

    dstPageHomeJs = dstNewProyect + directoryName + '/www/js/pages'

    shutil.copy(srcIPageHomeJs, dstPageHomeJs)

    #Construimos el Messages_es.properties con las caracteristicas del club y los labels del tipo de proyecto del tipo de proyecto
    srcMessagesProperties = resourcesThirdLabel + ensambledName + '/Cordova/MessagesProperties/Messages_es.properties'

    propertiesFile =  open(resourcesThirdLabel + ensambledName + '/Cordova/MessagesProperties/properties.txt')
    propertiesContent = propertiesFile.readlines()
    propertiesFile.close()
    log = open(srcMessagesProperties, 'w')
    log.writelines(propertiesContent[::1])
    log.close()

    log = open(srcMessagesProperties, 'a')
    log.write('\n')
    log.close()

    labelFile = open(resourcesThirdLabel + ensambledName + '/Cordova/MessagesProperties/label.txt')
    labelContent = labelFile.readlines()
    labelFile.close()
    labels = open(srcMessagesProperties, 'a')
    labels.writelines(labelContent[::1])
    labels.close()

    #se copia el archivo Messages_es.properties
    dstMessagesProperties = dstNewProyect + directoryName + '/www/language'

    shutil.copy(srcMessagesProperties, dstMessagesProperties)

    #Copiamos los dos archivos necesarios para firmar la app por consola, el build.json y y firmaLenguajeSport
    srcBuild = '/Users/lenguajesport/Desktop/LenguajeSport/RecursosGraficosActual/1raCapaRecursosGenerales/' + appType + '/FirmaAPKAndroid/build.json'
    srcFirma = '/Users/lenguajesport/Desktop/LenguajeSport/RecursosGraficosActual/1raCapaRecursosGenerales/' + appType + '/FirmaAPKAndroid/firmaLenguajeSport'

    dstBuild = dstNewProyect + directoryName
    dstFirma = dstNewProyect + directoryName

    shutil.copy(srcBuild, dstBuild)
    shutil.copy(srcFirma, dstFirma)

    #Se copian los archivos generados por Firebase para android y ios
    srcFirebaseAndroid = resourcesThirdLabel + ensambledName + '/Firebase/google-services.json'
    srcFirebaseIos = resourcesThirdLabel + ensambledName + '/Firebase/GoogleService-Info.plist'

    dstFirebaseAndroid = dstNewProyect + directoryName
    dstFirebaseIos = dstNewProyect + directoryName

    shutil.copy(srcFirebaseAndroid, dstFirebaseAndroid)
    shutil.copy(srcFirebaseIos, dstFirebaseIos)

    #Editamos el archivo config.xml para setear el num de version, el nombre de la app y demas datos REVISAR QUE NUM DE VERSION EXISTE ACTUALMENTE QUE SINO NO LO VA A REEMPLAZAR
    versionActual = 'version="3.6.0"'
    versionPrincipal = '3.7.0'
    versionAndroid = '37'
    versionIos =  '3.7'

    # Replace variables in file
    with open(dstNewProyect + directoryName + '/config.xml', 'r+') as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace('<author email="dev@cordova.apache.org" href="http://cordova.io">', '<author email="info@lenguajesport.com" href="http://www.lenguajesport.com">'))

    with open(dstNewProyect + directoryName + '/config.xml', 'r+') as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace(versionActual, 'version="' + versionPrincipal + '" android-versionCode="' + versionAndroid + '" ios-CFBundleVersion="' + versionIos + '"'))

    with open(dstNewProyect + directoryName + '/config.xml', 'r+') as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace('<name>Test</name>', '<name>' + clubName + '</name>'))

    with open(dstNewProyect + directoryName + '/config.xml', 'r+') as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace('Apache Cordova Team', 'Lenguaje Sport'))

    with open(dstNewProyect + directoryName + '/config.xml', 'r+') as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace('A sample Apache Cordova application that responds to the deviceready event.', 'Aplicación oficial de ' + clubName))

    
    #Hacemos el build para iOS
    from subprocess import Popen, PIPE, STDOUT
    buildApk = 'cordova build android --release --buildConfig'
    cd = 'cd '
    print(cd + cdRoot + cdProyect + buildApk)
    buildIos = 'cordova build ios'

    cordovaBuild = Popen("{}; {}; {}; {} ".format(cd, cdRoot, cdProyect, buildIos), shell=True, stdin=PIPE, 
              stdout=PIPE, stderr=STDOUT, close_fds=True)
    stdout, nothing = cordovaBuild.communicate()

    #Mostramos la hora de finalizacion del proceso por consola y  escribimos en el archivo log que esta en el directorio del .py  el output de la consola
    import datetime
    now = datetime.datetime.now()
    print ("Current date and time on iOS build : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    log = open('log-rebuild-ios', 'wb')
    log.write(stdout)
    log.close()

    #Hacemos el build para  tener el apk firmado de Android
    cordovaBuild = Popen("{}; {}; {}; {} ".format(cd, cdRoot, cdProyect, buildApk), shell=True, stdin=PIPE, 
              stdout=PIPE, stderr=STDOUT, close_fds=True)
    stdout, nothing = cordovaBuild.communicate()

    #Mostramos la hora de finalizacion del proceso por consola y  escribimos en el archivo log que esta en el directorio del .py  el output de la consola
    now = datetime.datetime.now()
    print ("Current date and time on Android build : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    log = open('log-rebuild-android', 'wb')
    log.write(stdout)
    log.close()



else: 
    print('El nombre de ensamblado que ingresaste no existe en la planilla de excel')



