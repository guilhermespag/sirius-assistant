SIRIUS Assistant - Configuração

1. Instale dependências:
pkg install termux-api
pip install -r requirements.txt

2. Execute:
python3 SIRIUS_Assistant.py

Atalho sugerido:
echo "alias sirius='cd ~/downloads/SIRIUS && python3 SIRIUS_Assistant.py'" >> ~/.bashrc
source ~/.bashrc

Depois rode apenas:
sirius