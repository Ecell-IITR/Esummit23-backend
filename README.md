# E-summit Backend

## Usage
run ```pip install -r requirements.txt ``` before using the project




This is the backend of E-summit 2023


## Acknowledgements

- [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)

## Authors

- Ishika
- Divya
- Kiran
- Vinay
- Divyanshu

## Tech Stack

**Client:** React, TailwindCSS,Bootstrap

**Server:** Django


## API Reference


#### Login

##### ca
```http
  POST /user/login
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

#### Get Color

```http
  GET /design/colors/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `NONE` | `string` | **Required**. NA |

#### Get Team

```http
  GET /public/team/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `NONE`      | `string` | **Required**. NA |



#### Get Speakers
```http
  GET /public/Speakers/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `NONE`      | `string` | **Required**. NA |


```


