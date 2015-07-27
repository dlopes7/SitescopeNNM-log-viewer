@echo OFF
echo Copiando logs Sitescope001
xcopy "Z:\SiteScope\logs\alert.log" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\sitescope001\" /y
xcopy "Z:\SiteScope\logs\alert.log.old" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\sitescope001\" /y

echo Copiando logs Sitescope002
xcopy "Y:\SiteScope\logs\alert.log" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\sitescope002\" /y
xcopy "Y:\SiteScope\logs\alert.log.old" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\sitescope002\" /y

echo Copiando logs Sitescope003
xcopy "X:\SiteScope\logs\alert.log" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\sitescope003\" /y
xcopy "X:\SiteScope\logs\alert.log.old" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\sitescope003\" /y

echo Copiando logs Sitescope004
xcopy "W:\SiteScope\logs\alert.log" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\sitescope004\" /y
xcopy "W:\SiteScope\logs\alert.log.old" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\sitescope004\" /y

echo Copiando logs NNM
xcopy "N:\ProgramData\HP\HP BTO Software\log\nnm\incidentActions.0.0.log" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\nnm\" /y
xcopy "N:\ProgramData\HP\HP BTO Software\log\nnm\incidentActions.1.0.log" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\nnm\" /y
xcopy "N:\ProgramData\HP\HP BTO Software\log\nnm\incidentActions.2.0.log" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\nnm\" /y
xcopy "N:\ProgramData\HP\HP BTO Software\log\nnm\incidentActions.3.0.log" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\nnm\" /y
xcopy "N:\ProgramData\HP\HP BTO Software\log\nnm\incidentActions.4.0.log" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\nnm\" /y
xcopy "N:\ProgramData\HP\HP BTO Software\log\nnm\incidentActions.5.0.log" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\nnm\" /y
xcopy "N:\ProgramData\HP\HP BTO Software\log\nnm\incidentActions.6.0.log" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\nnm\" /y
xcopy "N:\ProgramData\HP\HP BTO Software\log\nnm\incidentActions.7.0.log" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\nnm\" /y
xcopy "N:\ProgramData\HP\HP BTO Software\log\nnm\incidentActions.8.0.log" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\nnm\" /y
xcopy "N:\ProgramData\HP\HP BTO Software\log\nnm\incidentActions.9.0.log" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\nnm\" /y
xcopy "N:\ProgramData\HP\HP BTO Software\log\nnm\incidentActions.10.0.log" "C:\Users\david.lopes\Documents\HP DAVID\Sitescope\Customizacoes\Alert Log Viewer\nnm\" /y



C:\Python34\python.exe "C:/Users/david.lopes/Documents/HP DAVID/Sitescope/Customizacoes/Alert Log Viewer/alert_viewer.py"
C:\Python34\python.exe "C:/Users/david.lopes/Documents/HP DAVID/Sitescope/Customizacoes/Alert Log Viewer/nnm_alerts.py"