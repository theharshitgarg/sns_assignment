# About

### Installation

#### Using docker
```
docker build -t app-1 .
docker run --name app-1 -p 8000:8000 app-1
```

#### Without Using docker
```
pip install -r requirements.txt
python backend/manage.py runserver
```