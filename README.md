# Message Board

**DEMO:** http://ec2-52-37-156-40.us-west-2.compute.amazonaws.com/

### Description
MessageBoard is a simple web application built using Python, Django (a high-level web framework), Tastypie (a web service API framework for Django) and PostgreSQL database in the backend. AngularJS and HTML were used in the frontend. The application is deployed on an Ubuntu instance on AWS EC2 using mod_wsgi and Apache web server.


### Architecture
![architecture diagram](http://s30.postimg.org/8tqpj58ap/arc.png)

This application lets users post a message, list all the posted messages, view a selected message in detail, and delete a selected message. 

A Message class is defined in the model.py with properties user(string), content(string), creation_date(Date) and is_palindrome (boolean). The Message class also has a method to check if the message is a palindrome. The data is validated by MessageManager class before creating a message.

A MessageResource class is defined in api.py to handle the RESTful requests for the Message object. The MessageResource class has the list of allowed HTTP methods and the name of the resource. The get_all_or_create_resource method calls MessageManager create a Message and returns a response with appropriate status code and body. The get_or_delete_resource method return or delete a particular resource object based on the request type.

Each request is routed to appropriate resource based on the URL pattern defined in the urls.py.

A POST request to the message resource with a JSON object containing user (string) and content(string) can to create a message. When a POST request to create a message is received the data is validated, checked to see if it is a palindrome and saved. A response with status code is 201 is returned after successfully creating the new Message object.

A GET request to the root of the message resource will return all the messages and status code 200. 

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

A message can be created by providing a JSON object containing a user (string) and content (string) property. The user is the name of the user creating the message, and the content is the body of the message.

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

            HTTP/1.1 201 CREATED
            Date: Sun, 10 Apr 2016 19:29:23 GMT
            Server: Apache/2.4.7 (Ubuntu)
            Vary: Accept
            Keep-Alive: timeout=5, max=100
            Connection: Keep-Alive
            Transfer-Encoding: chunked
            Content-Type: application/json

    + Body

            [
              {
                "pk": 7,
                "model": "messageboard.message",
                "fields": {
                  "content": "Qlick is Awesome",
                  "is_palindrome": false,
                  "user": "Hisham",
                  "creation_date": "2016-04-10T19:29:23.182Z"
                }
              }
            ]

### List All Messages [GET] [/api/v1/message/]

+ Response 200 (application/json)

    + Headers

            HTTP/1.1 200 OK
            Date: Sun, 10 Apr 2016 19:35:29 GMT
            Server: Apache/2.4.7 (Ubuntu)
            Vary: Accept
            Cache-Control: no-cache
            Keep-Alive: timeout=5, max=100
            Connection: Keep-Alive
            Transfer-Encoding: chunked
            Content-Type: application/json

    + Body

            [
              {
                "pk": 5,
                "model": "messageboard.message",
                "fields": {
                  "content": "ABCB A",
                  "is_palindrome": true,
                  "user": "Hisham",
                  "creation_date": "2016-04-10T19:00:58.647Z"
                }
              },
              {
                "pk": 6,
                "model": "messageboard.message",
                "fields": {
                  "content": "123",
                  "is_palindrome": false,
                  "user": "Hisham",
                  "creation_date": "2016-04-10T19:01:11.452Z"
                }
              }
            ]

### View a Message Detail [GET] [/api/v1/message/{message_id}/]

+ Response 200 (application/json)

    + Headers
    
            HTTP/1.1 200 OK
            Date: Sun, 10 Apr 2016 19:34:01 GMT
            Server: Apache/2.4.7 (Ubuntu)
            Vary: Accept
            Cache-Control: no-cache
            Keep-Alive: timeout=5, max=100
            Connection: Keep-Alive
            Transfer-Encoding: chunked
            Content-Type: application/json

    + Body
            [
              {
                "pk": 7,
                "model": "messageboard.message",
                "fields": {
                  "content": "Qlick is Awesome",
                  "is_palindrome": false,
                  "user": "Hisham",
                  "creation_date": "2016-04-10T19:29:23.182Z"
                }
              }
            ]
        
        
### Delete a Message [DELETE] [/api/v1/message/{message_id}/]

+ Response 204 (application/json)

    + Headers
    
            HTTP/1.1 204 NO CONTENT
            Date: Sun, 10 Apr 2016 19:38:01 GMT
            Server: Apache/2.4.7 (Ubuntu)
            Vary: Accept
            Content-Length: 0
            Keep-Alive: timeout=5, max=100
            Connection: Keep-Alive
            Content-Type: application/json


### Deployment

Create an AWS EC2 Ubuntu Instance with Python 2.7, open port 80 for HTTP in the security group.

1. Copy the demo project from GitHub to the Ubuntu instance. NOTE: All the files must be directly under the demo folder.
2. Navigate to the demo folder. Make sure the all the files are properly copied. NOTE: Make sure the `000-default.conf` is present.
3. Run `sudo bash install_setup.sh` (you must have root access). When prompted to create super user for Django. Please type yes and provide password.
4. Now from your browser go to the public DNS of the Ubuntu instance to access the application.

