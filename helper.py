from streamlit import columns
from urlextract import URLExtract
from  wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji
extract=URLExtract()

def fetch_stats(selected_user,df):
    if selected_user!='Overall':
        df = df[df['user'] == selected_user]
    #fetch the no of messages
    num_messages = df.shape[0]
    #fetch the total number of words
    words = []
    for messages in df['messages']:
        words.extend(messages.split())

    #fetch number of media messages
    num_media_messages = df[df['messages']=='<Media omitted>\n'].shape[0]
    #fetch number of links shared

    links=[]
    for messages in df['messages']:
        links.extend(extract.find_urls(messages))

    return num_messages, len(words), num_media_messages,len(links)

def most_busy_users(df):
    x=df['user'].value_counts().head()
    #percentage of busy user dataframe
    df=round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'user':'Name','count':'Percent'})

    return x,df

from wordcloud import WordCloud

def create_wordcloud(selected_user, df):
    # Filter messages for the selected user
    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    # Remove media messages, group notifications, and empty messages
    df = df[df["messages"].notna()]  # Remove empty messages
    df = df[~df["messages"].str.contains("<Media omitted>", na=False)]  # Remove media messages

    # Combine all messages into a single text
    text = " ".join(df["messages"])

    # Check if text is empty
    if not text.strip():
        return None  # Return None if no valid words are present

    # Generate the word cloud
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color="white").generate(text)
    return wc


def most_common_words(selected_user,df):

    f=open('stop_hinglish.txt','r')
    stop_words=f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    temp=df[df['user']!='group_notification']
    temp=temp[temp['messages']!='<Media omitted>\n']
    words=[]
    for messages in temp['messages']:
        for word in messages.lower().split():
            if word not in stop_words:
                words.append(word)
    most_common_df=pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def emoji_helper(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    emojis=[]
    for messages in df['messages']:
        emojis.extend([c for c in messages if c in emoji.EMOJI_DATA])
    emoji_df=pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return emoji_df



def monthly_timeline(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    timeline=df.groupby(['year','month_num','month']).count()['messages'].reset_index()
    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i]+"-"+str(timeline['year'][i]))
    timeline['time']=time
    return timeline
def week_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()
#heat map
def activity_heatmap(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    user_heatmap=df.pivot_table(index="day_name",columns='period',values='messages',aggfunc='count').fillna(0)

    return user_heatmap













