# 📝 Домашнее задание к занятию 5 «Тестирование roles»

## ✅ Выполненные шаги

### Подготовка
- Установлены `molecule`, `molecule_docker`, `molecule_podman`.  
- Скачан образ `aragast/netology:latest` с предустановленными podman, tox и Python (3.7, 3.9).  

---

### Основная часть

#### Molecule
1. В роли **clickhouse-role** выполнена команда:
```
   molecule test -s ubuntu_xenial
```

2. В каталоге vector-role создан тестовый сценарий:
```
molecule init scenario --driver-name docker
```

3. В molecule.yml добавлены разные дистрибутивы:
```
oraclelinux:8
ubuntu:latest
```

4. Исправлены ошибки роли, найденные при тестировании.

5. В verify.yml добавлены проверки:
Валидность конфига Vector.
Успешный запуск сервиса.

6. Запуск тестирования показал успешное прохождение всех проверок:

<img width="927" height="782" alt="Снимок экрана 2025-08-25 в 14 38 30" src="https://github.com/user-attachments/assets/e1cac964-63b1-4837-b4ef-670273df5d02" />


#### Tox

1. В директорию vector-role добавлены необходимые файлы для tox.
2. Запуск контейнера:
```
docker run --privileged=True -v /home/rikolleti/Netology/git-2-ansible/05/vector-role-homework:/opt/vector-role -w /opt/vector-role -it aragast/netology:latest /bin/bash
```
3. Внутри контейнера выполнена команда:
```
tox
```
4. Создан облегчённый сценарий Molecule с драйвером molecule_podman
5. В tox.ini прописан запуск облегчённого сценария
```
posargs:molecule test -s tox --destroy always
```
6. Запуск Tox:

   <img width="1509" height="782" alt="Снимок экрана 2025-08-25 в 16 51 13" src="https://github.com/user-attachments/assets/63ea7f12-9c15-401c-b31c-aa8dc9d98bef" />

