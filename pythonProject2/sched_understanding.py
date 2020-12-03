import sched
import time
import pyttsx3

s = sched.scheduler(time.time, time.sleep)
if __name__ == "__main__":
    engine = pyttsx3.init()

def announcement(name):
    engine.say(name)
    engine.runAndWait()

e1 = s.enter(3,1, announcement,("Everyone should know, ",))
e2 = s.enter(3,1, announcement,("because it teaches you, ",))
e3 = s.enter(1,2, announcement,("how to think!",))
e4 = s.enter(1,1, announcement,("how to program a computer, ",))
s.run()