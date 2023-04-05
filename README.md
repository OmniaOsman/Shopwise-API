# Shopwise-API
 API for E-commerce website using Django Rest Framework

## accounts app

The authentication in project used Djoser third party package. Djoser is a library that provides a set of Django Rest Framework views to handle basic actions
such as registration, login, logout, password reset and account activation



### API Reference

#### Sign up for new user

```
  POST /auth/users/
```

| Body      | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. username, email, password, re_password **optional**, first_name, last_name  |


#### Create token

```
  POST /auth/token/login/ 
```

| Body      | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. email, password |


#### Reset password

```
  POST /auth/users/reset_password/
```

| Headers    | Description                |
| :--------  | :------------------------- |
| `Authorization Token` | **Required**. email, it will used the email to reset the password  |


#### Reset password confirmation

```
  POST /auth/users/reset_password_confirm/
```

| Headers    | Description                |
| :--------  | :------------------------- |
| `Authorization Token` | **Required**. uid, token, new_password, re_new_password  |


#### List all users

```
  GET /auth/users/
```

| Headers    | Description                |
| :--------  | :------------------------- |
| `Authorization Token` | nothing |


#### My information

```
  PATCH /auth/users/
```

| Headers    | Description                |
| :--------  | :------------------------- |
| `Authorization Token` | Body --> data want to update |


