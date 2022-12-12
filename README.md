# E-summit Backend

## Usage
run ```pip install -r requirements.txt ``` before using the project

Intilize reddis 

run ``` python manage.py runserver ```

## API Reference

#### signup

##### ca
```http
  POST /user/signup
```
##### json querry 
```
{
    "UserType":"ca",
    "user":{
        "full_name":"pranav arya",
        "email":"pranavleo22@gmail.com",
        "phone_number":"9833290022",
        "collage":"iit r",
        "branch":"ece",
        "year":"3rd",
        "city":"bom",
        "state":"UK",
        "password":"xxxxxx"
    }
    
}
```

#### Login

```http
  POST /user/login
```
##### json querry 
```
{
    "esummit_id":"xxxxxxxx",
    "password":"xxxxxxxxxx"
    
    
}
```


#### Events

##### list 
```http
  GET /events/all
```
##### json Response
``` 
    {
        "event_name": "ns",
        "logo_image": null,
        "card_description": ""
    }
```

##### single detail
```http
  GET /events/<str:event_name>
```




