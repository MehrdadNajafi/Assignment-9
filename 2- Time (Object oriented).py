class Time:
    def __init__(self, h, m, s):
        self.hour = h
        self.min = m
        self.sec = s
    
    def show(self):
        print(f"Result is: {self.hour}:{self.min}:{self.sec}")
    
    def SUM(self, time2):
        result = Time(None, None, None)
        result.hour = self.hour + time2.hour
        result.min = self.min + time2.min
        result.sec = self.sec + time2.sec

        if result.sec >= 60:
            result.min += result.sec // 60
            result.sec = result.sec % 60
        
        if result.min >= 60:
            result.hour += result.min // 60
            result.min = result.min % 60
        
        return result

    def Submission(self, time2):
        result = Time(None, None, None)
        result.hour = self.hour - time2.hour
        result.min = self.min - time2.min
        result.sec = self.sec - time2.sec

        while result.sec < 0 :
            result.min -= 1
            result.sec += 60
        
        while result.min < 0 :
            result.hour -= 1
            result.min += 60

        if result.hour < 0 :
            return 'This can not be calculated'
        
        else:
            return result

    def seconds_to_time(self):
        result = Time(0, 0, 0)
        result.sec = self.sec
        
        while result.sec >= 60:
            result.min += 1
            result.sec -= 60
        
        while result.min >= 60:
            result.hour += 1
            result.min -= 60

        return result

    def time_to_seconds(self):
        result = Time(0, 0, 0)
        result.sec = self.sec
        result.sec += self.min * 60
        result.sec += self.hour * 3600

        return result


    

def show_menu():
    print("1- Sum\n2- Submission\n3- Convert seconds to time\n4- Convert time to seconds\n5- Exit")

def get_input():
    time_1 = input('Please enter first time (hh:mm:ss): ')
    time_1 = time_1.split(':')
    
    time_2 = input('Please enter second time (hh:mm:ss): ')
    time_2 = time_2.split(':')

    time1 = Time(int(time_1[0]), int(time_1[1]), int(time_1[2]))
    time2 = Time(int(time_2[0]), int(time_2[1]), int(time_2[2]))

    return time1 , time2

def get_sec():
    seconds = int(input('Please enter seconds: '))
    return Time(None, None, seconds)

def get_time():
    time = input('Please enter time (hh:mm:ss): ')
    time = time.split(':')
    return Time(int(time[0]), int(time[1]), int(time[2]))


while True:
    show_menu()
    user_choice = int(input('Please choose an option: '))

    if user_choice == 1:
        time_1 , time_2 = get_input()
        time_1.SUM(time_2).show()

    elif user_choice == 2:
        time_1 , time_2 = get_input()
        try:
            time_1.Submission(time_2).show()
        except:
            print(time_1.Submission(time_2))

    elif user_choice == 3:
        sec = get_sec()
        sec.seconds_to_time().show()

    elif user_choice == 4:
        time = get_time()
        print(f"Result is: {time.time_to_seconds().sec}")

    elif user_choice == 5:
        break