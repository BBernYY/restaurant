# Created by BBernYY on https://github.com/BBernYY - The software may be allowed to be used, and modified, as long as this comment line stays here.import utils # imports my customized utils module, with a test and timing function. https://GitHub.com/BBernYY/FancyCoding
def main():
    import customer
    import json
    unhandled_requests = []
    requests = []
    while True:
        unhandled_requests -= unhandled_requests # update unhandled requests
        for i in unhandled_requests:
            requests.append(i)
            i.handled = True
            customer.send(i.user.id, i)


if __name__ == '__main__': # checks if the code is ran as a file
    while True:
        main() # starts the main function
