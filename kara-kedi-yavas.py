from ema_lightning import EMA

tts = EMA()                                    
speech = tts.say("Kara kedi kümese girmiş, kümesteki tavuğu ürkütmüş, tavuk kaçarken yolda kırmızı bir kediye çarpmış.", path="kara-kedi-yavas.wav", speed=0.60)

print(speech.duration, speech.sample_rate)

# most suitable for elderly people