# GetActive Server 
Contains the backend of the GetActive application which handles API request uses Spring Framework.

## Development Instructions

### Setup Devcontainer
1. Install [VSCode IDE](https://code.visualstudio.com/Download) then install `Dev Containers` extension.
2. Launch VSCode IDE, click on `File -> Open Folder`, then select `getactivecore` folder.
3. Type `Dev Containers: Reopen in Container` command.

Once devcontainer finished its configurations, you are now ready for development.


### Creating Docker Image
From the `backend` directory, run the following command:
```bash
docker build -t getactive/server:latest .
```

To Tag the docker image, provide the version as such:
```bash
docker build --no-cache -t getactive/server:1.0.0 .
```

 ie: To build a clean image, provide `--no-cache`.


 ### Running the Docker Image
```
docker run getactive/server:1.0.0
```