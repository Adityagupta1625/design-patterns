import os

class Logger:
    def log(self,message):
        pass

class ConsoleLogger(Logger):
    def log(self,message):
        print(message)

class FileLogger(Logger):
    
    def __init__(self, file):
        self.file = file

    def log(self,message):
        self.file.write(message+'\n')

class LoggerFactory:

    def create_logger(self,logger_type):
        if logger_type == "console":
            return ConsoleLogger()
        elif logger_type == "file":
            file = open("log.txt", "a") 
            return FileLogger(file)
        else:
            raise ValueError("Unsupported logger type")

factory = LoggerFactory()
console_logger = factory.create_logger("console")
file_logger = factory.create_logger("file")

console_logger.log("This is a console log message")
file_logger.log("This is a file log message")

# Remember to close the file after using it
file_logger.file.close()

# use case:
# https://www.linkedin.com/pulse/design-patterns-real-examples-go-part-2-factory-leonardo-araujo/