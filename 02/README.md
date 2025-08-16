# Playbook: Install and Configure Vector

## Описание

Данный playbook автоматизирует установку и настройку [Vector](https://vector.dev/) на целевых хостах (группа `vector` из inventory).

При выполнении playbook делает следующее:

1. Создаёт необходимые директории:

   * `/opt/vector` — директория для установки;
   * `/etc/vector` — директория для конфигурации;
   * `/var/lib/vector` — рабочая директория для данных.

2. Скачивает архив с дистрибутивом Vector версии `0.39.0` с GitHub.

3. Распаковывает дистрибутив в `/opt/vector`.

4. Создаёт символьную ссылку на бинарник в `/usr/local/bin/vector`.

5. Разворачивает конфигурацию из шаблона (`templates/vector.toml.j2`) в `/etc/vector/vector.toml`.

6. Создаёт systemd unit-файл `/etc/systemd/system/vector.service`.

7. Перезагружает systemd-демон.

8. Включает и запускает сервис `vector`.

При изменении конфигурации или systemd-юнита вызывается handler, который перезапускает сервис `vector`.

---

## Параметры

В playbook переменные не вынесены, используются зашитые значения:

* **Версия Vector**: `0.39.0`
* **Пути**:

  * `/opt/vector` — установка;
  * `/etc/vector/vector.toml` — конфигурация;
  * `/usr/local/bin/vector` — бинарник;
  * `/var/lib/vector` — рабочая директория.

Шаблон конфигурации находится в `templates/vector.toml.j2`.

---

## Теги

Каждая группа задач размечена тегами:

* `setup` — подготовка директорий
* `download` — скачивание дистрибутива
* `install` — распаковка архива и установка бинарника
* `config` — развёртывание конфигурации и systemd unit
* `service` — перезагрузка systemd и запуск сервиса

### Примеры запуска по тегам

Запустить только установку:

```bash
ansible-playbook -i inventory/prod.yml vector.yml --tags install
```

Применить изменения только конфигурации:

```bash
ansible-playbook -i inventory/prod.yml vector.yml --tags config
```

Запустить сервисные операции:

```bash
ansible-playbook -i inventory/prod.yml vector.yml --tags service
```

---

## Использование

1. Добавьте хосты в `inventory/prod.yml`, например:

```yaml
vector:
  hosts:
    vector-01:
      ansible_connection: local
```

2. Запустите playbook:

```bash
ansible-playbook -i inventory/prod.yml vector.yml
```

После выполнения Vector будет установлен и запущен как systemd-сервис.

Скриншоты:
<img width="1504" height="752" alt="Снимок экрана 2025-08-16 в 12 14 34" src="https://github.com/user-attachments/assets/8855e31f-c455-4c8b-8406-9f689dde5976" />

<img width="1504" height="783" alt="Снимок экрана 2025-08-16 в 12 14 52" src="https://github.com/user-attachments/assets/e2bb353f-ee3d-44c3-bee9-fa3222c54d95" />

<img width="1504" height="309" alt="Снимок экрана 2025-08-16 в 12 15 01" src="https://github.com/user-attachments/assets/eb2a3f04-ea03-412a-bcc2-18c220169f06" />
