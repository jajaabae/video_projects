import os

def folder_digger_fips(path):
    fips = []
    for e in os.listdir(path):
        eip = path+'/'+e
        if os.path.isfile(eip):
            fips.append(eip)
        if os.path.isdir(eip):
            fips += folder_digger_fips(eip)
    return fips
    
