#!/bin/sh
export TMP=/tmp
export TMPDIR=/tmp
export ORACLE_BASE=/oracle
export ORACLE_SID=ADATAMES1
export ORACLE_HOME=/oracle/product/10.2.0/db
export PATH=$ORACLE_HOME/bin:/oracle/product/10.2.0/crs/bin:$PATH
/oracle/product/10.2.0/db/bin/sqlplus -s 'sys/system as sysdba' <<EOF
set linesize 150;
set pagesize 40;
SELECT UPPER(F.TABLESPACE_NAME)  T_name,
       D.TOT_GROOTTE_MB T_totall,
       D.TOT_GROOTTE_MB - F.TOTAL_BYTES T_Used,
       TO_CHAR(ROUND((D.TOT_GROOTTE_MB - F.TOTAL_BYTES) / D.TOT_GROOTTE_MB * 100,2),'990.99') || '%' T_usage,
       F.TOTAL_BYTES Free,
       F.MAX_BYTES MAX
  FROM (SELECT TABLESPACE_NAME,
               ROUND(SUM(BYTES) / (1024 * 1024), 2) TOTAL_BYTES,
               ROUND(MAX(BYTES) / (1024 * 1024), 2) MAX_BYTES
          FROM SYS.DBA_FREE_SPACE 　
          GROUP BY TABLESPACE_NAME) F,
       (SELECT DD.TABLESPACE_NAME,
               ROUND(SUM(DD.BYTES) / (1024 * 1024), 2) TOT_GROOTTE_MB
          FROM SYS.DBA_DATA_FILES DD
         GROUP BY DD.TABLESPACE_NAME) D
 WHERE D.TABLESPACE_NAME = F.TABLESPACE_NAME;
EOF
exit

