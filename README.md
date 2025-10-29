# Django Admin Interface — Sorting & Listing (Admin-Interface–Übung)

This repository contains a small Django project focused on **configuring the Django Admin** so database entries can be **listed clearly and sorted reliably** using `admin.py` settings.  
The aim is a clean, practical example without unnecessary extras.

## Contents

- `core/` — Project configuration (settings, URLs, WSGI/ASGI).
- `bookings_app/` — App scaffold (models, admin configuration).
- `events_app/` — App scaffold (models, admin configuration).
- `manage.py` — Django management entry point.
- `requirements.txt` — Python dependencies.

> Repository layout confirmed from the public repo structure.

## What’s implemented in the Admin

The admin configuration focuses on making model lists **useful and fast to navigate**:

- **`list_display`** to define which fields appear in changelists
- **`ordering`** for default sort order
- **`list_filter`** for quick filtering in the sidebar
- **`search_fields`** to search over selected text fields
- (optionally) **`date_hierarchy`** and **`list_per_page`** for larger datasets

All changes are done in each app’s `admin.py`.

## Example: Minimal `admin.py` pattern

```python
from django.contrib import admin
from .models import ExampleModel

@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    # Columns in the list view
    list_display = ("id", "name", "created_at")
    
    # Default ordering (descending by created_at)
    ordering = ("-created_at",)
    
    # Sidebar filters
    list_filter = ("status", "created_at")
    
    # Search box
    search_fields = ("name", "description")
    
    # Optional niceties
    date_hierarchy = "created_at"
    list_per_page = 50
```

> Tip: In the list view, you can also click on **column headers** to sort ascending/descending by that column when it’s listed in `list_display` and supported by the model field.

## How to run locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/AbbasEl11/Admin-Interface--bung.git
   cd Admin-Interface--bung
   ```

2. **Create & activate a virtual environment (recommended)**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open the admin**
   - Visit: `http://127.0.0.1:8000/admin/`
   - Log in with your superuser
   - Navigate to your models (from `bookings_app` / `events_app`) to see the configured list view and sorting.

## Where to add/change admin configuration

- `bookings_app/admin.py`
- `events_app/admin.py`

Follow the example pattern above and adjust:
- `list_display` to show the most relevant fields for your model
- `ordering` to set a sensible default sort (e.g., newest first)
- `list_filter` and `search_fields` to improve discoverability

## Notes

- This project is intended as a **practical exercise** for Django Admin setup and model list ergonomics.
- No external styling or frontend changes are required; everything is done through Django’s admin configuration.

## Authors

- Abbas EL  

