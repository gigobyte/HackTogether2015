commands = {
	'take-picture': 'take a picture',
	'save-computer': 'save it to computer',
	'save-pc': 'save it to pc',
	'show-sms': 'show sms',
	'show-msg': 'show messages',
	'take-screenshot': 'take screenshot',
	'record-screen': 'record screen for seconds',
	'get-contacts': 'get contacts'

}

adb_commands = {
	'tcpip': 'platform-tools\\adb tcpip 5556',
	'netcfg': 'platform-tools\\adb shell netcfg',
	'connect': 'platform-tools\\adb connect ',
	'devices': 'platform-tools\\adb devices -l',
	'kill-server': 'platform-tools\\adb kill-server',
	'start-server': 'platform-tools\\adb start-server',
	'take-picture': 'platform-tools\\adb shell "am start -a android.media.action.STILL_IMAGE_CAMERA" && sleep 2 && platform-tools\\adb shell "input keyevent 27"',
	'list': 'platform-tools\\adb shell "ls / -R"',
	'open-movies': 'platform-tools\\adb shell "ls /sdcard/Movies -R"',
	'open-pictures': 'platform-tools\\adb shell "ls /sdcard/DCIM/Camera -R"',
	'open-music': 'platform-tools\\adb shell "ls /sdcard/Music -R"',
	'pull': 'platform-tools\\adb pull ',
	'transfer-sms': 'platform-tools\\adb shell "su cat "/data/data/com.android.providers.telephony/databases/mmssms.db" > /sdcard/sms.db"',
	'take-screenshot' : 'platform-tools\\adb shell "screencap /sdcard/screen.png"',
	'take-screenrecord' : 'platform-tools\\adb shell "screenrecord /sdcard/screen.mp4"',
	'accept-call': 'platform-tools\\adb shell input keyevent 5',
	'decline-call': 'platform-tools\\adb shell input keyevent 6',
	'check-callstate': 'platform-tools\\adb shell dumpsys telephony.registry | grep "mCallState"',
	'check-callnumber': 'platform-tools\\adb shell dumpsys telephony.registry | grep "mCallIncomingNumber"',
	'db' :  'platform-tools\\adb shell "content query --uri "
}
