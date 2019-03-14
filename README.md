# orca-installation-testing

![Version](https://img.shields.io/badge/version-1.5.1-blue.svg)
[![Build Status](https://travis-ci.org/UDST/orca-installation-testing.svg?branch=master)](https://travis-ci.org/UDST/orca-installation-testing)
[![Build status](https://ci.appveyor.com/api/projects/status/hxiyw9jo77e9pxuh?svg=true)](https://ci.appveyor.com/project/smmaurer/orca-installation-testing)

This repo uses Travis and Appveyor to test installation of Orca in many different environments.

- platforms: Linux, Mac, Windows
- package managers: pip, conda
- python versions: 2.7, 3.5, 3.6, 3.7

Click on the build status badges to see the full details.

This replicates the installation procedures that end users follow, in order to confirm that new releases have been distributed correctly and that they continue to work as dependencies are updated. This is separate from Orca's internal test suite, which uses a different installation procedure and doesn't cover as many environment combinations.

### Testing a new release

- publish the release on pip and conda
- in this repo, update the version number in `tests/test_version.py` and the badge URL in `README.md`
- trigger new builds manually in Travis and Appveyor
