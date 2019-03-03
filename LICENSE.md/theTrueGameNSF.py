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
atk = '10';
deff = '10';
mag = '10';
res = '10';
hp = '100';
magCool = '0';
turns = '0'






#autoconfig
def autoConfig():
	global os;
	global clear;
#what to do if linux
	if opsys.lower() == 'linux' or opsys.lower() == 'linux1' or opsys.lower() == 'linux2':
		clear = 'clear';
		gameStatGen();
#what to do if windows
	elif opsys.lower() == 'win' or opsys.lower() == 'win32':
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
	monHp = random.randint(10, 20) * int(lvl) + int(hp);

#fighting
	fight();



def fight():
	global turns;
	global tempHp;
	global monHp;
	tempTurn = int(turns) + 1;
	turns = tempTurn;
	print('Type the number of your option');
	print('Monster HP', monHp);
	print('Your HP', tempHp);
	print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------');
	print('1. Attack');
	print('2. Deffend');
	print('3. Flee');
	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------');
	userIn = input('>>>');

	if userIn == '1':
		os.system(clear);
		os.system(clear);
		print('Attack');
		print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------');
		print('1. Fist');
		print('2. Sword');
		print('3. Magic');
		print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------');
		userIn = input('>>>');

		if userIn == '1':
			trueAtk = int(tempAtk) + random.randint(-5, 5);
			monHpTemp = int(monHp) - (monDef - int(trueAtk));
			monHp = monHpTemp;
			monAtk();

		elif userIn == '2':
			trueAtk = int(tempAtk) + random.randint(-10, 10);
			monHpTemp = int(monHp) - (monDef - int(trueAtk));
			monHp = monHpTemp;
			monAtk();

		elif userIn == '3':
			if magCool <= '0':
				magAtk = int(tempMag) + random.randint(10, 40);
				magCool = magAtk;
				monHpTemp = monHP - (magAtk - monDef);
				monHp = monHpTemp;
				monAtk();
			if magCool > '0':
				print('You can not use magic yet');
				time.sleep(4);
				fight();
		else:
			print('Not a valid option');
			time.sleep(3);
			fight();


	if userIn == '2':
		print('Your deffence stat is', tempDef)


def monAtk():
	print('Monster Attack');
	fight();



autoConfig();
