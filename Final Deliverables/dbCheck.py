import ibm_db

connection = ibm_db.connect("DATABASE=bludb;HOSTNAME=2d46b6b4-cbf6-40eb-bbce-6251e6ba0300.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=32328;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xrl27444;PWD=TR5CfVrO2n3Q92s4",'','')s

print(connection)
print("Connection Successfull !\n\n")

sql = "SELECT EMAIL,PASSWORD FROM logins"
stmt = ibm_db.exec_immediate(connection, sql)
dictionary = ibm_db.fetch_assoc(stmt)
while dictionary != False:
    # printing
    print("Full Row : ", dictionary)
    dictionary = ibm_db.fetch_assoc(stmt)