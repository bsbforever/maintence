rman target sys/system nocatalog CMDFILE 'E:\BAK\LEDARCBAK\rman_arc.txt' log='E:\BAK\log\arc_backup_%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%".log'
@pause