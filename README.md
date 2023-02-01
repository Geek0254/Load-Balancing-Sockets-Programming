    RUNNING THE FILES TO TEST LOAD BALANCING
Save the server code in a file called server.py.
Save the client code in a file called client.py.
On your terminal, Run the server code using "python server.py". This will start the server and listen for incoming client requests.
In a separate terminal window, run the client code using "python client.py". This will send a request to the server and print the response.
Repeat step 4 to send additional requests to the server and see how the implemented load balancing on the requests work. For instance, the first 3 servers are to be handled by server 1, the next 3 by server 2, then the next incoming requests will be distributed and handled in an alternating way by the servers.
For instance; To run the scripts in the Windows terminal, open the terminal and navigate to the directory where you saved the server.py and client.py files. Copy the files and on the terminal, change the directory by using "cd" the paste the path where the client.py and server.py are saved.
Likewise, to run on other OS such as Linux, open a terminal and navigate to the directory where you saved the files. Then, you can start the server by running the command "python server.py" then the client by tunning "python client.py"


You can use multiple instances of clients for testing on different terminals or if on the same terminal, use different windows. The instance of a server should only be one.
