import os
import time

os.system('clear')

print('\033[1;91m',"""
     ____  _       _ _        _    ____ _            _
    |  _ \(_) __ _(_) |_ __ _| |  / ___| | ___   ___| | __
    | | | | |/ _` | | __/ _` | | | |   | |/ _ \ / __| |/ /
    | |_| | | (_| | | || (_| | | | |___| | (_) | (__|   <
    |____/|_|\__, |_|\__\__,_|_|  \____|_|\___/ \___|_|\_\
                      |___/\033[1;94m §Do not-copyright©	""")

print('\033[1;93m',"")
print("")

while True:
	localtime = time.localtime()
	result = time.strftime("  Current Time : %I:%M:%S %p", localtime)
	msg =("   @India Standard Time")
	print(result, end="", flush=True)
	print(msg, end="", flush=True)
	print("\r", end="", flush=True)
	time.sleep(1)
