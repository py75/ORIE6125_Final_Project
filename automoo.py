#! /usr/bin/env python

import SocketServer
import socket
import sys

#Assumptions about the Bulls and Cow Games
#	1. the secret code is a 4 digit number with unique digits from 1-9
#	2. every round, each person takes turns guessing the other's secret
#	3. Simplified guessing scheme:
#			Starting from 1234, guess and if wrong, increment guess by 1
#			Minimal optimization - explained below
#MyUDPHandler class, the server, and the client functionality based off
#the code found from
#hj ttp://docs.python.org/library/socketserver.html#socketserver-udpserver-example
#
#Bulls and Cow game code based off the example found from
#http://rosettacode.org/wiki/Bulls_and_Cows#Python

class MyUDPHandler(SocketServer.BaseRequestHandler):
   def handle(self):
      data = self.request[0].strip()
      socket = self.request[1]

      if secret == '1111':	#tells other player game over
         retDat = 'LOSE'
      elif data == secret:	#correct guess
         retDat = 'WIN'
      else:				#find bulls and cows
         bulls = cows = 0
         for i in range(4):
            if data[i] == secret[i]:
               bulls += 1
            elif data[i] in secret:
               cows += 1
         retDat = '%iB%iC' % (bulls, cows)
      socket.sendto(retDat, self.client_address)

if __name__ == "__main__":
   digits = '123456789'
   endGame = 0

   if len(sys.argv) != 4: #correct number of arguments
      sys.exit('Error: Please input a secret number, local port, and opponent port.')
   #set up parameters
   secret, myPort, oppPort = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
   host = 'localhost'
   guess = 1234
   printGuess = 1234
   #check valid secret code
   if not (len(secret) == 4 and all(char in digits for char in secret) and len(set(secret)) == 4):
      sys.exit('Error, try again. You need to enter 4 unique digits from 1 to 9 for the secret')

   #set up server and client for the player
   server = SocketServer.UDPServer((host, myPort), MyUDPHandler)
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   server.timeout = 2	#2 sec server timeout
   sock.settimeout(2)	#2 sec client timeout

   myTurn = 1
   #Check to see if this is instantiated first
   #If it is the first instance, let it guess second
   try:
      sock.sendto('0000', (host, oppPort))
      received = sock.recv(1024)
   except:	#opponent server not up yet
      myTurn = 0

   while not endGame:
      if not myTurn:	#take in an opponent's guess
         myTurn = 1	#make a guess next turn
         server.handle_request()
      else:			#take a guess
         try:
            myTurn = 0		#receive a guess next turn
            sock.sendto(str(guess), (host, oppPort))
            received = sock.recv(1024)

            if received == 'WIN':
               endGame = 1
               secret = '1111'	#flag to tell other player game over
               print 'GUESS: %i' % printGuess
               print 'RETURN: '+received+'\n'
            elif received == 'LOSE':
               endGame = 1
               print 'RETURN: '+received+'\n'
            else:
               print 'GUESS: %i' % printGuess
               print 'RETURN: '+received+'\n'

            #simple guessing optimization - make sure all guesses fit in Bulls and Cow constraints
            #for this assignment, I'm not worrying about using the info gained from xBxC
            #since we start with valid guess 1234, I'm finding the next valid guess
            valid = 0
            printGuess = guess
            while not valid:
               guess += 1
               if all(char in digits for char in str(guess)) and len(set(str(guess))) == 4:
                  valid = 1
         except:	#opponent server issue - retry the guess
            continue
   server.handle_request()	#final handle requests prints out LOSE for losing player

