📝 Домашнее задание к занятию 6 «Создание собственных модулей»

## Подготовка к выполнению

1. Создан пустой публичный репозиторий `my_own_collection`.

2. Скачан репозиторий Ansible:

```
git clone https://github.com/ansible/ansible.git
```

Переход в директорию Ansible:

```
cd ansible
```

Создано виртуальное окружение:

```
python3 -m venv venv
```

Активировано окружение и установлены зависимости:

```
source venv/bin/activate
```

```
pip install -r requirements.txt
```

Выполнена настройка окружения:

```
source hacking/env-setup
```

После проверки окружение деактивировано:

```
deactivate
```

## Основная часть

### Шаг 1. Создание модуля

Создан файл my_own_module.py в директории виртуального окружения.

### Шаг 2. Базовый код

Файл наполнен шаблонным содержимым Ansible-модуля.

### Шаг 3. Доработка

Модуль изменён так, чтобы:

параметр path задавал путь к файлу,

параметр content задавал содержимое файла,

при запуске модуль создавал/обновлял текстовый файл на хосте.

### Шаг 4. Проверка на исполняемость

Модуль протестирован локально:

<img width="1511" height="93" alt="Снимок экрана 2025-08-30 в 01 16 45" src="https://github.com/user-attachments/assets/52808630-c11f-4d97-9982-5f8301c22296" />


### Шаг 5. Single task playbook

Написан простой playbook, использующий модуль.

### Шаг 6. Идемпотентность

Playbook протестирован на идемпотентность:

<img width="1511" height="771" alt="Снимок экрана 2025-08-30 в 02 22 13" src="https://github.com/user-attachments/assets/7058adf1-b3a9-4a45-8e73-1257a263ee12" />


### Шаг 7. Завершение окружения

Виртуальное окружение деактивировано.

### Шаг 8. Инициализация collection

```
ansible-galaxy collection init my_own_namespace.yandex_cloud_el
```

### Шаг 9. Перенос модуля

Модуль перенесён в директорию plugins/modules/ коллекции.

### Шаг 10. Role

Single task playbook преобразован в роль.

У роли заданы defaults/main.yml с параметрами модуля.

### Шаг 11. Playbook

Создан playbook для вызова роли.

### Шаг 12. Документация и версия

Заполнена документация для коллекции

### Шаг 13. Сборка архива

```
ansible-galaxy collection build
```

### Шаг 14. Создание доп. директории

```
test_col
```

### Шаг 15. Установка коллекции

```
my_own_namespace-yandex_cloud_el-1.0.0.tar.gz
```

<img width="1158" height="195" alt="Снимок экрана 2025-08-30 в 02 07 45" src="https://github.com/user-attachments/assets/ce42f610-cd20-494f-98d4-45d103e93eb1" />


Шаг 16. Запуск playbook

Playbook запущен и работает корректно:

<img width="1511" height="397" alt="Снимок экрана 2025-08-30 в 02 08 56" src="https://github.com/user-attachments/assets/65dd264f-3d02-4e4b-ac41-98360bebc903" />

