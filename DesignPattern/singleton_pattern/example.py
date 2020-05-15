class SpeakerV1:
    def __init__(self):
        self.__volume = 5

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SpeakerV1, cls).__new__(cls)
        return cls.instance

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, _volume):
        self.__volume = _volume


j_speaker = SpeakerV1()
y_speaker = SpeakerV1()

print(j_speaker is y_speaker)

print(j_speaker.volume)
print(y_speaker.volume)

j_speaker.volume = 10

print(j_speaker.volume)
print(y_speaker.volume)

y_speaker.volume = 20

print(j_speaker.volume)
print(y_speaker.volume)
