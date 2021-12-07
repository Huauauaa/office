# Office

## [Features](./feature.md)

## prepare

- `python3 -m venv venv` `. venv/bin/activate`

### Database

```sql
create database <db_name>
```

```env
DB_USERNAME=
DB_PASSWORD=
DB_DATABASE=
```

#### init db

- `flask db init`

#### migrate

- `flask db migrate`

#### create table

- `flask db upgrade`

## Install

- `pip install -r requirements.txt`
- `pnpm install`

## Run

- `flask run`
- `pnpm run dev`

## Build

- `pnpm run build`
