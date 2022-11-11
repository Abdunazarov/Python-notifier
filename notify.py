import subprocess, time, datetime

from playsound import playsound


def pamadir(d):
	start_time = datetime.datetime.now()
	end_time = start_time + datetime.timedelta(minutes=d)

	if len(str(end_time.minute)) == 1:
		minute = '0' + str(end_time.minute)
	else:
		minute = end_time.minute

	start_time_minute = start_time.minute

	if len(str(start_time_minute)) < 2:
		start_time_minute = '0' + str(start_time_minute)


	print("Started at \033[1m{}:{}\033[0m, will end at \033[1m{end_h}:{end_m}\033[0m ".format(
		start_time.hour, start_time_minute, end_h=end_time.hour, end_m=minute))
	
	time.sleep(d * 60)
	subprocess.Popen(['xdg-open', '/home/diyor/Dev/Notify/stop.jpg'])
	playsound('sound.wav')


duration = int(input("Time: "))
pamadir(duration)

