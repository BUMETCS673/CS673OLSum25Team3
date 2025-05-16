### Running the App

##### Using the preconfigured IntelliJ run configuration:

* Click on the `GetActiveCore` run configuration in the top right corner of IntelliJ.

##### To manually run the application:

    $ ./gradlew bootRun

### Running the Tests

##### Using the preconfigured IntelliJ run configuration:

* Click on the `Tests` run configuration in the top right corner of IntelliJ.

##### To manually run the tests:

    $ ./gradlew test

### Accessing the Activity API

* Download the Postman application to test the API endpoints.
* Run the application using the instructions above.
* The activity API is available at `http://localhost:3232/v1/`.
    * `GET /v1/activities` - Retrieves all activities
    * `GET /v1/activity/{activityName}` - Retrieves list of activities which contain the given activity name