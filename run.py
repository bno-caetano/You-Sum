from tokenize import Token
from core.video_transcript import Transcript
from core.text_completion import *
from utils.count_tokens import TokenCount
from core.text_completion import TextCompletion

## Transcreve video do youtube

# url = "https://www.youtube.com/watch?v=aMIt_ON4CKk" # meu timao
# url = "https://www.youtube.com/watch?v=N7_z3GABxho" # dep
url = "https://www.youtube.com/watch?v=Xv_KGUqPyx0" # canal do tf

def yt_trancript(url):
    yt_transcript = Transcript()

    id = yt_transcript.get_yt_id(url)
    transcript = yt_transcript.transcript_from_id(id)
    formatted_output = yt_transcript.format_transcript(transcript)

    return formatted_output

# Define quantidade de tokens a serem reprocessados

def tokens_proc(txt):
    tokens = TokenCount()
    num_token = tokens.count_tokens(txt)

    print('quantidade de tokens a serem processados:', num_token)
    
    return num_token

def completion(prompt, num_token):

    comp = TextCompletion(prompt=prompt, num_token=num_token)
    for response in comp.final_response():    
        yield response
