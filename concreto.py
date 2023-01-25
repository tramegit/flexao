# flexosr Flexão simples reta seção retangular
import math

def flexosr(md, bw, d, fck, fyk):

	if fck <= 50:
		lamb = 0.80
		alpha = 0.85
	else:
		lamb = 0.80 - ((fck-50)/400)
		alpha = 0.85 * (1.0 - ((fck-50)/200))
	fcd = fck / 14
	k = md / (fcd * bw * d**2)
	bx = (1/lamb) * (1 - math.sqrt(1 - (2/alpha) * k))
	xc = d * bx
	yc = xc * lamb
	fyd = fyk / 11.5
	as1 = md / (fyd * (d - (yc/2)))
	eyd = fyd / 21000
	x34 = 0.0035 / (0.0035 + eyd)
   
	return [ as1, yc, xc, eyd, x34 ]

