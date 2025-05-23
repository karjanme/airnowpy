# AirNowPy Changelog

All notable changes to this project should be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## Release 2.3.1 [2025-03-26]
### Changed
- Bump `requests` from 2.32.0 to 2.32.2

## Release 2.3.0 [2024-06-12]
### Security
- CVE-2024-35195: Bump `requests` from 2.31.0 to 2.32.0

## Release 2.2.2 [2023-10-01]
### Fixed
- Bug with how timezones are applied to observation timestamps

## Release 2.2.1 [2023-10-01]
### Fixed
- Bug with how the observation date/time is read from the response

## Release 2.2.0 [2023-09-05]
### Changed
- Observation timestamps are now timezone aware

## Release 2.1.0 [2023-08-22]
### Security
- CVE-2023-32681: Bump `requests` from 2.22.0 to 2.31.0

## Release 2.0.0 [2020-07-14]
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
