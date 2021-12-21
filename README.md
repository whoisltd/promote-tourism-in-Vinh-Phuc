# Promote tourism in Vinh Phuc province

Web GIS promote tourism in Vinh Phuc province

## Demo

View demo in [here](https://promote-tourism.herokuapp.com/)

## Screenshots

![App Screenshot](/images/myWebsite.png)

## API Reference

### Get all areas

```http
  GET /api/v1/areas
```

### Get all places

```http
  GET /api/v1/places
```

### Get all services

```http
  GET /api/v1/services
```

### Get service by id

```http
  GET /api/v1/services/${id}
```

| Parameter | Type     | Description                             |
| :-------- | :------- | :-------------------------------------  |
| `id`      | `int`    | **Required**. Id of an service to fetch |

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

## Run Locally

Clone the project

```bash
  git clone https://github.com/WhoIsLTD/promote-tourism-in-Vinh-Phuc.git
```

Go to the project directory

```bash
  cd promote-tourism-in-Vinh-Phuc
```

Install packages

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  flask run
```

## Authors

- [@Dat Le](https://www.github.com/WhoIsLTD)
- [@Hoan Pham](https://www.github.com/pnghoan21)
- [@Son Vu](https://www.github.com/vuthienson8)
- [@Hanh Nguyen](https://www.github.com/Hanh263)
