print ("===================CAFE==================")
print ("=========MASUKKAN JUMLAH PESANAN=========")
CAPPUCINO =int(input("CAPPUCINO      DISKON 50%      Rp 25.000      : "))
VANILLA   =int(input("VANILLA LATTE  DISKON 65%      Rp 22.000      : "))
AMERICANO =int(input("AMERICANO      DISKON 35%      Rp 30.000      : "))
COFEE     =int(input("BREWED COFFEE  DISKON 40%      Rp 20.000      : "))
print ("==================TOTAL==================")
totalcap = ((25000*CAPPUCINO)- 25000*CAPPUCINO*50/100)
totalval = ((22000*VANILLA)- 22000*VANILLA*65/100)
totalame = ((30000*AMERICANO)- 30000*AMERICANO*35/100)
totalcof = ((20000*COFEE)-20000*COFEE*40/100)
print("TOTAL CAPPUCINO     :",totalcap)
print("TOTAL VANILLA     :",totalval)