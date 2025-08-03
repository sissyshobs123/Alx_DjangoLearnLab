# Task 0: Implementing a Custom User Model in Django

## 1. Custom User Model

- Created `CustomUser` class in `relationship_app/models.py`
- Subclassed `AbstractUser` to allow custom fields in the future

## 2. UserProfile Model

- Created `UserProfile` model with a OneToOne link to `CustomUser`
- Added `role` field with choices: `'librarian'` and `'member'`

## 3. Signals

- Used Django signals to automatically create and save `UserProfile` upon user creation

## 4. Views and URLs

- Created:
  - `dashboard_redirect` view that checks `role` and redirects appropriately
  - `librarian_dashboard` and `member_dashboard` views with login required
- Defined URL patterns:
  - `/dashboard/`
  - `/dashboard/librarian/`
  - `/dashboard/member/`

## 5. Templates

- `librarian_dashboard.html` and `member_dashboard.html` show personalized content

## 6. Authentication Flow

- Set `AUTH_USER_MODEL = 'relationship_app.CustomUser'` in settings
- Set `LOGIN_REDIRECT_URL = '/dashboard/'` for redirect after login

---

✅ **Tested and working:** user login redirects based on role.
