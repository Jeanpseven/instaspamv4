@echo off
python -V >nul 2>&1 && (
    python instaspamv4.py
) || (
    echo "Python 3.7 não encontrado, instale o Python!"
    timeout /t 5 /nobreak > NUL
    exit
)

timeout /t 15 /nobreak > NUL
