# Ansible Playbook - Установка Lighthouse

## Описание

Плейбук устанавливает и настраивает веб-интерфейс **Lighthouse** за **Nginx** на хостах группы `lighthouse`.

Что делает:
- Устанавливает `nginx` (Debian/Ubuntu).
- Клонирует репозиторий **Lighthouse** в целевой каталог.
- Разворачивает конфигурацию `nginx` из шаблона `templates/nginx.conf.j2`.
- Включает автозапуск и запускает сервис `nginx`.

---

## Требования

- Доступ Ansible к хостам с привилегиями `become: true`.
- Интернет-доступ с целевых хостов (для `git clone`).
- Целевые ОС: Debian/Ubuntu (используется модуль `apt`).
- Определены переменные (см. ниже), при необходимости --- в зашифрованном vault-файле.

---

## Структура

```
├─ inventory/
│ └─ hosts.yml
├─ group_vars/
│ └─ all.yml # содержит lighthouse_repo, lighthouse_dir, nginx_port
├─ templates/ 
│ └─ nginx.conf.j2 
└─ prod.yml # сам playbook
```

## Задачи плейбука (prod.yml)

1.  **Install nginx** --- установка пакета nginx через apt.
2.  **Download package** --- клонирование репозитория Lighthouse (git) в {{ lighthouse_dir }}.
3.  **Deploy nginx template** --- выкладка шаблона nginx.conf.j2 в /etc/nginx/nginx.conf и уведомление хендлера рестарта Nginx.
4.  **Ensure nginx service is enabled and started** --- включение автозапуска и запуск сервиса nginx.

### Хендлеры

-   **restart nginx** --- перезапуск сервиса nginx после изменения конфигурации.

Запуск
------

Обычный запуск (переменные под Vault):
`ansible-playbook -i inventory/hosts.yml prod.yml --ask-vault-pass`

Пробный прогон без изменений (dry run):
`ansible-playbook -i inventory/hosts.yml prod.yml --check --ask-vault-pass`

Теги
----

Все задачи имеют теги и могут запускаться выборочно:
-   nginx --- задачи, связанные с установкой и управлением Nginx.
-   lighthouse --- клонирование репозитория Lighthouse.
-   config --- выкладка конфигурации Nginx.
-   service --- управление сервисом Nginx.

Примеры запуска с тегами:

# Выполнить только установку nginx
`ansible-playbook -i inventory/hosts.yml prod.yml --tags nginx`

# Выполнить только клонирование Lighthouse
`ansible-playbook -i inventory/hosts.yml prod.yml --tags lighthouse`

# Выполнить только выкладку конфига
`ansible-playbook -i inventory/hosts.yml prod.yml --tags config`

Проверка
--------
Проверить активность сервиса:
`systemctl is-active nginx`

Проверить доступность в браузере:
`http://<IP_или_имя_хоста>:<nginx_port>/`
