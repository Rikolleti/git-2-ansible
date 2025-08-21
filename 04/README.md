# Домашнее задание к занятию 4 «Работа с roles»

## Выполненное задание

В рамках задания были созданы три роли и три плейбука для развертывания следующих сервисов:

- **ClickHouse** (роль: `clickhouse-role`)
- **Vector** (роль: `vector-role`)
- **LightHouse** (роль: `lighthouse-role`)

---

## Структура решения

### Роли

1. **clickhouse-role**
   - Устанавливает и настраивает СУБД ClickHouse.
   - Переменные:
     - `clickhouse_version` — версия ClickHouse.
     - `clickhouse_packages` — список пакетов для установки.
   - Используются шаблоны для конфигурации.
   - Репозиторий: [clickhouse-role](https://github.com/Rikolleti/clickhouse-role-homework)

2. **vector-role**
   - Устанавливает агент сбора логов Vector.
   - Конфигурация перенесена в шаблоны (`templates/vector.yaml.j2`).
   - Репозиторий: [vector-role](https://github.com/Rikolleti/vector-role-homework)

3. **lighthouse-role**
   - Устанавливает и настраивает веб-интерфейс LightHouse.
   - Переменные:
     - `lighthouse_repo` — git-репозиторий LightHouse.
     - `lighthouse_dir` — директория для установки.
   - Используются шаблоны для Nginx-конфига.
   - Репозиторий: [lighthouse-role](https://github.com/Rikolleti/lighthouse-role-homework)

---

### Playbook-и

1. **clickhouse-playbook**
   - Разворачивает ClickHouse с использованием роли `clickhouse-role`.

2. **vector-playbook**
   - Разворачивает Vector с использованием роли `vector-role`.

3. **lighthouse-playbook**
   - Разворачивает LightHouse с использованием роли `lighthouse-role`.
   - Использует зависимость от ClickHouse (подключается к уже установленной БД).

Все плейбуки используют `requirements.yml` для загрузки ролей.

---

## requirements.yml

```yaml
---
- name: clickhouse
  src: git@github.com:Rikolleti/clickhouse-role-homework.git
  scm: git

- name: lighthouse
  src: git@github.com:Rikolleti/lighthouse-role-homework.git
  scm: git

- name: vector
  src: git@github.com:Rikolleti/vector-role-homework.git
  scm: git
  
