import pandas as pd
from convokit import Corpus, download

# Put all the dataframes together
def download_data(year_min, year_max):
    years = list(range(year_min, year_max+1))
    df_convo = pd.DataFrame()
    df_speaker = pd.DataFrame()
    df_utt = pd.DataFrame()

    for year in years:
        corpus = Corpus(filename=download("supreme-"+str(year)))

        # Dataframe for conversations
        df_convo_temp = corpus.get_conversations_dataframe()
        df_convo_temp['year'] = year
        df_convo = pd.concat([df_convo, df_convo_temp])

        # Dataframe for speakers
        df_speaker_temp = corpus.get_speakers_dataframe()
        df_speaker_temp['year'] = year
        df_speaker = pd.concat([df_speaker, df_speaker_temp])

        # Dataframe for utterances
        df_utt_temp = corpus.get_utterances_dataframe()
        df_utt_temp['year'] = year
        df_utt = pd.concat([df_utt, df_utt_temp])

    # Save the dataframes
    filename = str(year_min) + ' - ' + str(year_max) + '.csv'
    df_convo.to_csv('conversations' + filename)
    print('Conversations saved')
    df_speaker.to_csv('speakers' + filename)
    print('Speakers saved')
    df_utt.to_csv('utterances' + filename)
    print('Utterances saved')


if __name__ == "__main__":
    year_min = 2011
    year_max = 2012
    download_data(year_min, year_max)