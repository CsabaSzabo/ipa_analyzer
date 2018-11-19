#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os				# file handling
import zipfile			# zipping
import shutil			# file handling2
import xmltodict		# xml parsing
from PIL import Image 	# image showing


# --------------------
# Printing functions and classes
# --------------------
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def print_info(build_infos, ipa_name, icon_array):

	print()
	print('+------------------------------------------------------------------------------+')
	print('| IPA Analyser - '+ipa_name+'                                                                ')
	print('+------------------------------------------------------------------------------+')

	bundleId = build_infos.bundleId
	versionNum = build_infos.versionNumber
	buildNum = build_infos.buildNumber
	appIconName = build_infos.appIconName

	if appIconName == None:
		appIconName = "No app was icon"

	print('Bundle Identifier: '+bundleId)
	print('Version number: '+versionNum)
	print('Build number: '+buildNum)
	print('App icon name: '+appIconName)
	
	if len(icon_array):
		print('App icons:')
		for icon_path in icon_array:
			print('   '+ icon_path)
	

	print('+------------------------------------------------------------------------------+')
	print()

def yes_no_question(question):
	# from https://gist.github.com/garrettdreyfus/8153571
	print(color.BOLD + 'QUESTION' + color.END)

	reply = str(input(question+' (y/n): ')).lower().strip()
	if reply[0] == 'y':
		return True
	if reply[0] == 'n':
		return False
	else:
		return yes_no_question("Uhhhh... please enter ")

def print_bold(text):
	print(color.BOLD + text + color.END)


# --------------------
# File handling functions
# --------------------

def unzip_ipa(file_path, zip_directory):

	zip_ref = zipfile.ZipFile(file_path, 'r')
	zip_ref.extractall(zip_directory)
	zip_ref.close()

def delete_tmp(directory_path):

	shutil.rmtree(os.getcwd() + '/_tmp/')

# --------------------
# Core logic functions
# -------------------- 

class IosBuildInfo:

	def __init__(self, bundleId, versionNumber, buildNumber, appIconName):
		self.bundleId = bundleId
		self.versionNumber = versionNumber
		self.buildNumber = buildNumber
		self.appIconName = appIconName

class IosIpaInfo:

	def __init__(self, ipa_name, ipa_path):
		self.name = ipa_name
		self.path = ipa_path




def get_info_plist(ipa_dir_path):

	payload_dir = ipa_dir_path + '/Payload'
	
	# find file
	infoplist_filepath = None

	for app_file in os.listdir(payload_dir):
		if app_file.endswith('.app'):
			for app_subfile in os.listdir(payload_dir + '/' + app_file):
				if app_subfile == 'Info.plist':
					infoplist_filepath = payload_dir + '/' + app_file + '/' + app_subfile

	return infoplist_filepath

def get_icon_files(ipa_dir_path, icon_name):

	payload_dir = ipa_dir_path + '/Payload'
	
	# find files
	icon_filepath_array = []

	if icon_name == None:
		return icon_filepath_array

	for app_file in os.listdir(payload_dir):
		if app_file.endswith('.app'):
			for app_subfile in os.listdir(payload_dir + '/' + app_file):
				if app_subfile.startswith(icon_name):
					appicon_filepath = payload_dir + '/' + app_file + '/' + app_subfile
					icon_filepath_array.append(appicon_filepath)

	return icon_filepath_array

# Returning content form a <string>ABC</string> plist line
def get_content_from_string_xml(line):

	content = line.split('<string>')[1]
	content = content.split('</string>')[0]
	return content


def get_build_infos(plist_path):

	# Required params
	bundleIdString = None
	versionNumber = None
	buildNumber = None
	appIcon = None

	# Get plist file
	plist_content = None
	with open(plist_path) as plist:
		plist_content = plist.readlines()
	
	# Find the required info
	index = 0;
	for plist_line in plist_content:

		if "CFBundleIdentifier" in plist_line:
			bundleIdString = get_content_from_string_xml(plist_content[index + 1])

		if "CFBundleShortVersionString" in plist_line:
			versionNumber = get_content_from_string_xml(plist_content[index + 1])

		if "CFBundleVersion" in plist_line:
			buildNumber = get_content_from_string_xml(plist_content[index + 1])

		if "CFBundleIconFiles" in plist_line:
			appIcon = get_content_from_string_xml(plist_content[index + 2])

		index = index + 1

	return IosBuildInfo(bundleIdString, versionNumber, buildNumber, appIcon)


def process_ipa(ipa):

	tmp_dir = os.getcwd() + '/_tmp/ipa_' + ipa.name

	# Find infos
	unzip_ipa(file_path = ipa.path, zip_directory = tmp_dir)
	infoplist_path = get_info_plist(ipa_dir_path = tmp_dir)
	build_infos = get_build_infos(infoplist_path)
	icon_array = get_icon_files(ipa_dir_path = tmp_dir, icon_name = build_infos.appIconName)

	# Print and Ask
	print_info(build_infos, ipa.name, icon_array)
	if yes_no_question("Would you like to release the app with these settings?"):
		print_bold('ACTION')
		print("Woooo - Your App is released.")
	else:
		print_bold('ACTION')
		print("Woooo - We saved your release. Please change the ipa and release it again.")

	# Delete tmp folder
	delete_tmp(tmp_dir)


def main():

	# Find files in directory
	ipa_directory = os.getcwd() + '/trial_excercise/'

	# Process .ipa files
	for ipa_file in os.listdir(ipa_directory):
		if ipa_file.endswith('.ipa'):
			ipa_info = IosIpaInfo(ipa_name = ipa_file, ipa_path = ipa_directory + '/' + ipa_file)
			process_ipa(ipa = ipa_info)
	

if __name__ == '__main__':
	main()