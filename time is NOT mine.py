# I MISS THAT KIND OF MISS ER E

import time
def lyrics(text, second,wait = 0):
    words = text.split()
    word_count = len(text.split())
    for word in words:
        print(word, end=" ", flush=True)
        time.sleep(second/word_count)
    time.sleep(wait)
    print()


print() #CHORUS
lyrics("I miss that kind of misery", 2.2,0.3)
lyrics("The kind where you are nice to me", 2.5)
lyrics("But only in the evening", 2)
lyrics("So I ask, am I just dreaming..?",2.4, 0.2)
print() #VERSE 1
lyrics("I love you so much that it's dripping",2.2, 0.2)
lyrics("Dripping from my arms and such",2.2,0.2)
lyrics("I'm sorry, I know, I'm too much",2.2)
lyrics("To love, to trust, I'm nothing but-",2,0.2)
print() #CHORUS
lyrics("I miss that kind of misery", 2.2,0.1)
lyrics("The kind where you are nice to me", 2.2)
lyrics("But only in the evening", 1.8)
lyrics("So I ask, am I just dreaming..?",2.2, 0.5)
print() #VERSE 2
lyrics("You are what I could believe in since I have nobody else", 3,.5)
lyrics("I keep screaming, I keep breathing, it's the living I can't help", 3,.7)
lyrics("It's the misery 'cause you can tell me how much that you care", 2.5,.7)
lyrics("And I know it's true, but yet you need to get me out your hairrrrrr", 2.5,.7)
print() #VERSE 2-2
lyrics("Is what we have special?", 1.2)
lyrics("What's that mean?",1.2)
lyrics("Why can't you choose me?", .7)
lyrics("is it greed?", .7)
lyrics("This isn't lust, ", 0.5)
lyrics("no fairy dust, ",.5)
lyrics("it's blunt,",.5)
lyrics("it's what you see",.5,.3)
lyrics("Misery in knowing I love you and had to leave", 2.5,.3)
lyrics("The misery that I can't shake, the misery I bleed",2.5,.3)
print() #CHORUS
lyrics("I miss that kind of misery", 2.2,0.1)
lyrics("The kind where you are nice to me", 2.2)
lyrics("But only in the evening", 1.8)
lyrics("So I ask, am I just dreaming..?",2.2, 0.3)
lyrics("But it's real, that kind of misery", 2.2,0.1)
lyrics("The kind where you are nice to me", 2.2)
lyrics("But only in the evening", 1.8)
lyrics("So I ask, am i just dreaming..?",2.2, 0.5)