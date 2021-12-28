#!/usr/bin/python
import os
import subprocess
import shlex
import commands
import time

kn = 4
fnir = open
#def onedisj(u1, u2, a, b):   # u2 = u1(x + a)^b
def onedisj(u1, x, kkf, kakfs, tt, firstflag, itert):     # from last u1, another - formir again
	sumitk = 0
	if firstflag == 0:
		ka = kkf + 2
		kb = ka + 2
		ku2 = ka + 4
		#kakfs.append(ka)
	else:
		if itert == 0:
			ku2 = kkf + 6 
			kkf = kakfs[tt]		
			ka = kakfs[tt] + 2
			kb = ka + 2
		else:
			kkf = kkf
			ka = kakfs[tt] + 6 * itert + 2
			kb = ka + 2
			ku2 = kkf + 6
	for ia in range (kn):
		ia1 = ia // 2     # ia -> ia1/ia2 - 3 -> 11
		ia2 = ia % 2
		for ib in range (kn):	
			ib1 = ib // 2     # ib -> ib1/ib2 - 3 -> 11
			ib2 = ib % 2  	
################# THINK THAT WE CAN DELETE CYCLE FOR KN AND TAKE ONLY ONE RANGE - RANGE(1)
			#for iu2 in range (kn): 
			for iu2 in range (1):
				sumitk = sumitk + 3
				iu21 = iu2 // 2     # iu2 -> iu21/iu22 - 3 -> 11
				iu22 = iu2 % 2 
				u11s = u1 // 2
 				u12s = u1 % 2
				
				g = (u1 * (x + ib) ** ia) % 4       # u1 here from 0 to 3
				g1 = g // 2
				g2 = g % 2
				kfw = str("-"*(u11s % 2)) + str(kkf) + " " + str("-"*(u12s % 2)) + str(kkf + 1)
				#f.write(str("- "*((ia1 + 1)%2)) + str(ka) + " " + str("- "*((ia2 + 1)%2)) + str(ka + 1) + str("- "*((ib1 + 1)%2)) + str(kb) + " " + str("- "*((ib2 + 1)%2)) + str(kb + 1) + 		
				af = str("-"*(ia1%2)) + str(ka) + " " + str("-"*(ia2%2)) + str(ka + 1) + " " + str("-"*(ib1%2)) + str(kb) + " " + str("-"*(ib2%2)) + str(kb + 1)
				#print("af = ", af)
				if g == 0:
					bf3 = str(str(-ku2) + " " + str((ku2 + 1)))
					#print("Bf3 = ", bf3)
					bf1 = str(str(-ku2) + " " + str(-(ku2 + 1)))
					bf2 = str(str(ku2) + " " + str(-(ku2 + 1)))
				elif g == 1:
					bf1 = str(str(-ku2) + " " + str(-(ku2 + 1)))
					bf2 = str(str(ku2) + " " + str((ku2 + 1)))
					bf3 = str(str(-ku2) + " " + str((ku2 + 1)))
				elif g == 2:
					bf1 = str(str(-ku2) + " " + str(-(ku2 + 1)))
					bf2 = str(str(ku2) + " " + str(-(ku2 + 1)))
					bf3 = str(str(ku2) + " " + str((ku2 + 1)))
				elif g == 3:
					bf1 = str(str(ku2) + " " + str((ku2 + 1)))
					bf2 = str(str(ku2) + " " + str(-(ku2 + 1)))
					bf3 = str(str(-ku2) + " " + str((ku2 + 1)))

				u2 = g
				allstr = kfw + " " + af + " " + bf1 + " 0" + "\n"
				f.write(allstr)
				f2.write(kfw + " " + af + " " + bf1 + " 0 " + str(g) + "\n")
				allstr = kfw + " " + af + " " + bf2 + " 0" + "\n"
				f.write(allstr)
				f2.write(kfw + " " + af + " " + bf2 + " 0 " + str(g) + "\n")
				allstr = kfw + " " + af + " " + bf3 + " 0" + "\n"
				f.write(allstr)
				f2.write(kfw + " " + af + " " + bf3 + " 0 " + str(g) + "\n")
	return u2  
			



kakfs = []
tt = 0
firstflag = 0
ourvec = '3331103033311030'

#ourvec = int(input())
#x = 0
f = open('anir.in', 'w')
f2 = open('anirotlad.in', 'w')
xs = []
w1 = []
allu1 = []
n = 2
k = 2
for wi in range(0, kn):
	w1.append(0)
	allu1.append(0)
for xi in range(0, n):
	xs.append(0)
#	allu1.append(0)
kf = 1
kkf = 1
bufkkf = 1
a = 1
for uu in range(0, kn ** n):  # its for full esop-form - all x's
	repkkf = 0
	for t in range(0, k):
		print(kakfs, t, uu)
		bufkkf = kkf
		if firstflag == 0:
			kakfs.append(kkf)
		for a in range(0, kn):  # was(1, kn)
			for itert in range(0, n):
				if itert == 0:
					u1 = a
					#f.write(str(kkf) + str(kkf+1) + ' 0' + '\n')
					u1 = onedisj(u1, xs[itert], kkf, kakfs, tt, firstflag, itert)
				else:
					for u1 in range(0, kn):     # was(1, kn)                      #its for all possible meanings of the predlast prod
						u1n = onedisj(u1, xs[itert], kkf, kakfs, tt, firstflag, itert)  
						allu1[u1] = u1n
				#u1 = onedisj(u1, xs[itert], kkf)
				kkf = kkf + 6
			if a != kn - 1:
				kkf = bufkkf
			else:
				kkf = kkf + 2 #### -- BECAUSE LAST U'S - ITS LAST AND NOT GIVEN ON UNPUT
			w1[a] = u1    # one prod with this kf
		#lastus0 = kkf - 2
		#lastus1 = kkf - 1

		if t > 0:	
	#	for t in range(0, k):
			for aa in range(0, kn):      # was(1, kn)
				aa0 = aa // 2
				aa1 = aa % 2
				for bb in range(0, kn):               # was(1, kn)
					bb0 = bb // 2
					bb1 = bb % 2
					if repkkf == 0:
						kfw = str("-"*(aa0 % 2)) + str(lastus0) + " " + str("-"*(aa1 % 2)) + str(lastus1) + " " + str("-"*(bb0 % 2)) + str(kkf - 2) + " " + str("-"*(bb1 % 2)) + str(kkf - 1)
					else:
						kfw = str("-"*(aa0 % 2)) + str(repkkf) + " " + str("-"*(aa1 % 2)) + str(repkkf + 1) + " " + str("-"*(bb0 % 2)) + str(kkf - 2) + " " + str("-"*(bb1 % 2)) + str(kkf - 1)
					g = (aa + bb) % 4
					if g == 0:
						bf3 = str(str(-kkf) + " " + str((kkf + 1)))
						bf1 = str(str(-kkf) + " " + str(-(kkf + 1)))
						bf2 = str(str(kkf) + " " + str(-(kkf + 1)))
					elif g == 1:
						bf1 = str(str(-kkf) + " " + str(-(kkf + 1)))
						bf2 = str(str(kkf) + " " + str((kkf + 1)))
						bf3 = str(str(-kkf) + " " + str((kkf + 1)))
					elif g == 2:
						bf1 = str(str(-kkf) + " " + str(-(kkf + 1)))
						bf2 = str(str(kkf) + " " + str(-(kkf + 1)))
						bf3 = str(str(kkf) + " " + str((kkf + 1)))
					elif g == 3:
						bf1 = str(str(kkf) + " " + str((kkf + 1)))
						bf2 = str(str(kkf) + " " + str(-(kkf + 1)))
						bf3 = str(str(-kkf) + " " + str((kkf + 1)))
					allstr = kfw + " " + bf1 + " 0" + "\n"
					f.write(allstr)
					f2.write(kfw + " " + bf1 + " 0 " + str(g) + "\n")
					allstr = kfw + " " + bf2 + " 0" + "\n"
					f.write(allstr)
					f2.write(kfw + " " + bf2 + " 0 " + str(g) + "\n")
					allstr = kfw + " " + bf3 + " 0" + "\n"
					f.write(allstr)
					f2.write(kfw + " " + bf3 + " 0 " + str(g) + "\n")

		lastus0 = kkf - 2
		lastus1 = kkf - 1
		if t > 0:
			repkkf = kkf # for remambaring
			kkf = kkf + 2  # its because we have new pers
		tt = tt + 1    # for mas kakfs - cause we will go on it and take olds a and b

	tt = 0
	firstflag = 1
 	if k != 1:
		if ourvec[uu] == '0':
			f.write(str(-repkkf) + " 0" + "\n" + str(-(repkkf+1)) + " 0" + "\n")
		elif ourvec[uu] == '1':
			f.write(str(-repkkf) + " 0" + "\n" + str((repkkf+1)) + " 0" + "\n")
		elif ourvec[uu] == '2':
			f.write(str(repkkf) + " 0" + "\n" + str(-(repkkf+1)) + " 0" + "\n")
		elif ourvec[uu] == '3':
			f.write(str(repkkf) + " 0" + "\n" + str((repkkf+1)) + " 0" + "\n")
	else:
		if ourvec[uu] == '0':
			f.write(str(-(kkf-2)) + " 0" + "\n" + str(-(kkf-1)) + " 0" + "\n")
		elif ourvec[uu] == '1':
			f.write(str(-(kkf-2)) + " 0" + "\n" + str((kkf-1)) + " 0" + "\n")
		elif ourvec[uu] == '2':
			f.write(str((kkf-2)) + " 0" + "\n" + str(-(kkf-1)) + " 0" + "\n")
		elif ourvec[uu] == '3':
			f.write(str((kkf-2)) + " 0" + "\n" + str((kkf-1)) + " 0" + "\n")



	for xi in range(0, n):
		xs[n - xi - 1] = (xs[n - xi - 1] + 1) % 4
		if xs[n - xi - 1] != 0:
			break
	f2.write('------------ x0 = ' + str(uu // kn) + 'x1 = ' + str(uu % kn) + '----------------------' + '\n')
	print("xs = ", xs)


f.close()
f2.close()
os.system('/home/andrei/minisat/simp/minisat_static anir.in bnir.out')   # path to satsolver
ff = open('bnir.out')
#print("u = ", u)
if ff.read(3) == "SAT":
	print("len = ", k)
print(xs)
ff.close()



		

                
