import tkinter as tk
import threading
import pyaudio
import wave

class App():
    chunk = 1024 
    sample_format = pyaudio.paInt16 
    channels = 2
    fs = 44100  
    
    frames = []  
    def __init__(self, master):
        self.isrecording = False
        self.button1 = tk.Button(main, text='rec',command=self.startrecording)
        self.button2 = tk.Button(main, text='stop',command=self.stoprecording)
        self.button1.focus()
      
        self.button1.pack()
        self.button2.pack()

    def startrecording(self):
        self.p = pyaudio.PyAudio()  
        self.stream = self.p.open(format=self.sample_format,channels=self.channels,rate=self.fs,frames_per_buffer=self.chunk,input=True)
        self.isrecording = True
        
        print('Recording')
        self.button2.focus()
        t = threading.Thread(target=self.record)
        t.start()

    def stoprecording(self):
        self.isrecording = False
        self.variable = tk.StringVar()
        self.name = tk.Entry(main, textvariable = self.variable,bg = "pink",width = 15)
        self.name.focus()
        self.name.pack()
        print('recording complete')
        
        self.button3 = tk.Button(main, text='SAVE',command=self.file_name)
        self.button3.pack()
        self.button3.focus()

    def file_name(self):
        self.filename=self.variable.get()
        self.filename = self.filename+".wav"
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        main.destroy()
    def record(self):
       
        while self.isrecording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)
		
main = tk.Tk()

main.title('Sound Recorder')
main.geometry('200x100')
app = App(main)
main.mainloop()