#import shit
import time;
import os;
import platform;
import random;

#get the operating system
opsys = platform.system();

#set the clear varible
clear = 'hold';



global lvl;
global lvlUp;
global atk;
global deff;
global mag;
global res;
global hp;
global magCool;
global turnes;
global trueDef;
global trueRes;
global lk;
global monLvl;
global monLuck;

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
lk = '10';



title = 'Monster Fighting Terminal Game'
version = 'Beta 2.1.24 b ~ 45'

print('Monster Fighting Terminal Game Beta 2.1.24');
def verCheck():
	os.system(clear);
	ver = platform.python_version();


	if ver == '2.7.13':
		print('Loading...');

	elif ver >= '2':
		print('Warning your python version may not be compatible with this program');
		print('Please use 2.7.13');
		time.sleep(10);
	else:
		print('Your python version is not compatable please use 2.7.13 or newer');
		time.sleep(7000);
		exit();



#autoconfig
def autoConfig():
	global os;
	global clear;
#what to do if linux
	if opsys.lower() == 'linux' or opsys.lower() == 'linux1' or opsys.lower() == 'linux2':
		clear = 'clear';
		os.system('clear');
		verCheck();
		gameStatGen();
#what to do if windows
	elif opsys.lower() == 'win' or opsys.lower() == 'win32' or opsys.lower() == 'cygwin':
		clear = 'cls';
		verCheck();
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
	global tempLk;
	global monAtk;
	global monDef;
	global monMag;
	global monRes;
	global monHp;
	global monLvl;
	global monLuck;
#	global magCool;

#player stat
	tempAtk = int(atk) * int(lvl) + random.randint(10, 20) * int(lvl);
	tempDef = int(deff) * int(lvl) + random.randint(10, 20) * int(lvl);
	tempMag = int(mag) * int(lvl) + random.randint(10, 20) * int(lvl);
	tempRes = int(res) * int(lvl) + random.randint(10, 20) * int(lvl);
	tempHp = int(hp) * int(lvl) + random.randint(10, 20) * int(lvl);
	tempLk = int(lk) * int(lvl) + random.randint(-20, 200) + random.randint(0, 10) * int(lvl);

#monster stat
	if int(lvl) > 5:
		monLvl = int(lvl) + random.randint(-4, 5);
		monAtk = random.randint(15, 25) * int(monLvl) + int(atk);
		monDef = random.randint(15,25) * int(monLvl) + int(deff);
		monMag = random.randint(15, 25) * int(monLvl) + int(mag);
		monRes = random.randint(15, 25) * int(monLvl) + int(res);
		monHp = random.randint(100, 150) * int(monLvl) + int(hp);
		monLuck = (int(lk) * int(monLvl)) + (random.randint(-20, 50) * int(monLvl));

	else:
		monLvl = int(lvl);
		monAtk = random.randint(15, 25) * int(monLvl) + int(atk);
		monDef = random.randint(15,25) * int(monLvl) + int(deff);
		monMag = random.randint(15, 25) * int(monLvl) + int(mag);
		monRes = random.randint(15, 25) * int(monLvl) + int(res);
		monHp = random.randint(100, 150) * int(monLvl) + int(hp);
		monLuck = int(lk) * int(monLvl);

	os.system(clear);
#fighting
	fight();


def HpCheck():
	global lvl;
	global magCool;
	magCoolTemp = int(magCool) - 1;
	magCool = magCoolTemp;
	trueAtk = 0;
	magAtk = 0;
	trueDef = 0;
	trueRes = 0;
	if tempHp <= 0:
		os.system(clear);
		print('Game Over');
		time.sleep(5);
		os.system(clear);
		print('Reseting all stats...');
		time.sleep(10);
		magCool = '0';
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
#	else:
#		print('Theres a FUCKING error');



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
	print(version);
	print('Type the number of your option');
	print('--------------------------------------------------------------------------------------------------------------------------------------');
	print('Your Stats:							Monster Stats:');
	print('HP:			', tempHp, '					HP:		', monHp);
	print('Defence:		', tempDef, '					Defence:	', monDef);
	print('Attack:			', tempAtk, '					Attack:		', monAtk);
	print('Magic:			', tempMag, '					Magic:		', monMag);
	print('Magic Resistance:	', tempRes, '					Magic Resistance', monRes);
	print('luck:			', tempLk, '					Luck:		', monLuck);
	print('Level:			', lvl, '					Level:		', monLvl);
	print('--------------------------------------------------------------------------------------------------------------------------------------');
	print('1. Attack');
	print('2. Defend');
	print('3. Flee');
	print('4. Healing Potion');
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
			trueAtk = int(tempAtk) + random.randint(10, 25) * int(lvl);
			monHpTemp = int(monHp) - (monDef - int(trueAtk));
			monHp = monHpTemp;
			trueDef = deff;
			print('You have delt ' + str(trueAtk) + ' dammage');
			monAttk();
			HpCheck();
			fight();
		elif userIn == '2':
			acAtk = int(tempAtk) + random.randint(30, 50) * int(lvl);
			trueAtk = int(acAtk) - int(monDef);
			monHpTemp = int(monHp) - (int(acAtk) - monDef);
			monHp = monHpTemp;
			trueDef = deff;
			print('You have delt ' + str(trueAtk) + ' dammage');
			HpCheck();
			monAttk();
			fight();
		elif userIn == '3':
			global magCool;
			if magCool <= 0:
				magAtk = int(tempMag) + random.randint(40, 65) * int(lvl);
				magCool = 5;
				monHpTemp = monHp - (magAtk - monDef);
				monHp = monHpTemp;
				print('You have delt ' + str(magAtk) + ' dammage');
				#monAttk();
				trueDef = deff;
				HpCheck();
				monAttk();
				fight();


			if magCool > 0:
				print('You can not use magic yet');
				time.sleep(4);
				fight();


		elif userIn == '4':
			pot = random.randint(1, 5);
			if pot == '1':
				hpUp =  10 + random.randint(0, 10) * int(lk);
				finHp = hpUp + tempHp;
				tempHp = finHp
				print('You have drank a health potion');
				print('You gained', hpUp, 'HP');
				print('Your HP is now', tempHp);
				time.sleep(3);
				attker = random.randint(1, 2);
				if attker == '1':
					print('The monster attacked before you got a chance');
					monAtk();
					fight();
				elif attker == '2':
					print('It is your turn to attack');
					time.sleep(3);
					fight();
			else:
				print('You ');



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
			global trueDef;
			trueDef = tempDef + random.randint(0, 5) * int(lvl);
			monAttk();
			fight();
		elif userIn == '2':
			global trueDef;
			global trueRes;
			trueDef = tempDef + random.randint(1, 10) * int(lvl);
			trueRes = tempRes + random.randint(1, 25) * int(lvl);
			monAttk();
			fight();
		elif userIn == '3':
			global trueRes;
			trueRes = tempRes + random.randint(20, 40) * int(lvl);
			monAttk();
			fight();


	elif userIn == 'formorFlee':
		print('Fleeing and finding new monster');
		gameStatGen();

	elif userIn == '4':
		pot = random.randint(-300, 300) + int(tempLk);
		if pot >= 100:
			hpUp = 10 + random.randint(0, 10) * int(lvl);
			finHp = hpUp + tempHp;
			tempHp = finHp
			print('You have drank a health potion');
			print('You gained', hpUp, 'HP');
			print('Your HP is now', tempHp);
			attker = random.randint(1, 2);
			if attker == 1:
				print('The monster attacked before you got a chance');
				time.sleep(3);
				monAttk();
				fight();
			elif attker == 2:
				print('It is your turn to attack');
				time.sleep(3);
				fight();
		else:
			print('You could not pull out a potion before the monsters attack');
			attker = random.randint(1, 2)
			time.sleep(3)
			if attker == 1:
				print('You doged the attack and it is your turn to attack');
				time.sleep(3);
				fight();
			elif attker == 2:
				print('The attack hits you');
				time.sleep(3);
				monAttk();
				fight();

	elif userIn == '3':
		flee = int(tempLk) - int(monLuck) + random.randint(-200, 200);
		if flee > 100:
			print('Fleeing from the monster');
			time.sleep(5);
			gameStatGen();

		else:
			print('You failed to escape and the monster attacks');
			monAttk();
			fight();


	elif userIn == 'Dev Cheat 1234':
		global lvl;
		lvl = input('1L: ~ ');
		gameStatGen();


	elif userIn == 'Dev Cheat 09876':
		global tempAtk;
		global tempDef;
		global tempHp;
		global tempMag;
		global tempRes;
		global tempLk;
		global monAtk;
		global monDef;
		global monMag;
		global monRes;
		global monHp;
		global monLvl;
		global monLuck;
		global lvl;

		lvl = input('1l ~ ');
		tempAtk = int(input('tempAtk ~ '));
		tempDef = int(input('tempDef ~ '));
		tempHp = int(input('tempHp ~ '));
		tempMag = int(input('tempMag ~ '));
		tempRes = int(input('tempRes ~ '));
		tempLk = int(input('tempLk ~ '));
		monAtk = int(input('monAtk ~ '));
		monDef = int(input('monDef ~ '));
		monMag = int(input('monMag ~ '));
		monRes = int(input('monRes ~ '));
		monHp = int(input('monHp ~ '));
		monLuck = int(input('monLk ~ '));
		monLvl = int(input('monLvl ~ '));

		fight();

	elif userIn == 'Dev Cheat 101403':
		magCool = input('mag001 ~ ');
		fight();


	elif userIn == 'Dev Cheat 42069':
		print("""Dev Cheat Codes:
101403 - mag001
1234   - 1L
09876  - stat~
42069  - THIS""");

		time.sleep(20);
		fight();

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
		print('The monster attacks with it\'s fist');
		trueMonAtk = ((int(monAtk) - random.randint(0, 5)) + (random.randint(0, 5)* int(lvl))) - int(trueDef);
		time.sleep(3);
		print('The monster has delt', trueMonAtk, 'dammage');
		time.sleep(3);
		finTrueHp = int(temHp) - int(trueMonAtk);
		tempHp = finTrueHp;
		os.system(clear);

	elif monType == 2:
		temHp = tempHp;
		print('The monster attacks with it\'s club');
		trueMonAtk = ((int(monAtk) + int(lvl) + random.randint(0, 5) * int(lvl)) - int(trueDef));
		time.sleep(3);
		print('The monster has delt', trueMonAtk, 'dammage');
		time.sleep(3);
		finTrueHp = int(temHp) - int(trueMonAtk);
		tempHp = finTrueHp;
		os.system(clear);

	elif monType == 3:
		temHp = tempHp;
		print('The monster attacks with magic');
		trueMonAtk = (int(monMag) + int(lvl) + random.randint(10, 25) * int(lvl)) - int(trueRes);
		time.sleep(3);
		print('The monster has delt', trueMonAtk, 'dammage');
		time.sleep(3);
		finTrueHp = int(temHp) - int(trueMonAtk);
		tempHp = finTrueHp;
		os.system(clear);



	else:
		print('Huh');
		time.sleep(4);
		fight();


autoConfig();
verCheck();
