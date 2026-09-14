# ER-диаграмма портала

```text
CustomUser 1 ──────── * Booking

CustomUser
- id: bigint PK
- username: varchar(150), unique
- password: varchar(128)
- full_name: varchar(255)
- phone: varchar(20)
- email: email
- is_admin: boolean
- is_staff: boolean
- is_superuser: boolean
- date_joined: datetime

Booking
- id: bigint PK
- user_id: FK -> CustomUser.id
- room_name: varchar(50), choices: auditorium/coworking/cinema
- conference_date: datetime
- payment_method: varchar(20), choices: offline/sbp
- status: varchar(20), choices: new/scheduled/completed
- review: text, nullable
- created_at: datetime
- updated_at: datetime
```

