Let's connect to the server and see how we could feed it with new examples.

`docker run -it --link server:server -v /root:/data katacoda/tensorflow_serving bash`{{execute}}

The command run the interactive bash, links the name and connects to the server from within. We can further query it using some images.  
