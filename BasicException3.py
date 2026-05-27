import sys
try:
    File=open('mygile.txt')
except IOError as e:
    print("Error opneing file!\r\n"+
          "Error Number:{0}\r\n".format(e.errno)+
          "Error Text:{0}".format(e.strerror))
else:
    print("File Openedd as expected.")
    File.close();
