from random import *
#import ntplib
from datetime import datetime, timezone


def values(li):
    li = []
    
    ntpprod= ntplib.NTPClient()
    response = ntpprod.request('uk.pool.ntp.org', version=3)
    response.offset
    dateprod = datetime.fromtimestamp(response.tx_time+2)
    
    temps_cuve = round(uniform(2.5,4),1)
    temps_ext = round(uniform(8,14),1)
    pds_lait = randint(3512,4607)
    ph = round(uniform(6.8,7.2),1)
    k_plus = randint(35,47)
    conc_nacl = round(uniform(1,1.7),1)
    niv_salmonelle = randint(17,37)
    niv_ecoli = randint(35,49)
    niv_listeria = randint(28,54)
    li.append(temps_cuve)
    li.append(temps_ext)
    li.append(pds_lait)
    li.append(ph)
    li.append(k_plus)
    li.append(conc_nacl)
    li.append(niv_salmonelle)
    li.append(niv_ecoli)
    li.append(niv_listeria)
    return li
