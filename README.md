# CUL BOT

Its a very Cul bot running on python made by mouda817#2464

<h3>
Do the follwing to run the bot on you machine
</h3>

1. Clone The Bot with
````
git clone https://github.com/moosa817/cul_bot.git
````
OR Just Download as zip

2. Install Python if you dont have and open the folder in command prompt or bash

3. Create a virtual env in python
```
#For Windows
python -m venv bot_env
bot_env/Scripts/activate

#For Linux/Mac
python -m venv bot_env
source bot_env/bin/
```

4. Open config.py and set the values
````
auth = "" #discord bot auth token
db_host = "" #mysql databasehost
db_database = "" #mysql database db
db_pwd = "" #mysql db pwd
db_user = "" #mysql db user
````
5. Run The Bot
```
python main.py
```


<h2>ADDITIONAL INFO</h2>
https://cul-bot.moosa817.repl.co/ is a website connected to mysql to db to add images and replies

You can view code of website at https://replit.com/@moosa817/Cul-Bot

Here's the sql for the db
```
CREATE TABLE IF NOT EXISTS `img_stuff` (
    `id` INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `img` VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS `logs` (
     `id` INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
    `time` VARCHAR(255) NOT NULL,
    `ip_address` VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS `text_stuff` (
     `id` INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `text` VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS `images` (
     `id` INTEGER PRIMARY KEY,
    `filename` TEXT NOT NULL,
    `img` TEXT NOT NULL
);
-- MYSQL DB
```