def announce(f):
    def wrapper():
        print("About to runa function..")
        f()
        print("Done with the function")
        return wrapper

@announce
def hello():
    print("Hello World !")
    hello()