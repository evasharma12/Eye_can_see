from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Relative
from django.core.files.storage import FileSystemStorage
from .forms import UserImage

# face_recognition imports
import face_recognition
import os
from face_recognition.api import face_encodings

# Open CV
import cv2
from .simple_facerec import SimpleFacerec

# Text to speech imports
from gtts import gTTS
from playsound import playsound

user_recognizing = ""


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        global user_recognizing
        user_recognizing = username
        # print("user updated: ", user_recognizing)
        # Names_Exist = User.objects.filter(name=username)
        # if len(Names_Exist) == 0:
        #     a = User.objects.create(name=username)
        #     a.save()
        form = UserImage()
        return render(request, 'app1/index.html', {'name': username, 'form': form})
    return render(request, 'app1/login.html')


def index(request):
    username = "Guest"
    print("1")
    if request.method == "POST":
        form = UserImage(request.POST, request.FILES)
        if form.is_valid():
            formInstance = form.instance
            print(formInstance)

            form.save()
            return render(request, 'app1/login.html')
        print("2")

        return render(request, 'app1/index.html', {'name': username, 'form': form})
    else:
        form = UserImage()
        print("3")

    return render(request, 'app1/index.html', {'name': username, 'form': form})


# Function to convert the text (name of person) to audio
def textToVoice(name):
    text_val = name
    language = "en"
    # Passing the text and language to the engine,
    # here we have assign slow=False. Which denotes
    # the module that the transformed audio should
    # have a high speed
    obj = gTTS(text=text_val, lang=language, slow=False)

    # Here we are saving the transformed audio in a mp3 file named
    # exam.mp3
    obj.save("exam.mp3")

    # Play the exam.mp3 file
    playsound("exam.mp3")


person = "Unknown"


def recognize(request):
    global user_recognizing

    if len(user_recognizing) > 0:
        # Encode faces from a folder
        sfr = SimpleFacerec()
        sfr.load_encoding_images(
           "../media/images", user_recognizing)

        # Load Camera
        cap = cv2.VideoCapture(-1)

        while True:
            # Get the frame
            ret, frame = cap.read()

            # Detect faces
            # We will get face locations and face names  in return
            face_locations, face_names = sfr.detect_known_faces(frame)

            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                global person
                person = name

                # Put text "name" on the frame on the given coord, font, thickness, color
                cv2.putText(frame, name, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200))
                # make a reactangle with coords x1,y1 and x2,y2 with color red(0,0,200) and thickness of 4 px
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

            cv2.imshow("Frame", frame)

            key = cv2.waitKey(1)

            if key == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


    textToVoice(person)
    return render(request, 'app1/afterCam.html', {'name': person})


def afterCam(request):
    return render(request, 'app1/afterCam.html', {'name': person})
