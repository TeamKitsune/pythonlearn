def computepay(h,r):
    if h <= 40 :
        return h * r
    elif  h > 40 :
        return (40 * r) + (h - 40) * (r * 1.5)

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)

p = computepay(h,r)
print 'Pay', p


#return 42.37  