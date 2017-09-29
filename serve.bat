REM File 1
REM .\serve # when called inside PS
REM
REM Build local
pelican content
cd output
REM Open browser to see pre-view
start "" "http://localhost:8000/"
REM Serve build content from \output\
python -m pelican.server
REM Ctrl-C to quit
