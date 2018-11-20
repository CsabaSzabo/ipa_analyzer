# Problem to solve
For App Store iOS app submission, you have to export an `.ipa` file, which could be uploaded to the App Store.
Validating information from this `.ipa` file is not easy by hand. This script solves this problem.

It lists the most important values of a `.ipa` file:

| Value             | .ipa value key                                          | Notes                                        |
|-------------------|---------------------------------------------------------|----------------------------------------------|
| Bundle Identifier | CFBundleIdentifier                                      | The ID of the app                            |
| Version number    | CFBundleShortVersionString                              | This is the visible version number for users |
| Build number      | CFBundleVersion                                         | This is the internal build number of the app |
| App Icon name     | CFBundleIcons > CFBundlePrimaryIcon > CFBundleIconFiles | App Store app icon name                      |

## How to use it

Running the solution:
```python
python3 ipa_analyzer.py PATH_TO_IPA
```

## Contribution guideline

- Clone the repository
- Run tests `python3 test_ipa_analyzer.py`
- Change code and update tests
- Submit a Pull request


## Similar projects 

- https://github.com/bitrise-io/ipa_analyzer
- https://github.com/mogui/pyipa
