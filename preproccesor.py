import re
import pandas as pd
def preprocess(data):
    pattern = r"\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s?[ap]m\s-\s"

    data = data.replace("\u202f", "")
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    if len(messages) != len(dates):
        min_length = min(len(messages), len(dates))
        messages = messages[:min_length]
        dates = dates[:min_length]

    # ✅ Create DataFrame
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # ✅ 1. Remove ' - ' from the extracted date
    df['message_date'] = df['message_date'].str.replace(r' - $', '', regex=True)

    # ✅ 2. Fix missing space in AM/PM (Fix "4:38pm " → "4:38 pm")
    df['message_date'] = df['message_date'].str.replace(r'(\d)([apAP][mM])', r'\1 \2', regex=True)

    # ✅ 3. Convert to datetime format
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %I:%M %p', errors='coerce')

    # ✅ 4. Rename column
    df.rename(columns={'message_date': 'date'}, inplace=True)
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df['user'] = users
    df['messages'] = messages
    df.drop(columns=['user_message'], inplace=True)
    df['month_num']=df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['day_name']=df['date'].dt.day_name()
    period=[]
    for hour in df[['day_name','hour']]['hour']:
        if hour==23:
            period.append(str(hour)+"-"+str('00'))
        elif hour==0:
            period.append(str('00')+"-"+str(hour+1))
        else:
            period.append(str(hour)+"-"+str(hour+1))
    df['period']=period



    return df





