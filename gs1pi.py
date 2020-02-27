
import RPi_I2C_driver
import time 
import os
import datetime
mylcd = RPi_I2C_driver.lcd()
scrn=1
loop=0
while True:
	if scrn == 1:
		if loop == 0:
			ncall="""boinccmd --get_state > op.txt"""
			nname="Node:0"
			time.sleep(1)
		#if loop == 1:
                #	ncall="""pdsh -w 192.168.10.2 -N -R ssh "boinccmd --get_state" > op.txt"""
                #	nname="Node:1"
		#if loop == 2:
                #	ncall="""pdsh -w 192.168.11.2 -N -R ssh "boinccmd --get_state" > op.txt"""
                #	nname="Node:2"
		#if loop == 3:
               # 	ncall="""pdsh -w 192.168.12.2 -N -R ssh "boinccmd --get_state" > op.txt"""
                #	nname="Node:3"
		#if loop == 4:
                #	ncall="""pdsh -w 192.168.13.2 -N -R ssh "boinccmd --get_state" > op.txt"""
                #	nname="Node:4"
	
		#loop = loop + 1
		#if loop == 5:
		#	loop = 0 
		os.system(ncall)
		time.sleep(2)
	
		fp = open("op.txt", "r")
		line = fp.readline()



		while line:
	
			line = fp.readline()
	 
			if line[3:22] == "active_task_state: ":
				op=line.split(":")
				a = op[1].replace("\r","")
				a = a.replace("\n","")
				a = a.replace(" ","")

			if line[3:18] == "fraction done: ":
                		op2=line.split(":")
				b = op2[1].replace("\r","")
				b = b.replace("\n","")
				b = b.replace(" ","")

			if line[3:19] == "jobs succeeded: ":
                		op3=line.split(":")
                		d = op3[1].replace("\r","")
                		d = d.replace("\n","")
                		d = d.replace(" ","")

		


		c = str(100 * float(b))

		now = datetime.datetime.now()
		dt =  (now.strftime("%d/%m/%Y  %H:%M:%S"))

		mylcd.lcd_clear()
		mylcd.lcd_display_string(nname+" -- Done: "+d, 1)
		mylcd.lcd_display_string(a, 2)
		mylcd.lcd_display_string(dt, 4)
		mylcd.lcd_display_string(c+"% Complete", 3)

		fp.close()
