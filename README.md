# Shopwise-API
 API for E-commerce website using Django Rest Framework

## accounts app

The authentication in project used Djoser third party package. Djoser is a library that provides a set of Django Rest Framework views to handle basic actions
such as registration, login, logout, password reset and account activation



### API Reference

#### Sign up for new user

```http
  POST /auth/users/
```

| Body      | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. username, email, password, re_password **optional**, first_name, last_name  |

