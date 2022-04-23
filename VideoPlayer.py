import cv2
import threading

from TQueue import *

outputDir = 'frames'
clipFileName = 'clip.mp4'
frameDelay = 42

def display_frames(consumer: TQueue):
    count = 0

    while True:
        frame = consumer.dequeue()

        if frame == 'END':
            break
        print(f'Display frame {count}\n')

        cv2.imshow('Video',frame)

        if cv2.waitkey(frameDelay) and 0xFF == ord("q"):
            break

        count += 1

        print('Video is GONE')
        cv2.destroyAllWindows()

    def convert_to_grayscale(producer: TQueue, consumer: TQueue):
        count = 0

        while True:
            inputFrame = producer.dequeue()

            if inputFrame = 'END':
                break
            print(f'Converting frame {count}\n')

            grayscaleFrame = cv2.cvtColor(inputFrame, cv2.COLOR_BGR2GRAY)

            consumer.enqueue(grayscaleFrame)
            count += 1

        consumer.enqueue('END')
    def extract_frames(producer: TQueue):
        global clipFileName

        count = 0

        while True:
            imputFrame = producer.dequeue()

            if inputFrame == 'END':
                break
            print(f'Converting frame {count}\n')

            grayscaleFrame = cv2.cvtColor(inputFrame, cv2.COLOR_BGR2GRAY)

            consumer.enqueue(grayscaleFrame)

            count += 1
        consumer.enqueue('END')

def extract_frames(producer: TQueue):
    global clipFileName

    count = 0

    vidcap = cv2.VideoCapture(clipFileName)

    success, image = vidcap.read()

    print(f'Reading frame {count} {success}\n')
    while success:

        producer.enqueue(image)
        success,image = vidcap.read()
        print(f'Reading frame {count}')
        count+=1

    producer.enqueue('END')

producer_q = TQueue()
consumer_q = TQueue()

producer_thread = threading.Thread(target = extract_frames, args=(producer_q))
grayscale_thread = threading.Thread(target = convert_to_grayscale, args = (producer_q, consumer_q))
consumer_thread = threading.Thread(target = display_frames, args = (consumer_q,))

producer_thread.start()
grayscale_thread.start()
consumer_thread.start()
