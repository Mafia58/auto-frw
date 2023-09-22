echo "Cloning Repo, Please Wait..."
git clone https://github.com/Mafia58/auto-frw
cd auto-frw
echo "Installing Requirements..."
pip3 install -U -r req.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
