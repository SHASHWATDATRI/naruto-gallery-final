import pymysql

# Django ko dhokha dene ke liye bada version number daalein
pymysql.version_info = (2, 2, 1, 'final', 0) 
pymysql.install_as_MySQLdb()