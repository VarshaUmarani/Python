import sys
import platform
import os

def main():
	v = sys.version_info
	print("Current Python Version is : {}.{}.{}".format(*v))
	print("Current Python Version is :",platform.python_version())
	print(sys.platform)
	print(os.name)
	print(os.getcwd())

if __name__ == "__main__":
	main()