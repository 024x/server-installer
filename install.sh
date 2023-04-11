apt-get update -y
apt-gey upgrade -y
apt-get install -y git
apt-get install -y python3
apt-get install -y python3-pip
git clone https://github.com/S4tyendra/python-server
cd "python-server"
pip install pyrogram
pip install -r requirements.txt
chmod -x ./start.sh