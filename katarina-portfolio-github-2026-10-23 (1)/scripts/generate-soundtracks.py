# Original synthesized sound sketches for this portfolio. Requires NumPy and ffmpeg.
from pathlib import Path
import numpy as np
import wave, subprocess, tempfile

PROJECT=Path(__file__).resolve().parents[1]
OUT=PROJECT/'dist/assets/audio'
TEMP_DIR=tempfile.TemporaryDirectory(prefix='retro-tv-audio-')
TMP=Path(TEMP_DIR.name);OUT.mkdir(parents=True,exist_ok=True)
SR=32000;DURATION=32;N=SR*DURATION

def hz(midi):return 440*2**((midi-69)/12)
def add_note(track,midi,start,length,kind,level,pan=0):
    t=np.arange(int(length*SR))/SR;f=hz(midi)
    if kind=='bell':
        env=(1-np.exp(-t/0.012))*np.exp(-t/1.7)
        tone=np.sin(2*np.pi*f*t)+.20*np.sin(2*np.pi*f*2.003*t)*np.exp(-t/0.7)+.055*np.sin(2*np.pi*f*3.99*t)*np.exp(-t/0.25)
    elif kind=='pad':
        env=np.sin(np.pi*np.minimum(t/length,1))**1.8
        tone=(np.sin(2*np.pi*f*t)+.30*np.sin(2*np.pi*f*1.0016*t)+.12*np.sin(2*np.pi*f*2*t))/1.42
    else:
        env=np.sin(np.pi*np.minimum(t/length,1))**1.5
        tone=np.sin(2*np.pi*f*t)+.12*np.sin(2*np.pi*f*2*t)+.06*np.sin(2*np.pi*f*3*t)
        tone*=1+.03*np.sin(2*np.pi*.16*t)
    v=level*env*tone;idx=(int(start*SR)+np.arange(len(t)))%N
    np.add.at(track[:,0],idx,v*np.sqrt((1-pan)/2));np.add.at(track[:,1],idx,v*np.sqrt((1+pan)/2))

def finish(name,a):
    wet=np.zeros_like(a)
    for delay,level in [(.183,.15),(.373,.11),(.719,.075),(1.123,.04)]:wet+=np.roll(a[:,::-1],int(delay*SR),axis=0)*level
    a+=wet;a-=a.mean(axis=0);a*=.68/max(abs(a).max(),.001)
    pcm=(np.clip(a,-1,1)*32767).astype('<i2');p=TMP/(name+'.wav')
    with wave.open(str(p),'wb') as w:w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes(pcm.tobytes())
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(p),'-codec:a','libmp3lame','-b:a','112k','-ar','32000',str(OUT/(name+'.mp3'))],check=True)
    print(name,'seconds',DURATION,'peak',round(float(abs(a).max()),3),'rms',round(float(np.sqrt((a*a).mean())),3))

forest=np.zeros((N,2),dtype=np.float64)
for i,chord in enumerate([[50,57,62,66],[47,54,59,62],[43,50,55,59],[45,52,57,59]]):
    for j,note in enumerate(chord):add_note(forest,note,i*8,13,'pad',.075 if j==0 else .045,(j-1.5)*.22)
for i,note in enumerate([81,78,85,81,78,74,81,78]):add_note(forest,note,i*4+2,5,'bell',.012,(-1)**i*.5)
finish('forest-air',forest)

story=np.zeros((N,2),dtype=np.float64)
for i,note in enumerate([74,78,81,78,83,81,78,76,74,78,81,86,83,81,76,78]):add_note(story,note,i*2,7,'bell',.12,(-1)**i*.28)
for i,chord in enumerate([[50,57,62],[47,54,59],[43,50,55],[45,52,57]]):
    for j,note in enumerate(chord):add_note(story,note,i*8,12,'pad',.025,(j-1)*.3)
finish('storybook',story)

retro=np.zeros((N,2),dtype=np.float64)
for i,chord in enumerate([[45,52,59,60],[43,50,57,59],[41,48,55,57],[40,47,54,55]]):
    for j,note in enumerate(chord):add_note(retro,note,i*8,14,'synth',.055 if j==0 else .04,(j-1.5)*.2)
for i,note in enumerate([69,72,76,71,67,71,74,69,65,69,72,67,64,67,71,66]):add_note(retro,note,i*2+.5,4,'synth',.02,(-1)**i*.35)
finish('late-broadcast',retro)
