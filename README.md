# Djitter

Twitter clone using Django

This code is based on a Django tutorial (https://ahackersday.com/blog/djitter-how-to-build-a-twitter-clone-using-django-2-0/).

## Usage

```bash
git clone https://github.com/tat3/djitter.git 
echo SECRET_KEY="anything" > .env
docker-compose build
docker-compose run app ./manage.py migrate
docker-compose up
docker exec -it djitter_app_1 ./manage.py migrate
```
Then open http://localhost.

