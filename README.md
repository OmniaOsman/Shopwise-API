# Shopwise-API
 API for E-commerce website using Django Rest Framework

## accounts app

The authentication in project used Djoser third party package. Djoser is a library that provides a set of Django Rest Framework views to handle basic actions such as registration, login, logout, password reset and account activation. Gmail is used for email settings



### API Reference

#### Sign up for new user

```
  POST /auth/users/
```

| Body      | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. `username`, `email`, `password`, `re_password` **optional**, `first_name`, `last_name`  |


#### Create token

```
  POST /auth/token/login/ 
```

| Body      | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. `email`, `password` |


#### Reset password

```
  POST /auth/users/reset_password/
```

| Headers    | Description                |
| :--------  | :------------------------- |
| `Authorization Token` | **Required**. `email`, it will used the email to reset the password  |


#### Reset password confirmation

```
  POST /auth/users/reset_password_confirm/
```

| Headers    | Description                |
| :--------  | :------------------------- |
| `Authorization Token` | **Required**. `uid`, `token`, `new_password`, `re_new_password`  |


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


#### Activate account

```
  POST /auth/users/activation/
```

| Body       | Description                |
| :--------  | :------------------------- |
| `Token`, `uid` | nothing |




## shop app

This app contains the CRUD operations for products and categories. We can filter the product with `product_title` or `product_brand`, and categories with `title`


#### Display all products

```
  GET /api/products/
```


#### Display all categories

```
  GET /api/category/
```


#### Add new product

```
  POST /api/product/
```

| Headers    | Body                       |   
| :--------  | :------------------------- |
| `Authorization Token`    | **required** `product_title`, `product_price`, `product_desc`, `product_img`, `inventory`, `category`, `best_seller`, `discount`, `product_brand` |


#### Add new category

```
  POST /api/category/
```

| Headers    | Body                             | Description                |
| :--------  | :------------------------------- | :------------------------- |
| `Authorization Token` | **required** `title`  | `slug` is created automatically from `title` field |



#### Update Product

```
  PATCH /api/products/{product_slug}/
```

| Headers               |  Body                        |
| :-------------------  | :--------------------------- |
| `Authorization Token` | Body --> data want to update |


#### Update category

```
  PUT /api/category/{title}/
```

| Headers               | Body  |
| :-------------------  | :---- |
| `Authorization Token` | title |



#### Delete Product, Delete category

```
  DELETE /api/products/{product_slug}/
```
```
  DELETE /api/category/{slug}/
```

| Headers               |                    
| :-------------------  |
| `Authorization Token` |


#### Search product, search category

```
  GET /api/products/
```

```
  GET /api/category/
```
| params   | Type  | Description                |                
| :------- | :---- | :------------------------- |
| `search` | `str` | use `product_title` or `product_brand` for search products, `title` for category |


### order app
This app for adding products to cart. every user can create only cart and add products into it. in the cart the total and the number of items are calculated.


#### Display all carts and cartitems

```
  GET /api/carts/
```
```
  GET /api/cartitems/
```


#### Delete cart

```
  DELETE /api/carts/{user-id}/
```

| Headers               |                    
| :-------------------  |
| `Authorization Token` |


#### Create cart

```
  POST /api/carts/
```
| Body      | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `id`     | **Required**. `userID`     |


#### Add item to cart

```
  POST /api/cartitems/
```
| Body      | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `id`     | **Required**. `cartID`, `product-ID`  |
