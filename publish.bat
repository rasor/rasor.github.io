REM File 3
REM .\publish "some comment" # when called inside PS
call publishprivate.bat %1
call publishpublic.bat
ECHO Done
