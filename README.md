# LoggingManager

Simplify logger making and management.

    Main function:
        1. Make logger according to the external ini-file like "logging.ini"
        2. Make and Add Filter(be scheduled)


# DEMO
**list0806_2.py**  
- Source book: Introduction To GameDevelopment In Python  
  - [Pythonでつくる ゲーム開発 入門講座](http://www.sotechsha.co.jp/pc/html/1239.htm)
- This code is the modified version of the part of `list0806_2.py`, in the above source book.

## DEMO CODE : list0806_2.py
```python
import tkinter
import tkinter.messagebox

import LoggingManager


logger = LoggingManager.LoggingManager().logger_maker(logger_lv='debug', logger_name='logger-1.list0806.2')
    
YUKA = 0
NUM_YUKA = 1

# Line 83, 84
logger.debug('rooting start point')
logger.debug(f'YUKA: {YUKA} NUM_YUKA: {NUM_YUKA}')

# Line 89, 92
logger.debug(f'YUKA: {YUKA} NUM_YUKA: {NUM_YUKA}')
logger.debug(f'YUKA: {YUKA} NUM_YUKA: {NUM_YUKA}')

# Line 117-123
logger.info('The maze description starts')
for row_num in range(len(maze)):
    for col_num in range(len(maze[row_num])):
        if maze[row_num][col_num] == 1:
            canvas.create_rectangle(col_num * 80, row_num * 80, col_num * 80 + 79, row_num * 80 + 79,
                                    fill="skyblue", width=0)
logger.info('The maze description finished')

```

## logging_oneline.log   : Focus on legibility

The below displaying is that of over version [0.1.1]
```
2023-08-17 16:01:45,846 - [DEBUG] rooting start point  --> ( 83 ) logger-1.list0806.2
2023-08-17 16:01:45,846 - [DEBUG] YUKA: 0 NUM_YUKA: 1  --> ( 84 ) logger-1.list0806.2
2023-08-17 16:01:45,846 - [DEBUG] YUKA: 0 NUM_YUKA: 1  --> ( 89 ) logger-1.list0806.2
2023-08-17 16:01:45,846 - [DEBUG] YUKA: 0 NUM_YUKA: 1  --> ( 92 ) logger-1.list0806.2
2023-08-17 16:01:45,846 - [INFO] The maze description starts  --> ( 117 ) logger-1.list0806.2
2023-08-17 16:01:45,846 - [INFO] The maze description finished  --> ( 123 ) logger-1.list0806.2
```

## logging.log : More details

The below displaying is that of over version [0.1.1]
```
--------------------------------------------------------------------------------
[DEBUG] L 83 <list0806_2.py> [2023-08-17 16:01:45,846]
[MSG] rooting start point
--------------------------------------------------------------------------------
--LOGGER_NAME:   logger-1.list0806.2
--FUNCTION:      <module>
--MODULE:        list0806_2
--PROCESS_ID:    25296
--PROCESS_NAME:  MainProcess
--THREAD_ID:     14480
--THREAD_NAME:   MainThread
--TIME_TO_OCCUR: 48
--FILE_PASS:     C:\Users\Username\Projectname\c\Lesson\Chapter8\list0806_2.py
--------------------------------------------------------------------------------
[DEBUG] L 84 <list0806_2.py> [2023-08-17 16:01:45,846]
[MSG] YUKA: 0 NUM_YUKA: 1
--------------------------------------------------------------------------------
--LOGGER_NAME:   logger-1.list0806.2
--FUNCTION:      <module>
--MODULE:        list0806_2
--PROCESS_ID:    25296
--PROCESS_NAME:  MainProcess
--THREAD_ID:     14480
--THREAD_NAME:   MainThread
--TIME_TO_OCCUR: 48
--FILE_PASS:     C:\Users\Username\Projectname\IntroductionToGameDevelopmentInPython\Lesson\Chapter8\list0806_2.py
```

# Features
Plan to add

# Requirement
 
"LoggingManger" (ver.0.1.0) doesn't require third-party Library.
Probably, it works on over Python3.7.x Environment.

* Python 3.7.x
 
# Installation
Copy & Paste the below 4 files of LoggingManager directory to each directory you want to get logging.
- LoggingManager.py
- logging.ini
- logging_oneline.log
- logging.log  

If you need to switch default logging setting to Specific one, you can Copy & Paste `logging_Specific.ini` and edit it.


# Usage
## [0.1.0] The Initial update

        1. Make logger according to the external ini-file like "logging.ini"

### Use Case : src/ModuleName.py
```python
import LoggingManager

logger = LoggingManager.LoggingManager()
logger = logger.logger_maker(log_lv='Debug', logger_name='logger-1.src.ModuleName')

def main():
  logger.debug('test')
  a = 15
  x = 10 * a
  logger.info(f"When a={a} and x=10*a, x={x}")

if __name__ == '__main__':
    main()
```
### Output on Console
```bash
2023-09-04 23:11:03,265 - INFO:logger-1.src.ModuleName:When a=15 and x=10*a, x=150
```
#### __ Why only an INFO log is on console?
The hierarchy of logging levels is below:
```
CRITICAL > ERROR > WARNING >  INFO > DEBUG
```
In `logging.ini`, the `level=` of `streamHandler` is set to `info`.  
The `streamHandler` is the handler which rules the description on console, so only an 'INFO' log is on console.

### Output in logging_oneline.log : Focus on legibility
```
2023-09-04 23:11:03,265 - DEBUG:logger-1.src.ModuleName:test
2023-09-04 23:11:03,265 - INFO:logger-1.src.ModuleName:When a=15 and x=10*a, x=150
```

### Output in logging.log : More details
```
--------------------------------------------------------------------------------
DEBUG: L.103 <main.py> [2023-09-04 23:11:03,265]
MSG: test
--------------------------------------------------------------------------------
--LOGGER_NAME:   logger-1.src.main
--FUNCTION:      main
--MODULE:        ModuleName
--PROCESS_ID:    11856
--PROCESS_NAME:  MainProcess
--THREAD_ID:     8104
--THREAD_NAME:   MainThread
--TIME_TO_OCCUR: 43
--FILE_PASS:     C:\Users\Username\ProjectName\src\ModuleName\main.py
--------------------------------------------------------------------------------
INFO: L.106 <main.py> [2023-09-04 23:11:03,265]
MSG: When a=15 and x=10*a, x=150
--------------------------------------------------------------------------------
--LOGGER_NAME:   logger-1.src.main
--FUNCTION:      main
--MODULE:        ModuleName
--PROCESS_ID:    11856
--PROCESS_NAME:  MainProcess
--THREAD_ID:     8104
--THREAD_NAME:   MainThread
--TIME_TO_OCCUR: 43
--FILE_PASS:     C:\Users\Username\ProjectName\src\ModuleName\main.py
```
## [0.1.1] Modify the display format on console and .log files
The part of `logging.log` changed.  
It is Intended to improve the legibility of logging text  on console and in .log files. 
### Comparing between 0.1.0 → 0.1.1
The changes between 0.1.0 and 0.1.1 are showed below.
#### Output on console & logging_oneline.log 
A point worthy of special mention is inserting the "line number" of the line had called the logger.
```
[0.1.0]
2023-09-04 23:11:03,265 - DEBUG:logger-1.src.ModuleName:test
```
```
[0.1.1]
2023-09-04 23:11:03,265 - [DEBUG] test  --> ( 103 ) logger-1.src.ModuleName
```
#### Output in logging.log 
```
[0.1.0]
--------------------------------------------------------------------------------
DEBUG: L.103 <main.py> [2023-09-04 23:11:03,265]
MSG: test
--------------------------------------------------------------------------------
--LOGGER_NAME:   logger-1.src.main
--FUNCTION:      main
--MODULE:        ModuleName
--PROCESS_ID:    11856
--PROCESS_NAME:  MainProcess
--THREAD_ID:     8104
--THREAD_NAME:   MainThread
--TIME_TO_OCCUR: 43
--FILE_PASS:     C:\Users\Username\ProjectName\src\ModuleName\main.py
```
```
[0.1.1]
--------------------------------------------------------------------------------
[DEBUG] L 103 <main.py> [2023-09-04 23:11:03,265]
[MSG] test
--------------------------------------------------------------------------------
--LOGGER_NAME:   logger-1.src.main
--FUNCTION:      main
--MODULE:        ModuleName
--PROCESS_ID:    11856
--PROCESS_NAME:  MainProcess
--THREAD_ID:     8104
--THREAD_NAME:   MainThread
--TIME_TO_OCCUR: 43
--FILE_PASS:     C:\Users\Username\ProjectName\src\ModuleName\main.py
--------------------------------------------------------------------------------
```

## [0.1.2] New function : logfile_initializer is introduced anew
- logfile_initializer() is introduced anew  
  - With default setting, it will put both of 'logging.log' and 'logging_oneline.log' back on the drawing board.
  - With `False` is assigned to `oneline` or `detail`,both or a hand of these log-files will keep the log-text and new logs to be added on the end of log-files continually.
  - Use case is below :
```python
""" main.py """

import LoggingManager


LOGGING_MODE = True

logger = LoggingManager.LoggingManager()

if LOGGING_MODE:
    LoggingManager.logfile_initializer(oneline=True, detail=True,
                                       online_path='./logging_oneline.log',
                                       detail_path='./logging.log')
    logger = logger.logger_maker(log_lv='Debug', logger_name='logger-1.main')
else:
    logger = logger.logger_maker(logger_name='null')
```
- Description of above code example.
  - This code is recommend to put on the top of each python modules.
    -  Identifiers of `logger_name` require [tree-structure](https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial) based on that of inter-module relationship.
  - When `LOGGING_MODE` is `True`, both of log-files will be back to whole blank ones and `logger-1.main` will set to `logger` with `Debug` logging level.
  - When `LOGGING_MODE` is `False`, logger `null` will set to `logger` and logging on this `main.py` will not work.

# Note
 
I don't test the Environments under Linux and Mac.
 
# Author

* Auther: **Aoi Natsuki (蒼井 夏樹)**
* Work: [Blau Tine](https://sites.google.com/view/blau-tinte)
* E-mail: blautinte8`☆`gmail.com  
_- - - - - > Replace '☆' for '@'_
        

* Twitter ( or "X")
    <dl>
    <dt>Auther</dt>
     <dd><a href="https://twitter.com/Aoi_NatsuSolar">Aoi Natsuki(蒼井 夏樹)</a></dd>
     <dt>Workplace</dt>
     <dd><a href="https://twitter.com/BlauTinte">Blau Tinte</a></dd>
    </dl> 
* LinkedIn: [Aoi Natsuki](https://www.linkedin.com/in/aoi-natsuki)
 
# License
" LoggingManager" is under [MIT license](https://opensource.org/license/mit).

# Version
[CHANGELOG.md](CHANGELOG.md)  

[unreleased]: https://github.com/NatsuSolar/LoggingManager/compare/v0.1.0...HEAD
[0.1.2]: https://github.com/NatsuSolar/LoggingManager/releases/tag/0.1.2
[0.1.1]: https://github.com/NatsuSolar/LoggingManager/releases/tag/0.1.1
[0.1.0]: https://github.com/NatsuSolar/LoggingManager/releases/tag/0.1.0
  
  