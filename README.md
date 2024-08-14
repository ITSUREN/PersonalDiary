# 📔 Personal Diary 
- A Simple Flask application that uses web interface to store Diary Entries to SQLite DB.
- Chosen for simplicity.
- A project for a Raspberry Pi home server.

&ensp;

# 🌐 Database Structure
- Should contain the following attributes on creation:
```sql
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    content TEXT
```

&ensp;

# ✨ Features
- Limited Features:
    1. **➕ Add Entries**: Date and Time are recorded on submit. 
    2. **➖ Delete Entries**: Date is used to search the record and then purged.
    3. **🔨 Modify Entries**: Date is used to search the record and then modified; Date and Time are not modified upon Submit.
&ensp;
- Acknowledged Missing Features:
    1. **Manual DB Creation**: Having to manually create a sqlite database, instead of being managed by the application. (author didn't feel the need due to being a personal project)
    2. **Backup Management**: Backup not managed by the application. (Author didn't feel the need as backup is managed by a crontab instance with rsync)
    3. **UI**: Better UI for integrating the Add, Delete, Modify and View Sections. (Author didn't feel the need; functional enough)