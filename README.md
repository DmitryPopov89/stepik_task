## Stepik test automation task


#### Подготовка к запуску тестов: 


```commandline
python -m  venv venv
venv\Scripts\activate
pip install -r requirements.txt

```

#### Запуск тестов:

```commandline
python -m pytest -v --tb=line --language=en -m need_review 

```