
### 장르 데이터 DB에 저장

```bash
python manage.py loaddata genre_data.json
```

### 영화 데이터 DB에 저장

- 반드시 장르 데이터를 먼저 저장한 후에 저장해야 한다.

```bash
python manage.py loaddata movie_data.json
```

### 영화 퀴즈 데이터 DB에 저장

```bash
python manage.py loaddata kmovie_data.json
```

