s1 = "ant" #attribute the string ant to s1
s2 = "bat" #attribute the string ant to s2
s3 = "cod" #attribute the string ant to s3
print( s1+ " " + s2+" " + s3) #write "ant bat cod"
print((s1 +" ") *10) #write ant 10 times
print(s1 + " " + (s2+" ")*2 + (s3+" ") * 3)  #write ant bat bat cod cod cod
print(s1 + " " + s2 + " " + s1 + " " + s2 + " "+ s1 + " "+ s2+ " " + s1 + " " + s2 + " " + s1 + " " + s2 + " " + s1 + " " + s2 + " " + s1 + " " + s2) #write ant bant 7 times
print((((s2*2)+s3+" ")*5)) #write batbatcod 5 times