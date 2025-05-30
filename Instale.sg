#!/bin/bash

echo "🔧 Instalando dependências necessárias..."
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install termux-api -y
pkg install wget -y
pkg install unzip -y
pkg install git -y
pkg install portaudio -y

pip install --upgrade pip
pip install SpeechRecognition gTTS pyaudio

echo "📂 Criando pastas e baixando projeto..."
cd ~
rm -rf SIRIUS
git clone https://github.com/guilhermespag/sirius-assistant.git SIRIUS

cd SIRIUS

mkdir -p voices

echo "✅ Instalação concluída!"
echo "🚀 Para executar, rode:"
echo "cd ~/SIRIUS && python SIRIUS_Assistant.py"
