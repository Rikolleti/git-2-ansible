# Документация коллекции

- [Роль `file_create`](./roles/file_create.md)
- Плагины/модули: (если есть) см. `docs/plugins/...`

# Роль: file_create

Создаёт файл с заданным содержимым.

## Переменные

| Переменная           | Тип    | По умолч. | Описание                    |
|----------------------|--------|-----------|-----------------------------|
| `file_create_path`   | string | обязат.   | Путь к файлу                |
| `file_create_content`| string | ""        | Содержимое файла            |
| `file_create_mode`   | string | "0644"    | Права на файл               |
| `file_create_owner`  | string | root      | Владелец                    |
| `file_create_group`  | string | root      | Группа                      |

## Пример использования
```yaml
- hosts: localhost
  connection: local
  collections:
    - my_own_namespace.yandex_cloud_el
  roles:
    - role: file_create
      vars:
        file_create_path: "/tmp/hello.txt"
        file_create_content: "Hello"
        file_create_mode: "0644"


### Локальный `roles/file_create/README.md`
Можно продублировать тот же блок, что в docs.

---

# Проверка структуры и сборка

(Опционально, но полезно)
```bash
# линтеры (если стоят)
ansible-lint
yamllint .

# сборка архива коллекции
ansible-galaxy collection build .
