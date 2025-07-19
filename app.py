import streamlit as st
import preproccesor,helper
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import streamlit as st
from PIL import Image

# Sidebar title with emoji
st.sidebar.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    .title {
        text-align: center;
        font-size: 38px; /* Increased size */
        font-weight: bold;
        font-family: 'Poppins', sans-serif;
        background: -webkit-linear-gradient(45deg, #00ff99, #0077ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        padding: 15px;
    }
    </style>
    <h1 class='title'>🚀 Chat Insider</h1>
    """,
    unsafe_allow_html=True
)

import streamlit as st

# 📂 Stylish File Uploader
st.sidebar.markdown(
    "<h2 style='color: #00FF99; text-align: center;'>📂 Upload Your WhatsApp Chat</h2>",
    unsafe_allow_html=True
)
uploaded_file = st.sidebar.file_uploader("", type=["txt"])

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preproccesor.preprocess(data)

    # 👤 Stylish User Selection
    st.sidebar.markdown(
        "<h3 style='color: #0077ff; text-align: center;'>👤 Select User</h3>",
        unsafe_allow_html=True
    )
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("", user_list)

    # 🚀 Beautiful Analysis Button
    st.sidebar.markdown(
        """
        <style>
        div.stButton > button:first-child {
            background-color: #ff6347;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px 20px;
            width: 100%;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
        }
        div.stButton > button:first-child:hover {
            background-color: #d84315;
            transition: 0.3s;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.sidebar.button("🚀 Show Analysis"):
        st.sidebar.success("✅ Processing... Please wait!")  # Feedback for users
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

        # Stylish Section Title
        st.markdown("<h1 style='text-align: center; color: #ff6347;'>📊 Top Statistics</h1>", unsafe_allow_html=True)

        # Create colored statistic cards
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown("<h3 style='text-align: center; color: #4CAF50;'>💬 Total Messages</h3>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #fff;'>{num_messages}</h2>", unsafe_allow_html=True)

        with col2:
            st.markdown("<h3 style='text-align: center; color: #2196F3;'>📝 Total Words</h3>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #fff;'>{words}</h2>", unsafe_allow_html=True)

        with col3:
            st.markdown("<h3 style='text-align: center; color: #FF9800;'>📸 Media Shared</h3>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #fff;'>{num_media_messages}</h2>", unsafe_allow_html=True)

        with col4:
            st.markdown("<h3 style='text-align: center; color: #E91E63;'>🔗 Links Shared</h3>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='text-align: center; color: #fff;'>{num_links}</h2>", unsafe_allow_html=True)

        # Add a horizontal line for better separation
        st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)

        st.title("Monthly Timeline")

        # Get the timeline data
        timeline = helper.monthly_timeline(selected_user, df)

        # Create the plot
        fig, ax = plt.subplots(figsize=(8, 4))  # Set figure size
        ax.plot(timeline['time'], timeline['messages'], marker='o', linestyle='-', color='b', label="Messages Sent")

        # Improve readability
        plt.xticks(rotation=45)  # Rotate labels for better view
        ax.set_xlabel("Month")  # Label X-axis
        ax.set_ylabel("Number of Messages")  # Label Y-axis
        ax.set_title("Monthly Messaging Activity")  # Chart title
        ax.legend()  # Show legend
        ax.grid(True, linestyle="--", alpha=0.5)  # Add grid

        # Display the plot
        st.pyplot(fig)


        #activity map
        st.title("Activity Map")
        col1,col2=st.columns(2)
        with col1:
            st.header("Most Busy Day")
            busy_day=helper.week_activity_map(selected_user, df)
            fig,ax=plt.subplots()
            ax.bar(busy_day.index,busy_day.values)
            st.pyplot(fig)
        with col2:
            st.header("Most Busy Month")

            busy_month= helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            
            st.pyplot(fig)




        st.title("Weekly Activity Map")
        user_heatmap=helper.activity_heatmap(selected_user, df)
        fig,ax=plt.subplots()
        ax=sns.heatmap(user_heatmap)


        st.pyplot(fig)















        #finding the active user most in the group(group level)

        if selected_user == 'Overall':
            st.title('Most Active Users')

            # Get data of most active users
            x, new_df = helper.most_busy_users(df)

            # Create figure
            fig, ax = plt.subplots(figsize=(8, 5))  # Increase size

            col1, col2 = st.columns(2)

            with col1:
                # Plot bar chart with better colors
                ax.bar(x.index, x.values, color='#00AB89', edgecolor='#0DFFCF')

                # Improve readability
                plt.xticks(rotation=45, ha="right")  # Rotate names for clarity
                ax.set_xlabel("Users")
                ax.set_ylabel("Number of Messages")
                ax.set_title("Top Active Users in Group")
                ax.grid(axis="y", linestyle="--", alpha=0.5)  # Add light grid

                # Display chart
                st.pyplot(fig)

            with col2:
                # Display detailed stats in a table
                st.dataframe(new_df)

        # Word Cloud Section
        st.title("Word Cloud")

        # Generate word cloud
        df_wc = helper.create_wordcloud(selected_user, df)

        # Check if the word cloud is empty
        if df_wc is None:
            st.warning(f"No words available for {selected_user}. This user may have only sent media messages.")
        else:
            # Plot the word cloud
            fig, ax = plt.subplots()
            ax.imshow(df_wc, interpolation="bilinear")
            ax.axis("off")  # Hide axis for better visualization
            st.pyplot(fig)

        #most common words
        # Most Common Words Section
        st.title("Most Common Words")

        # Get most common words
        most_common_df = helper.most_common_words(selected_user, df)

        # Check if DataFrame is empty
        if most_common_df.empty:
            st.warning("No common words found.")
        else:
            # Rename columns if needed (assuming helper function returns a DataFrame)
            most_common_df.columns = ['word', 'count']  # Ensure correct column names

            # Plot
            fig, ax = plt.subplots()
            ax.barh(most_common_df['word'], most_common_df['count'], color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        #emoji analysis


        plt.rcParams['font.family'] = 'Segoe UI Emoji'

        # Get emoji data
        emoji_df = helper.emoji_helper(selected_user, df)

        # If there are no emojis, display a message and avoid plotting
        if emoji_df.empty:
            st.title("Emoji Analysis")
            st.warning("No emojis were used by this user.")
        else:
            # Sort by highest usage and take top 10
            top_n = 10
            if len(emoji_df) > top_n:
                top_emojis = emoji_df[:top_n].copy()
                other_sum = emoji_df[top_n:][1].sum()
                top_emojis.loc[len(top_emojis)] = ["Other", other_sum]
            else:
                top_emojis = emoji_df

            st.title("Emoji Analysis")

            col1, col2 = st.columns(2)

            with col1:
                st.dataframe(emoji_df)

            with col2:
                fig, ax = plt.subplots(figsize=(7, 7))

                # Custom Colors
                colors = plt.cm.Paired.colors

                # Explode the largest section
                explode = [0.1 if i == top_emojis[1].idxmax() else 0 for i in range(len(top_emojis[1]))]

                # Plot the Pie Chart
                wedges, texts, autotexts = ax.pie(
                    top_emojis[1],
                    labels=top_emojis[0],
                    autopct=lambda p: f"{p:.1f}%" if p > 5 else "",
                    colors=colors,
                    explode=explode,
                    shadow=True,
                    startangle=140,
                    textprops={'fontsize': 12},
                    wedgeprops={'edgecolor': 'black', 'linewidth': 1}
                )

                for text in texts:
                    text.set_fontsize(12)
                    text.set_fontweight("bold")

                ax.set_title("Top Emoji Usage Distribution", fontsize=14, fontweight="bold")
                ax.axis("equal")

                st.pyplot(fig)



