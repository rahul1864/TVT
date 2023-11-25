lw=1100
um=900
cig=200
h=100

#total
lw=lw-((lw/100)*5)
um=um*4-((um/100)*5)
cig=cig*3
h=h*2

#total price with gst price
li=lw+((lw/100)*18)
ui=um+((um/100)*12)
ci=cig+((cig/100)*28)
hi=h
# gst price
lt=li-lw
ut=ui-um
ct=ci-cig
ht=hi-h

total=li+ui+ci+hi
if lt>ut>ct:
    print("leather wallet max gst amt=",lt)
elif ut>ct:
    print("umberlla max",ut)
else:
    print("cigarette max",ct)
print("total",total)
