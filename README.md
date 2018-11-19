# Task
https://gist.github.com/godrei/e8b1a90919c253f6db94ed08c361961d

# Solution
This repository contains the solution, which was written in Python3, as that's the most comfortable scripting language for me.

## Private or Public
I made this repository private, as I wouldn't publicate your Trial Day task. Otherwise, I would made this repository public.

## iOS IPA info

An `.ipa` file is basically a `.zip` file, containing the app `Payload`.

### IPA File structure

Info could be found in: `IPA_NAME.ipa (.zip) / Payload / APP_NAME.app / Info.plist`

- `Bundle Identifier` - `CFBundleIdentifier`
- `Version number` - `CFBundleShortVersionString`
- `Build number` - `CFBundleVersion`
- `App Icon` - `CFBundleIcons > CFBundlePrimaryIcon > CFBundleIconFiles`

**Tasks:**
- Copy, rename and unzip the Bundle .ipa
- Get and parse Info.plist
- Write data and ask for usage

**Solution:**
- Parsing the info.plist manually, however it was a wrong decision due to the custom format of the plist file
- I solved parsing for the given cases, however it doesn't handle every plist case

Now I would try to use IPA analysers like:
- https://github.com/bitrise-io/ipa_analyzer
- https://github.com/mogui/pyipa
