echo "Cloning Repo...."
git clone https://github.com/hardeepsingh62/aasimsearcherbot.git /aasimsearcherbot
cd /aasimsearcherbot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 main.py
