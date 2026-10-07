from ema_lightning import EMA

tts = EMA()                                    
speech = tts.say("Kara kedi kümese girmiş, kümesteki tavuğu ürkütmüş, tavuk kaçarken yolda kırmızı bir kediye çarpmış.", path="tekerleme.wav")

print(speech.duration, speech.sample_rate)