import scratchapi
import time

class Main:
    def decode(encodestring):
        encode = list(encodestring)
        letters = [" ","!",'"',"#","$","%","&","'","(",")","*","+",",","-",".","/","0",
                   "1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A",
                   "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
                   "S","T","U","V","W","X","Y","Z","[","/","]","^","_","`","a","b","c",
                   "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
                   "u","v","w","x","y","z","{","|","}","~","£"]
        decodevar = "";
        i = 0
        while i < len(encode):
            ii = encode[i] + encode[i + 1]
            if (ii == "00"):
                break
            decodevar += letters[int(ii) - 1]
            i += 2
        return decodevar

    scratch = scratchapi.ScratchUserSession("Cloud-", "Duncan2003")
    cloud = scratchapi.CloudSession(116725373, scratch)

    while (True):
        if(cloud.get_var("port") == "0" or cloud.get_var("port") == "1"):
            print("No one is on, stopping")
        else:
            print(decode(cloud.get_var("port")) + " is on!")
            cloud.set_var("port", "1")
        time.sleep(1)

