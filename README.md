# DjCanteen

**An ongoing personal project built to learn Django and HTMX.**

I'm building DjCanteen to learn how to make web applications with **Django** and **HTMX**. The idea is a simple canteen catalogue where I can organize products into categories, keep track of their prices and stock, and practice building interactive pages with server-rendered HTML.

**This project is still in progress.** Features, structure, and implementation choices will change as I learn. The main goal is to build understanding through a practical project, so the code reflects that learning process.

## What I'm learning

- Structuring a Django project with apps, URL routes, views, and templates.
- Modeling data with the Django ORM, including foreign keys and one-to-one relationships.
- Working with migrations, querysets, related objects, and pagination.
- Creating and validating forms with Django's `ModelForm`.
- Using HTMX to submit forms and navigate pages while Django handles rendering.
- Sharing layouts, template components, and form context across pages.
- Styling the interface with Tailwind CSS and daisyUI.
- Writing management commands to populate a development database.

## Current features

- **Category catalogue:** browse categories with descriptions and product counts.
- **Products by category:** open a category to see its products.
- **Product catalogue:** browse products with their category, description, price, and stock. Prices are displayed in Indonesian rupiah (`Rp`).
- **Pagination:** five categories per page, five products per category page, and ten products per page in the full catalogue.
- **Add Item modal:** create categories and products through Django forms submitted with HTMX, with validation errors displayed in the modal.
- **HTMX navigation:** boosted links and pagination fetch server-rendered pages without a traditional full-page reload.
- **Django admin:** manage categories, products, and product details.
- **Sample data:** management commands for seeding the catalogue and setting product stock.

## Technology stack

| Technology | Role |
| --- | --- |
| Python | Application language; `pyproject.toml` currently requires **3.15 or newer** |
| Django | Models, views, forms, templates, routing, and administration; currently declared as `>=6.1.3` |
| HTMX | HTML-driven requests and navigation; served locally from `assets/js/htmx.js` |
| SQLite | Default local database |
| Tailwind CSS 4 | Utility-based styling |
| daisyUI 5 | Interface components |
| uv | Python environment and dependency management |
| Node.js and npm | Frontend dependency installation and CSS compilation |

The Python dependencies also include Django REST Framework, Simple JWT, CORS headers, django-filter, Markdown, and PostgreSQL adapters. Their presence does not mean those features are active: REST Framework, JWT routes, and CORS integration are currently commented out, and the configured database is SQLite.

## Getting started locally

Run these commands from the project root, where `manage.py` is located.

### 1. Install the prerequisites

You will need:

- A Python version satisfying the requirement in `pyproject.toml` (currently `>=3.15`).
- `uv` for Python dependencies.
- Node.js and npm for the CSS tooling.

The dependency versions reflect the current development environment. If dependency resolution fails, check the Python requirement and package versions in `pyproject.toml` and `uv.lock`.

### 2. Install dependencies

```bash
uv sync
npm ci
```

`uv sync` creates the Python virtual environment and installs the project dependencies. `npm ci` installs frontend dependencies using the committed `package-lock.json`.

### 3. Configure the environment

Copy the example configuration and follow the instructions in [`.env.example`](.env.example):

```bash
cp .env.example .env
```

### 4. Apply database migrations

```bash
uv run python manage.py migrate
```

This creates the local SQLite database at `db.sqlite3` and applies the Django and catalogue migrations.

### 5. Add sample data (optional)

```bash
uv run python manage.py seed
uv run python manage.py seed_stock
```

The `seed` command creates or updates five sample categories, 25 products, and their calorie and ingredient details. Its categories are Meals, Snacks, Drinks, Desserts, and Breakfast. Re-running it updates matching sample entries rather than intentionally creating another set; it can overwrite their descriptions, prices, and details.

The separate `seed_stock` command sets the stock of **every existing product to 20**, including products you added yourself. Newly created products otherwise default to zero stock unless a value is supplied.

### 6. Build the styles

```bash
npm run build
```

For development, run the watcher in a separate terminal instead:

```bash
npm run dev
```

Both commands compile `assets/css/app.css` into `catalogue/static/css/app.css`. The watcher rebuilds when relevant source files change; the build command produces minified CSS.

### 7. Start Django

```bash
uv run python manage.py runserver
```

Open <http://127.0.0.1:8000/> to browse the categories. Use **Add Item** in the navigation bar to create a category or product. Create a category first so it can be selected when adding a product.

To access the Django admin, create a superuser:

```bash
uv run python manage.py createsuperuser
```

Then sign in at <http://127.0.0.1:8000/admin/>.

## How Django and HTMX work together

Django handles database access, form validation, and HTML rendering. HTMX adds interactivity through attributes in the templates:

- `hx-boost="true"` on the shared layout enhances normal links and pagination with AJAX navigation.
- `hx-post` submits the category and product forms to their Django views.
- `hx-target` directs returned form validation errors into the matching error container.
- After a successful save, the view returns an `HX-Location` header pointing to the corresponding catalogue page.

The forms include Django's CSRF token. Shared forms are supplied through `catalogue.context_processors.navbar_forms`, making the Add Item modal available throughout the catalogue.

This gives me a practical way to explore interactive interfaces while keeping the application logic and rendering in Django.

## Data models

| Model | Fields and relationships |
| --- | --- |
| `Category` | Name and optional description; contains multiple products. |
| `Product` | Name, optional description, decimal price, nonnegative stock, and a category foreign key. |
| `Detail` | Calories, optional ingredients, and a one-to-one relationship with a product. |

A category referenced by products is protected from deletion. Deleting a product also deletes its associated detail record. Product details are currently available through the model, seed command, and admin; the public catalogue does not display them yet.

## Routes

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/` | Category list |
| GET | `/categories/<category_id>/` | Products belonging to a category |
| POST | `/categories/add/` | Create a category |
| GET | `/products/index/` | Full product list |
| POST | `/products/add/` | Create a product |
| GET | `/admin/` | Django admin entry point |

Catalogue list pages accept a `?page=` query parameter for pagination.

## Project structure

```text
DjCanteen/
├── assets/
│   ├── css/app.css              # Tailwind and daisyUI source
│   └── js/htmx.js               # Local HTMX script
├── catalogue/
│   ├── management/commands/     # seed and seed_stock commands
│   ├── migrations/              # Database schema migrations
│   ├── static/                  # Compiled CSS and favicon
│   ├── templates/
│   │   ├── components/          # Shared product table and pagination
│   │   ├── layouts/             # Shared layout, navigation, and forms
│   │   └── pages/               # Category and product pages
│   ├── admin.py                # Admin model registration
│   ├── context_processors.py   # Shared navigation forms
│   ├── forms.py                # Category and product ModelForms
│   ├── models.py               # Category, Product, and Detail
│   ├── urls.py                 # Catalogue routes
│   └── views.py                # Listing and creation views
├── config/                     # Django settings and project URLs
├── src/djcanteen/              # Python package entry point
├── manage.py                   # Django management entry point
├── package.json                # Frontend dependencies and CSS scripts
├── pyproject.toml              # Python dependencies and project metadata
└── uv.lock                     # Python dependency lockfile
```

## Development checks

Run Django's configuration checks with:

```bash
uv run python manage.py check
```

Run the Django test runner with:

```bash
uv run python manage.py test
```

`catalogue/tests.py` is currently a placeholder, so there are no catalogue tests yet. Automated coverage is one of the areas still to develop as the project grows.

## Ongoing development

DjCanteen is still a learning project, and the current scope centers on browsing and creating catalogue entries. Editing and deleting entries through the public interface, search and filtering, and displaying product details are possible areas to explore next. Orders, checkout, and payments are not implemented.

The public catalogue creation views currently have no authentication or permission checks. The setup above is intended for local development; production configuration and access controls still need work before a public deployment.

My focus is to keep learning Django and HTMX by building, experimenting, and improving this project step by step.
