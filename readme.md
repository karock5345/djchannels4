# <span style="color:orange;">**Linux development env.**</span>

# SETUP Linux development env.
Install Ubuntu desktop on PC / VM
Install Docker and Redis image: 
```bash
sudo apt install docker redis-tools -y
sudo docker run -p 6379:6379 -d redis:5
# Check Redis:
redis-cli
127.0.0.1:6379> PING
PONG
# Shutdown Redis:
redis-cli
127.0.0.1:6379> SHUTDOWN 
# Exit Redis-cli:
127.0.0.1:6379> EXIT 
```


# SETUP SOURCE CODE
### <span style="color:orange;">**Copy / git source code to home dir**</span>

Before install packages (python -m pip freeze > requirements.txt) 

```bash
git clone https://github.com/karock5345/djchannels4.git
sudo apt-get install -y virtualenv
cd to project folder
virtualenv env
source env/bin/activate
```


```bash
python3 -m pip install -r requirements.txt
# [List of installed packages] pip list
# [update package] 
python3 -m pip install django -U

python3 manage.py runserver 0.0.0.0:8000
# test the server : ip:8000
deactivate
```

### <span style="color:orange;">**Test the code**</span>

>python3 manage.py runserver 0.0.0.0:8000

Open web browner : http://127.0.0.1:8000/chat/