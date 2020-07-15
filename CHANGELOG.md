# AirNowPy Changelog

All notable changes to this project should be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased
### Added
- The ability to access all data contained within an observation
### Changed
- The way data is accessed from an observation

## Release 1.0.0 [2020-06-24]
### Added
- Type hints per PEP 484
- Ability to specify distance as a parameter to the API functions
### Changed
- Omit the distance from the webservice payload if not provided
- Stop converting the observation timestamp from local to UTC
### Fixed
- Treat 5-digit zip codes beginning with 0 as valid

## Release 0.1.2 [2020-06-12]
### Fixed
- Export the modules of the package

## Release 0.1.1 [2020-04-16]
### Fixed
- Package name to be all lowercase so it adheres to PEP 8

## Release 0.1.0 [2020-04-15]
### Added
- Initial release of project
