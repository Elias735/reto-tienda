#!/usr/bin/env bash

echo "1. Creando entorno virtual..."
python3 -m venv .venv

echo "2. Activando entorno virtual..."
source .venv/bin/activate

echo "3. Actualizando pip..."
python3 -m pip install --upgrade pip

echo "4. Instalando dependencias de requirements.txt..."
python3 -m pip install -r requirements.txt

echo "5. Ejecutando script de compilación..."
bash compilar.sh

echo "¡Todo listo! Entorno configurado y contratos compilados."