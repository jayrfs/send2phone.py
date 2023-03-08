import argparse
import subprocess
import win10toast

parser = argparse.ArgumentParser(description="Push files to Android device using ADB.")
parser.add_argument("filepaths", metavar="filepath", nargs="+", help="List of filepaths to push to /sdcard")
args = parser.parse_args()

for filepath in args.filepaths:
    adb_command = ["adb", "push", filepath, "/sdcard"]
    print(f"Running command: {' '.join(adb_command)}")
    result = subprocess.run(adb_command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
win10toast.ToastNotifier().show_toast("send2phone.py", "Transfer complete :)",duration=3)