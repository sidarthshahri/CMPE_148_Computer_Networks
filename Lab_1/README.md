This zip file contains several Python source files.
They come in pairs:
- UDP:
    - UDPClient.py
    - UDPServer.py
- TCP:
    - TCPClient.py
    - TCPServer.py

Additionally, there is a Prime.py file that contains a function for checking if an input number is prime.
        
My code is heavily based off of the example in the textbook. I tried adding as many comments as possible to show that 
I understand what's happening behind the scenes and for my future reference. Otherwise, I have written all code.

To use the client-server program for either UDP or TCP, please do 
the following:
- For UDP:
    - Run UDPServer.py. This will start the UDP server which will run indefinitely.
    - Run UDPClient.py. This will initiate the client process which will ask for a number input. 
        - Note: I have not added any error checking to my code:
            - i.e. If you enter anything other than a number, my code will work unexpectedly.
    - Enter a number.
    - Observe the result.
- For TCP:
    - Run TCPServer.py. This will start the TCP server which again runs indefinitely.
    - Run TCPClient.py. This will start the client process which will ask fora number. 
        - Note: I have not added any error checking to my code:
            - i.e. If you enter anything other than a number, my code will work unexpectedly.
    - Enter a number.
    - Observe the results.
    
Test cases:
- Any number will do, but you can try the following:
    - Prime Case:
        - Enter "7" after following the steps above for either protocol:
            - The client will print the following: "From server: Number is prime! :-)"
    - Not Prime Case:
        - Enter "4" after following the steps above for either protocol:
            - The client will print the following: "From server: Number is not prime. :-("