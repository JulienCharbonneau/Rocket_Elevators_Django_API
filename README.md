# Rocket_Elevators_Django_API

This API allows you to save and retrieve facial keypoints of employees, as well as to compare an image with the images of the employees and return the matching employee.

## Endpoints

### Save Facial Keypoints
- Endpoint: `/save_key/`
- Method: `PUT`
- Enter an image on postman `form-data/Key:image,Type:file`
- Enter an ID on postman  `form-dat/Key:employee_id,Type:text` note: id are between 1 to 10.


### Retrieve Keypoints
- Endpoint: `/compare_key/`
- Method: `GET`
- Enter an image on postman `form-data/Key:image,Type:file`

Postman collection: https://api.postman.com/collections/24380917-b1ca9b88-7efd-4684-addb-5055eab5f854?access_key=PMAT-01GPKFT4KKS826WM0TJFPGTMHX

## Usage

1. First, you need to save the facial keypoints of an employee by making a PUT request to the `/save_key/` endpoint with the image of the employee and the employee_id.

2. Then, you can retrieve the keypoints of an employee by making a GET request to the `/compare_key/` endpoint with the image of the employee.

3. if the employee exist in the database and the keypoints match, the API will return the full name and title of the employee and also the id.

## Dependecies
- Python 3
- Django
- face_recognition library
