def computepay(h, r):
	if h <=40:
		pay = h * r
	else:
		pay = r * 40 + (r * 1.5 * (h - 40))
	return pay

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter Rate:")
r = float(rate)

pay = computepay (h, r)

print pay