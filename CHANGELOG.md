# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.2] - 2023-09-05
### Added
- [New function : logfile_initializer() is introduced anew](README.md#012-new-function--logfileinitializer-is-introduced-anew)
  - With default setting, it will put both of 'logging.log' and 'logging_oneline.log' back on the drawing board.

## [0.1.1] - 2023-09-05
### Changed
- [Modify the display format on console and .log files](README.md#011-modify-the-display-format-on-console-and-log-files)
  - Intended to improve the legibility of logging text  on console and in .log files. 

## [0.1.0] - 2023-08-14

### Added
- The initial version 
- Main function:
  -  (1) Make logger according to the external file like "logging.ini"
  -  (2) Make and Add Filter (is scheduled)

- This package contains below directories and files.

```
root
├── src
│   └── src\LoggingManager
│         ├── src\LoggingManager\LoggingManager.py
│         ├── src\LoggingManager\__init__.py
│         ├── src\LoggingManager\logging.ini
│         ├── src\LoggingManager\logging.log
│         ├── src\LoggingManager\logging_oneline.log
│         └── src\LoggingManager\logging_Specific.ini
│
├── CHANGELOG.md
├── LICENSE
├── README.md
└── requirements.txt
```

[unreleased]: https://github.com/NatsuSolar/LoggingManager/compare/0.1.2...HEAD
[0.1.2]: https://github.com/NatsuSolar/LoggingManager/compare/0.1.1...0.1.2
[0.1.1]: https://github.com/NatsuSolar/LoggingManager/compare/0.1.0...0.1.1
[0.1.0]: https://github.com/NatsuSolar/LoggingManager/releases/tag/0.1.0