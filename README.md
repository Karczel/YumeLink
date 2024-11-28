# YumeLink
Business model reference : social media
<br>
[Deployed link](https://yumelink.onrender.com)
<br>
**May take a while to finish loading**

### to run locally, run these commands:
```-r requirement.txt```
```python manage.py makemigrations```
```python manage.py migrate```
```python manage.py runserver```
### and you may load data for testing
Mac/Linux
```commandline
for file in data/*.json; do
    python manage.py loaddata $file
done
```
Windows
```commandline
for %f in (data\*.json) do python manage.py loaddata "%f"
```

## DEMO
| username | pwd |
|-|-|
| abc | iamabc1234 |
| karczel | iamkarczel1234 |
| mammothx | iammammoth1234 |
| tanfan | iamtanfan1234 |
