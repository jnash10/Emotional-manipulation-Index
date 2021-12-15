
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


def get_transcript(link):
    id = link.strip("https://www.youtube.com/watch?v=") 
    word_dic = YouTubeTranscriptApi.get_transcript(id)
    formatter = TextFormatter()
    text = formatter.format_transcript(word_dic)
    with open('transcript.txt', 'w') as text_file:
        text_file.write(text)
    



    

