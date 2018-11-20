import unittest
import os
from ipa_analyzer import IosBuildInfo, IosIpa

class TestBuildInfo(unittest.TestCase):
	"""
	Test IosIpa class
	"""

	def test_all_values_are_defined(self):
		"""
		Tests IPA initial settings
		"""
		testIpa = IosIpa(os.getcwd() + '/test_data/test_app.ipa')

		self.assertEqual(testIpa.buildInfo.bundleId, 'CsabaSzabo.ios-simple-objc')
		self.assertEqual(testIpa.buildInfo.versionNumber, '1.0')
		self.assertEqual(testIpa.buildInfo.buildNumber, '1')
		self.assertEqual(testIpa.buildInfo.appIconName, 'AppIcon60x60')

		testIpa.delete_tmp()

	def test_no_images(self):
		"""
		Tests IPA with no image
		"""
		testIpa = IosIpa(os.getcwd() + '/test_data/test_app_2.ipa')

		self.assertEqual(testIpa.buildInfo.bundleId, 'com.CsabaSzabo.code-sign-test')
		self.assertEqual(testIpa.buildInfo.versionNumber, '1.0')
		self.assertEqual(testIpa.buildInfo.buildNumber, '1')
		self.assertEqual(testIpa.buildInfo.appIconName, None)

		testIpa.delete_tmp()

	def test_bigger_numbers(self):
		"""
		Tests real build and version numbers
		"""
		testIpa = IosIpa(os.getcwd() + '/test_data/test_changedBuildNumber.ipa')

		self.assertEqual(testIpa.buildInfo.bundleId, 'CsabaSzabo.ios-simple-objc')
		self.assertEqual(testIpa.buildInfo.versionNumber, '5.43')
		self.assertEqual(testIpa.buildInfo.buildNumber, '201811191621')
		self.assertEqual(testIpa.buildInfo.appIconName, 'AppIcon60x60')

		testIpa.delete_tmp()

	def test_no_version_number(self):
		"""
		Tests IPA with no version number
		"""
		testIpa = IosIpa(os.getcwd() + '/test_data/test_no_versionNumber.ipa')

		self.assertEqual(testIpa.buildInfo.bundleId, 'CsabaSzabo.ios-simple-objc')
		self.assertEqual(testIpa.buildInfo.versionNumber, None)
		self.assertEqual(testIpa.buildInfo.buildNumber, '1')
		self.assertEqual(testIpa.buildInfo.appIconName, 'AppIcon60x60')

		testIpa.delete_tmp()

	def test_unexpected_CFBundleIconFiles_format(self):
		"""
		Tests IPA with no version number
		"""
		testIpa = IosIpa(os.getcwd() + '/test_data/test_unexpected-CFBundleIconFiles.ipa')

		self.assertEqual(testIpa.buildInfo.bundleId, 'CsabaSzabo.ios-simple-objc')
		self.assertEqual(testIpa.buildInfo.versionNumber, '1.0')
		self.assertEqual(testIpa.buildInfo.buildNumber, '1')
		self.assertEqual(testIpa.buildInfo.appIconName, None)

		testIpa.delete_tmp()


if __name__ == '__main__':
	unittest.main()
