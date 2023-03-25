# OpenAI API Endpoints

This is a FastAPI app that provides the following endpoints using OpenAI API:

- `/scriptmatch`: Get the percentage of similarity and matching work of a movie script to an already existing work.
- `/movie_poster`: Create a movie poster based on a given prompt and image size.
- `/generate_fictional_character`: Generate a fictional character based on a given prompt.

## `/scriptmatch`

Get the percentage of similarity and matching work of a movie script to an already existing work.

### Request

- **HTTP Method:** `GET`
- **Endpoint:** `/scriptmatch`
- **Query Parameters:**
  - `query`: a string representing the movie script to check for similarity to an existing work.

### Response

- **Status Code:** 200 OK
- **Content Type:** application/json
- **Response Body:** 
  - `match_percentage`: a float representing the percentage of similarity of the movie script to an existing work.
  - `matching_work`: a string representing the name of the matching work, or `None` if no matching work is found.

## `/movie_poster`

Create a movie poster based on a given prompt and image size.

### Request

- **HTTP Method:** `GET`
- **Endpoint:** `/movie_poster`
- **Query Parameters:**
  - `query`: a string representing the prompt for the movie poster.
  - `ip_size`: a string representing the desired size of the image in the format "width x height".

### Response

- **Status Code:** 200 OK
- **Content Type:** application/json
- **Response Body:**
  - `image_url`: a string representing the URL of the generated movie poster image.

## `/generate_fictional_character`

Generate a fictional character based on a given prompt.

### Request

- **HTTP Method:** `GET`
- **Endpoint:** `/generate_fictional_character`
- **Query Parameters:**
  - `prompt`: a string representing the prompt for the fictional character.

### Response

- **Status Code:** 200 OK
- **Content Type:** application/json
- **Response Body:**
  - `character`: a string representing the URL of the generated fictional character image.
