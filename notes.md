
## iOS build info

Info could be found in: .ipa (.zip) / Payload / Info.plist

`Bundle Identifier` - `CFBundleIdentifier`
`Version number` - `CFBundleShortVersionString`
`Build number` - `CFBundleVersion`
`App Icon` - `CFBundleIcons > CFBundlePrimaryIcon > CFBundleIconFiles`


Tasks:
- Copy, rename and unzip the Bundle .ipa
- Get and parse Info.plist
- Code syntax and handling
- Write tests


Solution:
- Parsing the info.plist manually, however it was a wrong decision due to the custom format of the plist file
- I solved parsing for the given cases, however it doesn't handle every plist case

