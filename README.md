# Account Management System

This project is a simple system for **account management**, including:
- Authentication (login, logout)
- Authorization (permissions, roles)

---

## Tech Stack

- Python 3.14
- Django 6
- SQLite3

---

## Run with Script

You can start the project using the provided script:

```bash
./scripts/run.sh
```

You will be asked to enter a port:

```bash
Enter port (default 8000):
```

- Press **Enter** to use default port `8000`
- Or enter a custom port (e.g. `9000`)

---

## Run Manually

Follow these steps:

```bash
cd src
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

You can change the port if needed:

```bash
python manage.py runserver 0.0.0.0:<your_port>
```

---

## Notes

- Make sure Python 3.14 is installed
- Database is SQLite3 (no setup required)
- Default host: `0.0.0.0`
