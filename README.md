# A simple calculator to calculate simple interest.

to use this calculator, you first have to import the file.
to import the file, you do;
import si_calc

# calculating for the simple interest.
to calculate the simple interest, you have to call the simple interest function.
to call the function, you do;
   print(SI(200,3,0.035))
   now run the code.
in the code above, the arguments passed to the function are passed in an order.
the order of which the code was passed is "P" which is principal, "T" which is for time and then "R" which us the rate.

you can also do;
    print(f"The simple interest = {SI(200,8,0.035)} $")
in this way the output becomes readable and user friendly. 

# calculating for the Principal.
to calculate for the Principal, you have to call the function out as well.
to call the function, you do;
    print(principal(200,0.035,5))
in this order the "I" comes first then the "R" then finally the "T".

print(f"the principal = {principal(200,0.035,5)} years")
the code above can also be done to make the output user friendly and readable.

# calculating for the Time.
to calculate the time, you have to call the time function.
to do this, you do;
    print(time(200,300,0.035))

in calling the function, the arguments are to be passed in this manner:
(I,P,R)

print(f"the time = {time(200,300,0.035)} years")
this code will make the output meaningful and readable.

# calculating for the Rate.
to calculate the rate as usual you have to call the rate function.
to call the rate function, you do;
    print(rate(200,300,5))

in this code, the order of passing arguments is;
(I,P,T).

print(f"the rate = {rate(200,300,5)} %")
    the above code, makes the output meaningful and readable.


that's all on how to use the si_calc.
