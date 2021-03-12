#Khai báo thư viện
#Thư viện chuyển đổi giọng nói thành văn bản
import speech_recognition
#Thư viện chuyển đổi văn bản thành giọng nói
import pyttsx3
#Thư viện ngày giờ
from datetime import date, datetime
import googletrans
from googletrans import Translator

#Khai báo biến
#Biến lưu văn bản được chuyển từ giọng nói
robot_ear = speech_recognition.Recognizer()
#Biến lưu dữ liệu được training
robot_brain = ""
#Biến lưu giọng nói được chuyển từ văn bản
robot_mouth = pyttsx3.init()
trans = Translator()


#Vòng lặp 
while True:
    #Nghe
    #Sử dụng mic để ghi dữ liệu giọng nói
    with speech_recognition.Microphone() as mic:
        #In ra dòng máy sẵn sàng ghi âm dữ liệu giọng nói
        print("Robot: I'm Listening")
        #Biến lưu dữ liệu giọng nói được lấy từ mic
        audio = robot_ear.listen(mic)
        #In ra thể hiện máy đang load dữ liệu để trả lời
        print("Robot: ...")
    #Máy load dữ liệu được ghi từ giọng nói    
    try:
        #Biến lưu dữ liệu được ghi 
        you = robot_ear.recognize_google(audio)
    #Nếu trong khi sử dụng mic có ký tự không hiểu được    
    except:
        #Biến lưu dữ liệu khi máy không hiểu từ được ghi
        you = ""
    #In ra dòng mà người dùng nói
    print("You: " + you)

    #Hiểu - AI - Training cho máy 
    #Nếu máy không hiểu người dùng nói
    if you == "":
        #Gán dữ liệu cho bộ não máy
        robot_brain = "I can't hear you, try again"
    #Trong câu nói có chữ "Hello"
    #elif "hello" in you:
        #Gán dữ liệu cho bộ não máy
        #robot_brain = "Hello Duy"
    #Trong câu nói có chữ "Today"
    #elif "today" in you:
        #Biến lưu trữ dữ liệu ngày hiện hành
        #today = date.today()
        #Gán dữ liệu ngày hiện hành cho bộ não máy với dạng cho sẵn
        #robot_brain = today.strftime("%B %d, %Y")
    #Trong câu nói có chữ "Time"
    #elif "time" in you:
        #Biến lưu trữ giờ hiện hành
        #now = datetime.now()
        #Gán dữ liệu giờ hiện hành cho bộ não máy
        #robot_brain = now.strftime("%H hours %M minutes %S seconds")
    #Trong câu nói có chữ "Bye"
    elif "bye" in you:
        #Gán dữ liệu cho bộ não máy
        robot_brain = "Bye! See you later!"
        #In dữ liệu được gán thể hiện máy trả lời câu hỏi
        print("Robot: " + robot_brain)
        #Máy trả lời qua loa máy tính
        robot_mouth.say(robot_brain)
        #Máy tiếp tục sẵn sàng nghe câu kế tiếp
        robot_mouth.runAndWait()
        #Dừng lại Project
        break
    else:
        result_trans = trans.translate(you,src="en",dest="vi")
        robot_brain = result_trans.text
        #result_trans = trans.translate(you,src="vi",dest="en")
        #robot_brain = result_trans.text
        
    #Nói
    #In dữ liệu được gán thể hiện máy trả lời câu hỏi
    print("Robot: " + robot_brain)
    #Máy trả lời qua loa máy tính
    robot_mouth.say(robot_brain)
    #Máy tiếp tục sẵn sàng nghe câu kế tiếp
    robot_mouth.runAndWait()