"""test"""
from settings import settings

settings.setyaml("config.yaml")

for k, v in settings.items():
    print(k, v)
