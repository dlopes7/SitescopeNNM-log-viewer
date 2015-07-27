from subprocess import call
import time

count = 0
while 1:
    count +=1
    start = time.time()
    call(["C:\\Users\\david.lopes\\Documents\\HP DAVID\\Sitescope\\Customizacoes\\Alert Log Viewer\\atualiza_sitescope.bat"])
    print ('Refresh: ' + str(count) + ' concluido em: ' + "{0:.2f}".format(time.time() - start) + ' segundos')
    time.sleep(300)
