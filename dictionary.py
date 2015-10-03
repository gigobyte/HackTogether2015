commands = {
	'take-picture': 'take a picture'
}

adb_commands = {
	'tcpip': 'platform-tools\\adb.exe tcpip 5556',
	'netcfg': 'platform-tools\\adb.exe shell netcfg',
	'connect': 'platform-tools\\adb.exe connect ',
	'devices': 'platform-tools\\adb.exe devices -l',
	'kill-server': 'platform-tools\\adb.exe kill-server',
	'start-server': 'platform-tools\\adb.exe start-server',
	'camera-image-capture': 'platform-tools\\adb shell "am start -a android.media.action.IMAGE_CAPTURE"',
	'take-picture': 'platform-tools\\adb shell "input keyevent KEYCODE_CAMERA"'
}