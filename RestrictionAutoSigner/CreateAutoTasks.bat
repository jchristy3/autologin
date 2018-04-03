SchTasks /Create /SC WEEKLY /D WED /TN "AutoRestrSign_WED" /TR "%dp0\restrSign.bat" /ST 18:50 /DELAY 0028:00
SchTasks /Create /SC WEEKLY /D FRI /TN "AutoRestrSign_FRI_pre" /TR "%dp0\restrSign.bat" /ST 18:50 /DELAY 0028:00
SchTasks /Create /SC WEEKLY /D FRI /TN "AutoRestrSign_FRI_post" /TR "%dp0\restrSign.bat" /ST 22:50 /RI 60 /DU 03:00 /DELAY 0028:00
SchTasks /Create /SC WEEKLY /D SAT /TN "AutoRestrSign_SAT" /TR "%dp0\restrSign.bat" /ST 08:50 /RI 60 /DU 17:00 /DELAY 0028:00
SchTasks /Create /SC WEEKLY /D SUN /TN "AutoRestrSign_SUN" /TR "%dp0\restrSign.bat" /ST 08:50 /RI 60 /DU 12:00 /DELAY 0028:00


