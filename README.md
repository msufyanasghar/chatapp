Go to the project server directory

```bash
cd "sandesha/server"
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 7890
```

Go to the project client directory

```bash
cd ..
cd client
npm install
npm start
```
