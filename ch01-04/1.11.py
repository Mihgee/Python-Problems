population=312032486
seconds1=(365*24*60*60)
seconds2=(365*24*60*60*2)
seconds3=(365*24*60*60*3)
seconds4=(365*24*60*60*4)
seconds5=(365*24*60*60*5)
#5
births5=(seconds5//7)
deaths5=(seconds5//13)
immigrants5=(seconds5//45)
#4
births4=(seconds4//7)
deaths4=(seconds4//13)
immigrants4=(seconds4//45)
#3
births3=(seconds3//7)
deaths3=(seconds3//13)
immigrants3=(seconds3//45)
#2
births2=(seconds2//7)
deaths2=(seconds2//13)
immigrants2=(seconds2//45)
#1
births1=(seconds1//7)
deaths1=(seconds1//13)
immigrants1=(seconds1//45)
#print("Total seconds in 5 years is",seconds)
#1
pop1=(population+births1+immigrants1-deaths1)
print("The total population in 1 year will be",pop1)
#2
pop2=(population+births2+immigrants2-deaths2)
print("The total population in 2 years will be",pop2)
#3
pop3=(population+births3+immigrants3-deaths3)
print("The total population in 3 years will be",pop3)
#4
pop4=(population+births4+immigrants4-deaths4)
print("The total population in 4 years will be",pop4)
#5
pop5=(population+births5+immigrants5-deaths5)
print("The total population in 5 years will be",pop5)