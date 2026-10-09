<div align="center">

# 🖼️ Django Photo Album

**A photo gallery where you upload photos in bulk with captions, organize them into categories and filter by category.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)

</div>

---

## ✨ Features

- 📤 **Bulk upload** - add several photos at once with a description and category.
- 🗂️ **Categories** - choose an existing category or create a new one.
- 🔎 **Filter** the gallery by category.
- 🔍 **Photo detail** page and 🗑️ **delete** photos.
- 💾 Stored in an SQLite database.

## 🚀 Getting Started

```bash
git clone https://github.com/Arashomranpour/Django-album.git
cd Django-album

python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install django pillow

python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/.

## 🔗 Routes

| Route | Purpose |
|---|---|
| `/` | Gallery (with category filter) |
| `/photo/<id>` | View a photo |
| `/add/` | Upload photos / create a category |
| `/delete/<id>` | Delete a photo |

## 📁 Project Structure

```
.
├── manage.py
├── photoalbum/     # Project settings and root URLs
└── photos/         # App: Category and Photo models, forms, views, templates
```

## 🛠️ Tech Stack

`Python` · `Django` · `Pillow` · `SQLite`
