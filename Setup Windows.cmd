@echo off
title AisleSense - First-time setup
cd /d "%~dp0"
py -3.13 scripts\setup.py
if errorlevel 1 (
  echo Setup did not finish. Read README.md and the error above.
  pause
  exit /b 1
)
echo Ready. Open Start Business Dashboard.cmd.
pause
