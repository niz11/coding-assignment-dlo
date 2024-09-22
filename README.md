# Minddistrict DLO URL Generator
This project provides a Python script and a Flask server for generating Delegated Logon (DLO) URLs for Minddistrict.

## Features
1. Generates DLO URLs based on Minddistrict documentation: [DLO documentation](https://docs.minddistrict.com/delegatedlogon/index.html#prerequisites-to-generating-the-dlo-url)
2. Supports both client and care provider user types.
3. Offers optional path and redirect URL parameters for customization.


## Run the project.
This project is Dockerized for ease of use. You'll need Docker installed locally. It is also possible to run the server on your machine directly, for that an installation of Flask and Werkzeug is needed (look into requirements.txt file.)

1. Give permission for the bash script: ```chmod +x dlo.sh```
2. Add and .env file: ```touch .env```
3. Add the secret `SECRET_KEY` with it's value the .env file.
2. Run:
        ```./dlo.sh build```
        ```./dlo.sh start```
3. Visit: [Local page](http://127.0.0.1:5005)

## Flask Server
Note: User ids, Minddistricts base URL, and secret keys are pre defined for the Flask server. 
Three routes are implemented:
### Landing page (`/`): 
Here you can pick the type of user, And a path you want to go to inside the Minddistricts platform. The redirecation button will generate the DLO URL, and redirect you to the platform.

### Client Route (`/client`)
Will directly redirect you to the platform with a client DLO URL. Here you can add two query params: `path` and `redirecturl`.

### Care  Provider Route (`/careprovider`)
 Will directly redirect you to the platform with a provider DLO URL. Here you can add two query params: `path` and `redirecturl`.
Both query params needs to be URL encoded.

`path` will take you to the path within the Minddistrict platform.
`redirecturl` URL to redirect to after DLO access (URL encoded).

# Testing
## Run unit tests:
```./dlo.sh unittest```

## Manual testing
Start server, visit [http://localhost:5005/](http://localhost:5005/), and test redirecting to Minddistrict platform and being authenticated.





