commands = {
	'take-picture': 'take a picture',
	'save-computer': 'save it to computer',
	'save-pc': 'save it to pc'
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
	'sms-dir': '/data/data/com.android.providers.telephony/databases/mmssms.db '

}