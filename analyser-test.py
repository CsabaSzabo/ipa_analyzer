import unittest
from analyser import IosBuildInfo, IosIpa

class TestBuildInfo(unittest.TestCase):
	"""
	Test class to test ``get_build_infos`` function
	"""

	def test_all_values_are_defined(self):
		"""
		Tests IPA initial settings
		"""
		testIpa = IosIpa('app.ipa', '/Users/szabocsaba/DEV/bitrise-trialday/trial_excercise/app.ipa')

		self.assertEqual(testIpa.buildInfo.bundleId, 'Bitrise.ios-simple-objc')
		self.assertEqual(testIpa.buildInfo.versionNumber, '1.0')
		self.assertEqual(testIpa.buildInfo.buildNumber, '1')
		self.assertEqual(testIpa.buildInfo.appIconName, 'AppIcon60x60')

		testIpa.delete_tmp()

	def test_no_images(self):
		"""
		Tests IPA with no image
		"""
		testIpa = IosIpa('app_2.ipa', '/Users/szabocsaba/DEV/bitrise-trialday/trial_excercise/app_2.ipa')

		self.assertEqual(testIpa.buildInfo.bundleId, 'com.bitrise.code-sign-test')
		self.assertEqual(testIpa.buildInfo.versionNumber, '1.0')
		self.assertEqual(testIpa.buildInfo.buildNumber, '1')
		self.assertEqual(testIpa.buildInfo.appIconName, None)

		testIpa.delete_tmp()

	def test_bigger_numbers(self):
		"""
		Tests real build and version numbers
		"""
		testIpa = IosIpa('test_changedBuildNumber.ipa', '/Users/szabocsaba/DEV/bitrise-trialday/test_data/test_changedBuildNumber.ipa')

		self.assertEqual(testIpa.buildInfo.bundleId, 'Bitrise.ios-simple-objc')
		self.assertEqual(testIpa.buildInfo.versionNumber, '5.43')
		self.assertEqual(testIpa.buildInfo.buildNumber, '201811191621')
		self.assertEqual(testIpa.buildInfo.appIconName, 'AppIcon60x60')

		testIpa.delete_tmp()

	def test_no_version_number(self):
		"""
		Tests IPA with no version number
		"""
		testIpa = IosIpa('test_no_versionNumber.ipa', '/Users/szabocsaba/DEV/bitrise-trialday/test_data/test_no_versionNumber.ipa')

		self.assertEqual(testIpa.buildInfo.bundleId, 'Bitrise.ios-simple-objc')
		self.assertEqual(testIpa.buildInfo.versionNumber, None)
		self.assertEqual(testIpa.buildInfo.buildNumber, '1')
		self.assertEqual(testIpa.buildInfo.appIconName, 'AppIcon60x60')

		testIpa.delete_tmp()

	def test_unexpected_CFBundleIconFiles_format(self):
		"""
		Tests IPA with no version number
		"""
		testIpa = IosIpa('test_unexpected-CFBundleIconFiles.ipa', '/Users/szabocsaba/DEV/bitrise-trialday/test_data/test_unexpected-CFBundleIconFiles.ipa')

		self.assertEqual(testIpa.buildInfo.bundleId, 'Bitrise.ios-simple-objc')
		self.assertEqual(testIpa.buildInfo.versionNumber, '1.0')
		self.assertEqual(testIpa.buildInfo.buildNumber, '1')
		self.assertEqual(testIpa.buildInfo.appIconName, None)

		testIpa.delete_tmp()


if __name__ == '__main__':
	unittest.main()
