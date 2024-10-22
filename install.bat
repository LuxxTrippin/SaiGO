@echo off
setlocal

:OSChoice
echo Choose your operating system:
echo 1. Windows
echo 2. Linux
echo 3. MacOS
echo 4. I Have Python Installed Already
set /p "os_choice=Enter your choice (1, 2, 3, Or 4): "

if "%os_choice%"=="1" goto Windows
if "%os_choice%"=="2" goto Linux
if "%os_choice%"=="3" goto MacOS
if "%os_choice%"=="4" goto SkipPythonInstall

echo Invalid choice, exiting...
exit /b

:Windows
echo.
echo Downloading Python 3.11.0 for Windows...
start "" "https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe"
set "file_name=python-3.11.0-amd64.exe"
goto WaitInstall

:Linux
echo Downloading Python 3.11.0 for Linux...
start "" "https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe"
set "file_name=python-3.11.0-amd64.exe"
goto WaitInstall

:MacOS
echo Downloading Python 3.11.0 for MacOS...
start "" "https://www.python.org/ftp/python/3.11.0/python-3.11.0-macos11.pkg"
set "file_name=python-3.11.0-macos11.pkg"
goto WaitInstall

:WaitInstall
echo Waiting for download to complete...

:: Set the downloads path, adjust if necessary
set "downloads_path=%USERPROFILE%\Downloads"

:CheckFile
if exist "%downloads_path%\%file_name%" (
    echo Download complete! Opening installer...
    start "" "%downloads_path%\%file_name%"
    echo.
    echo Please make sure any other version of python is UNINSTALLED before continuing!
    echo.
    echo Waiting for installation to complete... 
    echo Press any key to continue once you are done.
    pause >nul  :: Wait for the user to press any key
) else (
    echo File not found yet. Waiting...
    timeout /t 5 /nobreak >nul
    goto CheckFile
)

:: Continue with the rest of the script
goto InstallModules

:SkipPythonInstall
echo Skipping Python installation...
:: Directly go to module installation
goto InstallModules

:InstallModules
echo Before continuing, please confirm Python 3.11 is the ONLY version of python installed 
echo Press any key to continue once you are done.
pause >nul  :: Wait for the user to press any key
echo Now installing additional Python modules...
python -m pip install customtkinter keyboard pyautogui pillow ahk easyocr
python -m pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

echo All modules installed successfully!
pause
exit /b

:InstallModules4
echo Now installing additional Python modules...
python -m pip install customtkinter keyboard pyautogui pillow ahk easyocr
python -m pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

echo All modules installed successfully!
pause
exit /b