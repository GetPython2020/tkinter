from time import sleep

class Clock(object):
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def run(self):
        self.second +=1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 25:
            self.hour = 0
    def show(self):
        return f'{self.hour}:{self.minute}:{self.second}'

def main():
    clock = Clock(23,30,40)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()
if __name__ == '__main__':
    main()