#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os				# file handling
import shutil			# file handling2
import zipfile			# zipping
import argparse			# arguments

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

def print_bold(text):
	print(color.BOLD + text + color.END)

def print_info(build_infos, ipa_name):

	print()
	print('+------------------------------------------------------------------------------+')
	print('| IPA Analyzer - '+ipa_name+'                                                                ')
	print('+------------------------------------------------------------------------------+')

	bundleId = build_infos.bundleId
	versionNum = build_infos.versionNumber
	buildNum = build_infos.buildNumber
	appIconName = build_infos.appIconName

	if appIconName == None:
		appIconName = "No app icon was found"

	print('Bundle Identifier: '+bundleId)
	print('Version number: '+versionNum)
	print('Build number: '+buildNum)
	print('App icon name: '+appIconName)

	print('+------------------------------------------------------------------------------+')
	print()


# --------------------
# Core iOS IPA classes
# --------------------

class IosBuildInfo:

	def __init__(self, bundleId, versionNumber, buildNumber, appIconName):
		self.bundleId = bundleId
		self.versionNumber = versionNumber
		self.buildNumber = buildNumber
		self.appIconName = appIconName

class IosIpa:

	def __init__(self, ipa_path):
		
		self.path = ipa_path
		self.name = ipa_path.rsplit('/', 1)[1]

		self.tmp_dir = os.getcwd() + '/_tmp/ipa_' + self.name
		self.unzip()

		self.infoplist_filepath = self.get_info_plist()
		self.buildInfo = self.get_build_infos()
		self.iconsArray = self.get_icon_files()


	# Unzip IPA to TMP directory
	def unzip(self):
		zip_ref = zipfile.ZipFile(self.path, 'r')
		zip_ref.extractall(self.tmp_dir)
		zip_ref.close()


	# Delete TMP directory
	def delete_tmp(self):
		shutil.rmtree(os.getcwd() + '/_tmp/')


	# Get info plist filepath
	def get_info_plist(self):

		payload_dir = self.tmp_dir + '/Payload'
		
		# find file
		infoplist_filepath = None

		for app_file in os.listdir(payload_dir):
			if app_file.endswith('.app'):
				for app_subfile in os.listdir(payload_dir + '/' + app_file):
					if app_subfile == 'Info.plist':
						infoplist_filepath = payload_dir + '/' + app_file + '/' + app_subfile

		return infoplist_filepath

	# Get build infos as IosBuildInfo object
	def get_build_infos(self):

		# Required params
		bundleIdString = None
		versionNumber = None
		buildNumber = None
		appIcon = None

		# Get plist file
		plist_content = None
		with open(self.infoplist_filepath) as plist:
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

	# Return an array of App icon file names
	def get_icon_files(self):

		payload_dir = self.tmp_dir + '/Payload'
		
		# find files
		icon_filepath_array = []

		if self.buildInfo.appIconName == None:
			return icon_filepath_array

		for app_file in os.listdir(payload_dir):
			if app_file.endswith('.app'):
				for app_subfile in os.listdir(payload_dir + '/' + app_file):
					if app_subfile.startswith(self.buildInfo.appIconName):
						appicon_filepath = payload_dir + '/' + app_file + '/' + app_subfile
						icon_filepath_array.append(appicon_filepath)

		return icon_filepath_array



# --------------------
# Plist file parser extension
# --------------------

# Returning content form a <string>ABC</string> plist line
def get_content_from_string_xml(line):

	if 'string' in line:
		content = line.replace('<string>', '')
		content = content.replace('</string>', '')
		content = content.replace('\n', '')
		content = content.replace(' ', '')	
		return content
	else:
		return None

# --------------------
# Main
# --------------------

def main():

	# Process arguments
	ipafile_path = ''

	parser = argparse.ArgumentParser()
	parser.add_argument("ipapath", help="Absolute Path of the IPA file")
	args = parser.parse_args()
	ipafile_path = args.ipapath

	# Create IPA
	ipa = IosIpa(ipa_path = ipafile_path)
	
	# Print and Ask
	print_info(ipa.buildInfo, ipa.name)
	
	# Delete tmp folder
	ipa.delete_tmp()
	

if __name__ == '__main__':
	main()