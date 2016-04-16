def jimmy(a, b, **kwargs):
    print [a, b]
    return None

stuff = 'b'
stuff2 = 'flatus'
jimmy('a', 'b')
jimmy(b=stuff2, a='b')
# jimmy(stuff='a', a='b')

def shout():
    return 'loud noises'
def instance_shout(anduril='flame of the west'):
    return 'loud noises'

Jam = type('Jam',
        (object,),
        dict(
            speak='flounce',
            loud=shout,
            working_loud=instance_shout
            )
        )

def breeding(poke1, poke2):
    return type('Offspring', (type(poke1), type(poke2)))

test = Jam()
print type(Jam)
print type(test)
print test.speak
print test.working_loud()
# print test.loud()

class Flubber(object):
    def __init__(self):
        self.bouncy=True

print type(Flubber), 'class flubber'
print type(jimmy), 'standalone function'
print type(type), 'hahahaha'
print type(Flubber()), 'instance of flubber'

def delayed_doer(function):
    print 'doing!', function()

# delayed_doer(lambda x: print 'fart')
delayed_doer(shout)
