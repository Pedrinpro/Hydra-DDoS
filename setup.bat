@echo off

rem Verifica se o Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo Python nao encontrado. Instalando Python...
    rem Adicione aqui os comandos para instalar o Python
    rem Exemplo: choco install python --yes
) else (
    echo Python encontrado.
)

echo Deseja instalar os modulos http.server, random, threading, socket e colorama? (S/N)

choice /c SN /n /m "Digite S para Sim ou N para Nao: "

if errorlevel 2 goto No
if errorlevel 1 goto Yes

:Yes
echo Você escolheu Sim.
pip install -U http.server
pip install -U random
pip install -U threading
pip install -U socket
pip install -U colorama
goto finali

:No
echo Você escolheu Nao.
goto end

:end

:finali
echo Instalação finalizada.
