#import shit
import time;
import os;
import platform;
import random;

#get the operating system
opsys = platform.system();

#set the clear varible
clear = 'hold';



lvl = '1';
lvlUp = '1';
atk = '10';
deff = '10';
mag = '10';
res = '10';
hp = '100';
magCool = '1';
turns = '0';
trueDef = '0';
trueRes = '0';





#autoconfig
def autoConfig():
	global os;
	global clear;
#what to do if linux
	if opsys.lower() == 'linux' or opsys.lower() == 'linux1' or opsys.lower() == 'linux2':
		clear = 'clear';
		os.system('clear');
		gameStatGen();
#what to do if windows
	elif opsys.lower() == 'win' or opsys.lower() == 'win32' or opsys.lower() == 'cygwin':
		clear = 'cls';
		gameStatGen();
#error if you arnt running windows or linux
	else:
		print('Your Operating System is not supported.');
		print('Please use a Linux or a Windows device.');
		time.sleep(3600);
		exitr();

#exit function
def exitr():
	print('Exiting...');
	time.sleep(3);
	exit();


#the main menu
def gameStatGen():
	global tempAtk;
	global tempDef;
	global tempMag;
	global tempRes;
	global tempHp;
	global monAtk;
	global monDef;
	global monMag;
	global monRes;
	global monHp;
#	global magCool;

#player stat
	tempAtk = int(atk) * int(lvl);
	tempDef = int(deff) * int(lvl);
	tempMag = int(mag) * int(lvl);
	tempRes = int(res) * int(lvl);
	tempHp = int(hp) * int(lvl);
	

#monster stat
	monAtk = random.randint(10, 20) * int(lvl) + int(atk);
	monDef = random.randint(10,20) * int(lvl) + int(deff);
	monMag = random.randint(10, 20) * int(lvl) + int(mag);
	monRes = random.randint(10, 20) * int(lvl) + int(res);
	monHp = random.randint(100, 200) * int(lvl) + int(hp);


	os.system(clear);
#fighting
	fight();


def HpCheck():
	global lvl;
	global magCool;
	magCoolTemp = int(magCool) - 1;
	magCool = magCoolTemp;
	if tempHp <= 0:
		os.system(clear);
		print('Game Over');
		time.sleep(5);
		os.system(clear);
		print('Reseting all stats...');
		time.sleep(10);
		os.system(clear);
		lvl = '1';
		gameStatGen();
	elif monHp <= 0:
		os.system(clear);
		print('You win');
		tempLvl = int(lvl) + int(lvlUp);
		lvl = tempLvl;
		print('You are now level', lvl);
		time.sleep(5);
		print('Continueing to next level');
		time.sleep(3);
		gameStatGen();
	else:
		print('F');



def fight():
	os.system(clear);
	HpCheck();
	os.system(clear);
	global lvl;
	global turns;
	global tempHp;
	global monHp;
	global trueDef;
	global trueRes;
	tempTurn = int(turns) + 1;
	turns = tempTurn;
	print('Type the number of your option');
	print('--------------------------------------------------------------------------------------------------------------------------------------');
	print('Monster HP', monHp);
	print('Your HP', tempHp);
	print('Your Defence is', tempDef);
	print('Your Attack is', tempAtk);
	print('Your Magic is', tempMag)
	print('Your Magic Resistance is', tempRes);
	print('Your Level is', lvl);
	print('--------------------------------------------------------------------------------------------------------------------------------------');
	print('1. Attack');
	print('2. Deffend');
	print('3. Flee');
	print('--------------------------------------------------------------------------------------------------------------------------------------');
	userIn = input('>>>');

	if userIn == '1':
		global clear;
		os.system(clear);
		os.system(clear);
		print('Attack');
		print('Your attack stat is', tempAtk);
		print('-------------------------------------------------------------------------------------------------------------------------------');
		print('1. Fist');
		print('2. Sword');
		print('3. Magic');
		print('-------------------------------------------------------------------------------------------------------------------------------');
		userIn = input('>>>');

		if userIn == '1':
			trueAtk = int(tempAtk) + random.randint(-5, 5);
			monHpTemp = int(monHp) - (monDef - int(trueAtk));
			monHp = monHpTemp;
			trueDef = deff;
			print('You have delt ' + str(trueAtk) + ' dammage');
			monAttk();
			fight();
		elif userIn == '2':
			trueAtk = int(tempAtk) + random.randint(10, 20);
			monHpTemp = int(monHp) - (monDef - int(trueAtk));
			monHp = monHpTemp;
			trueDef = deff;
			print('You have delt ' + str(trueAtk) + ' dammage');
			monAttk();
			fight();
		elif userIn == '3':
			global magCool;
			if magCool <= 0:
				magAtk = int(tempMag) + random.randint(10, 40);
				magCool = 5;
				monHpTemp = monHp - (magAtk - monDef);
				monHp = monHpTemp;
				print('You have delt ' + str(magAtk) + ' dammage');
				#monAttk();
				trueDef = deff;
				monAttk();
				fight();
			if magCool > 0:
				print('You can not use magic yet');
				time.sleep(4);
				fight();
		else:
			print('Not a valid option');
			time.sleep(3);
			fight();


	elif userIn == '2':
		os.system(clear);
		print('Defence');
		print('Your deffence stat is', tempDef);
		print('-------------------------------------------------------------------------------------------------------------------------------');
		print('1. Block');
		print('2. Sheild');
		print('3. Magic');
		print('-------------------------------------------------------------------------------------------------------------------------------');
		userIn = input('>>>');


		if userIn == '1':
			trueDef = tempDef + random.randint(0, 5);
			monAttk();
		elif userIn == '2':
			trueDef = tempDef + random.randint(10, 20);
			monAttk();
		elif userIn == '3':
			magDef = tempRes + random.randint(30, 40);
			monAttk();



	elif userIn == '3':
		print('Fleeing and finding new monster');
		gameStatGen();
	else:
		print('Invalid option');
		time.sleep(3);
		os.system(clear);
		fight();
def monAttk():
	global tempHp;

	#temHP = tempHp;
	#print('The monster is attacking');
#	trueMonAtk = monAtk() + lvl + random.randint(-15, 15);
	#trueHp = (int(monAtk) + int(lvl)) - int(trueDef);
	#time.sleep(5);
	#print('The monster has done ' + str(trueHp) + ' dammage');
	#time.sleep(3);
	#finTrueHp = int(temHP) - int(trueHp);
	#tempHp = finTrueHp;
	#fight();
	monType = random.randint(1, 3);
	if monType == 1:
		temHp = tempHp;
		print('The monster attacks with it\' fist');
		trueMonAtk = (int(monAtk) + int(lvl)) - int(trueDef);
		time.sleep(3);
		print('The monster has done', trueMonAtk, 'dammage');
		time.sleep(3);
		finTrueHp = int(temHp) - int(trueMonAtk);
		tempHp = finTrueHp;
		os.system(clear);
		fight();

	elif monType == 2:
		temHp = tempHp;
		print('The monster attacks with it\'s club');
		trueMonAtk = (int(monAtk) + int(lvl) + random.randint(5, 10) - int(trueDef));
		time.sleep(3);
		print('The monster has delt', trueMonAtk, 'dammage');
		time.sleep(3);
		finTrueHp = int(temHp) - int(trueMonAtk);
		tempHp = finTrueHp;
		os.system(clear);
		fight();

	elif monType == 3:
		temHp = tempHp;
		print('The monster attacks with magic');
		trueMonAtk = (int(monMag) + int(lvl) + random.randint(5, 7)) - int(trueRes);
		time.sleep(3);
		print('The monster has delt', trueMonAtk, 'dammage');
		time.sleep(3);
		finTrueHp = int(temHp) - int(trueMonAtk);
		tempHP = finTrueHp;
		os.system(clear);
		fight();
	else:
		print('Huh');
		time.sleep(4);
		fight();


autoConfig();
