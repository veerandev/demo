# Message Board

**DEMO:** http://ec2-52-37-228-131.us-west-2.compute.amazonaws.com

### Description
MessageBoard is a simple web application built using Python, Django (a high-level web framework), Tastypie (a web service API framework for Django) and PostgreSQL database in the backend. AngularJS and HTML were used in the frontend. 


### Architecture
![architecture diagram](http://s30.postimg.org/8tqpj58ap/arc.png)

This application lets users post a message, list all the posted messages, view a selected message in detail, and delete a selected message. 

A Message class is defined in the model.py with properties user(string), content(string), creation_date(Date) and is_palindrome (boolean). The Message also has a method to check if the message is a palindrome. The data is validated by MessageManager class before creating a message.

A MessageResource class is defined in api.py to handle the RESTful requests for the Message object. The MessageResource class has the list of allowed HTTP methods and the name of the resource. The handle_resource method calls MessageManager create a Message and returns a response with appropriate status code and body.

Each request is routed to appropriate resource based on the URL pattern defined in the urls.py file.

When a POST request to create a message is received the data is validated, checked to see if it is a palindrome and saved. A response with status code is 201 is returned after successfully creating the new Message object.

A GET request to the root of the message resource will return all the messages. 

A DELETE request with the id of the Message object will delete the message and a response with status code 204 is send back. 

A GET request with an id can be used to retrieve a particular Message object.


## Sequence Diagrams
    
**Post Message**

![post message sequence diagram](http://s17.postimg.org/mm1jf61of/post.png)

**Get all Messages**

![get all message sequence diagram](http://s23.postimg.org/gfio9g4rv/get_All.png)

**Get a Message**

![get a message sequence diagram](http://s24.postimg.org/fcxsl4no5/get.png)

**Delete a Message**

![delete sequence diagram](http://s28.postimg.org/v7yvngwct/delete.png)

## API Documentation 

### Create a message [POST] [/api/v1/message/]

A message can be created by providing a JSON object containing a user and content property. The value of the user is the name of the user and content is the message body.

+ user (string) - The name of the user posting the message (required). 
+ content (string) - The content of the message (required).

+ Request (application/json)
    + Headers

            Content-Type: application/json

    + Body
        {
            "user": "Hisham",
            "content": "Qlick is Awesome"
        }

+ Response 201 (application/json)

    + Headers

            HTTP/1.0 201 CREATED
            Date: Tue, 05 Apr 2016 23:29:56 GMT
            Server: WSGIServer/0.1 Python/2.7
            Vary: Accept
            Content-Type: application/json
            Location: http://127.0.0.1:8000/api/v1/message/48/

    + Body

        {
            "content": "Qlick is Awesome",
            "creation_date": "2016-04-05T19:29:56.202000",
            "id": 48,
            "is_palindrome": false,
            "resource_uri": "/api/v1/message/48/",
            "user": "Hisham"
        }

### List All Messages [GET] [/api/v1/message/]

+ Response 200 (application/json)

    + Headers

            HTTP/1.0 200 OK
            Date: Tue, 05 Apr 2016 23:32:51 GMT
            Server: WSGIServer/0.1 Python/2.7
            Vary: Accept
            Content-Type: application/json
            Cache-Control: no-cache

    + Body

            {
                "meta": {
                    "limit": 0,
                    "offset": 0,
                    "total_count": 3
                },
                "objects": [
                    {
                      "content": "abc",
                      "creation_date": "2016-04-04T01:40:34.301000",
                      "id": 1,
                      "is_palindrome": false,
                      "resource_uri": "/api/v1/message/1/",
                      "user": "Hisham"
                    },
                    {
                      "content": "helloworld",
                      "creation_date": "2016-04-04T01:44:42.343000",
                      "id": 2,
                      "is_palindrome": false,
                      "resource_uri": "/api/v1/message/2/",
                      "user": "Veeran"
                    },
                    {
                      "content": "aba",
                      "creation_date": "2016-04-04T01:45:02.114000",
                      "id": 3,
                      "is_palindrome": true,
                      "resource_uri": "/api/v1/message/3/",
                      "user": "hisham"
                    }
                ]
            }

### View a Message Detail [GET] [/api/v1/message/{message_id}/]

+ Response 200 (application/json)

    + Headers
    
            HTTP/1.0 200 OK
            Date: Tue, 05 Apr 2016 23:36:13 GMT
            Server: WSGIServer/0.1 Python/2.7
            Vary: Accept
            Content-Type: application/json
            Cache-Control: no-cache

    + Body
            {
                "content": "Django is awesome",
                "creation_date": "2016-04-05T19:35:57.924000",
                "id": 49,
                "is_palindrome": false,
                "resource_uri": "/api/v1/message/49/",
                "user": "Hisham"
            }
        
        
### Delete a Message [DELETE] [/api/v1/message/{message_id}/]

+ Response 204 (application/json)

    + Headers
    
            HTTP/1.0 204 NO CONTENT
            Date: Tue, 05 Apr 2016 23:43:06 GMT
            Server: WSGIServer/0.1 Python/2.7
            Vary: Accept
            Content-Length: 0
            Content-Type: text/html; charset=utf-8


### Deployment

Create a AWS EC2 Ubuntu Instance with Python 2.7, open port 80 for HTTP in the security group.

1. Copy the demo project from GitHub to the Ubuntu instance. Note: All the files must be directly under the demo folder.
2. Navigate to the demo folder. Make sure the all the files are properly copied. Note: Make sure the 000-default.conf is present.
3. Run `sudo bash install_setup.sh` (you must have root access). When prompted to create super user for Django. Please type yes and provide password.
4. Now from your browser go to the public DNS of the Ubuntu instance to access the application.

