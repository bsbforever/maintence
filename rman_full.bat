rman target sys/system nocatalog CMDFILE 'E:\BAK\LEDFULLBAK\rman_full.txt' log='E:\BAK\log\full_backup_%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%".log'
@pause