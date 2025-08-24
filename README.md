# Social Media API

Django REST Framework Social Media API for ALX Django Learn Lab.  

## Endpoints

### Accounts
- **Register**: `POST /api/accounts/register/`
- **Login**: `POST /api/accounts/login/`
- Use token: `Authorization: Token <your_token>`

### Posts
- **Create**: `POST /api/posts/`
- **List**: `GET /api/posts/`
- **Update**: `PUT /api/posts/{id}/` (author only)
- **Delete**: `DELETE /api/posts/{id}/` (author only)

### Comments
- **Create**: `POST /api/comments/`
- **List**: `GET /api/comments/`
- **Update**: `PUT /api/comments/{id}/` (author only)
- **Delete**: `DELETE /api/comments/{id}/` (author only)

## Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

### Follows & Feed

- Follow user: `POST /api/accounts/follow/{user_id}/` (auth required)
- Unfollow user: `POST /api/accounts/unfollow/{user_id}/` (auth required)
- Feed (posts from followed users): `GET /api/feed/` (auth required)

API Docs (Task 3)
Follow a User

POST /api/accounts/follow/{user_id}/
Response: { "message": "You are now following alice" }

Unfollow a User

POST /api/accounts/unfollow/{user_id}/
Response: { "message": "You unfollowed alice" }

Like a Post

POST /api/posts/{id}/like/
Response: { "message": "Post liked" }

Unlike a Post

POST /api/posts/{id}/unlike/
Response: { "message": "Post unliked" }

Get Notifications

GET /api/notifications/

Supports filters: ?unread=true or ?read=true
Response:

[
  {"id":1,"actor":"bob","verb":"liked your post","read":false}
]

 Mark Notification as Read

PATCH /api/notifications/{id}/
Body: { "read": true }