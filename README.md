# Employee Registry Service 

## Usage

All responses will have the form

```json
{
	"data":"Mixed type holding the content of the response",
	"message": "Description of what happened"
}	
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all employees

**Definition**

`GET /employees`

**Response**

- `200 OK` on success

```json
[
	{
		"employee_id":"100234",
		"name":"Prateek",
		"age":"26",
		"department":"Finance",
		"location":"Bangalore"
	},
	{
		"employee_id":"121339",
		"name":"Rahul",
		"age":"30",
		"department":"Human Resource",
		"location":"Pune"
	}
]
``` 

### Registering a new employee

**Definition**

`POST /employees`

**Arguements**

- `"employee_id":string` a globally unique identifier for this device.
- `"name":string` name of employee
- `"age":string` age of employee
- `"department":string` department of employee
- `"location":string` location of employee

If a employee with a given id already exists, the existing employee will be overwritten.

**Response**

- `201 Created` on success
```json
{
	"employee_id":"121339"
	"name":"Rahul",
	"age":"30",
	"department":"Human Resource"
	"location":"Pune"
}
``` 

## Lookup employee details

`GET /employees/<employee_id>`

**Response**

- `404 Not Found` if the employee does not exist
- `200 OK` on success

```json
{
	"employee_id":"121339",
	"name":"Rahul",
	"age":"30",
	"department":"Human Resource",
	"location":"Pune"
}
```

## Delete a employee

**Definition**

`DELETE /employees/<employee_id>

**Response**
- `404 Not found` if the employee does not exist
- `204 No content` on success