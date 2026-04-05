#!/usr/bin/env python
# coding: utf-8

# # **TikTok Project**
# **Course 2 - Get Started with Python**

# Welcome to the TikTok Project!
# 
# You have just started as a data professional at TikTok.
# 
# The team is still in the early stages of the project. You have received notice that TikTok's leadership team has approved the project proposal. To gain clear insights to prepare for a claims classification model, TikTok's provided data must be examined to begin the process of exploratory data analysis (EDA).
# 
# A notebook was structured and prepared to help you in this project. Please complete the following questions.

# # **Course 2 End-of-course project: Inspect and analyze data**
# 
# In this activity, you will examine data provided and prepare it for analysis.
# <br/>
# 
# **The purpose** of this project is to investigate and understand the data provided. This activity will:
# 
# 1.   Acquaint you with the data
# 
# 2.   Compile summary information about the data
# 
# 3.   Begin the process of EDA and reveal insights contained in the data
# 
# 4.   Prepare you for more in-depth EDA, hypothesis testing, and statistical analysis
# 
# **The goal** is to construct a dataframe in Python, perform a cursory inspection of the provided dataset, and inform TikTok data team members of your findings.
# <br/>
# *This activity has three parts:*
# 
# **Part 1:** Understand the situation
# * How can you best prepare to understand and organize the provided TikTok information?
# 
# **Part 2:** Understand the data
# 
# * Create a pandas dataframe for data learning and future exploratory data analysis (EDA) and statistical activities
# 
# * Compile summary information about the data to inform next steps
# 
# **Part 3:** Understand the variables
# 
# * Use insights from your examination of the summary data to guide deeper investigation into variables
# 
# <br/>
# 
# To complete the activity, follow the instructions and answer the questions below. Then, you will us your responses to these questions and the questions included in the Course 2 PACE Strategy Document to create an executive summary.
# 
# Be sure to complete this activity before moving on to Course 3. You can assess your work by comparing the results to a completed exemplar after completing the end-of-course project.

# # **Identify data types and compile summary information**
# 

# Throughout these project notebooks, you'll see references to the problem-solving framework PACE. The following notebook components are labeled with the respective PACE stage: Plan, Analyze, Construct, and Execute.
# 
# # **PACE stages**
# 
# <img src="images/Pace.png" width="100" height="100" align=left>
# 
#    *        [Plan](#scrollTo=psz51YkZVwtN&line=3&uniqifier=1)
#    *        [Analyze](#scrollTo=mA7Mz_SnI8km&line=4&uniqifier=1)
#    *        [Construct](#scrollTo=Lca9c8XON8lc&line=2&uniqifier=1)
#    *        [Execute](#scrollTo=401PgchTPr4E&line=2&uniqifier=1)

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## **PACE: Plan**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response:
# 
# 

# ### **Task 1. Understand the situation**
# 
# *   How can you best prepare to understand and organize the provided information?
# 
# 
# *Begin by exploring your dataset and consider reviewing the Data Dictionary.*

# ==> ENTER YOUR RESPONSE HERE
# 
# To best prepare for this project, I will follow these strategic steps:
# 
# Review the Project Business Goal: I will start by internalizing the core mission, which is to develop a predictive model that classifies user reports as either "claims" or "opinions" to improve moderation efficiency.
# 
# Consult the Data Dictionary: I will examine the data dictionary to understand the definition and expected data type of each of the 12 variables, paying close attention to key features like claim_status, author_ban_status, and engagement metrics (views, likes, shares).
# 
# Identify Key Stakeholders: I will identify the target audience for my findings, distinguishing between technical members (Willow Jaffey, Orion Rainier) who require concise data summaries, and non-technical managers (Mary Joanna Rodgers) who need business-oriented insights.
# 
# Establish a Workflow (PACE): I will use the PACE framework to maintain a disciplined approach, beginning with this Plan stage to frame the problem before moving into Analyze for data inspection and statistical summaries.
# 
# Identify Information Gaps: During the initial inspection, I will look for missing values or structural anomalies (outliers) that might require cleaning before the model construction phase.

# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## **PACE: Analyze**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Analyze stage.

# ### **Task 2a. Imports and data loading**
# 
# Start by importing the packages that you will need to load and explore the dataset. Make sure to use the following import statements:
# *   `import pandas as pd`
# 
# *   `import numpy as np`
# 

# In[2]:


# Import packages
### YOUR CODE HERE ###
import pandas as pd
import numpy as np


# Then, load the dataset into a dataframe. Creating a dataframe will help you conduct data manipulation, exploratory data analysis (EDA), and statistical activities.
# 
# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[3]:


# Load dataset into dataframe
data = pd.read_csv("tiktok_dataset.csv")


# ### **Task 2b. Understand the data - Inspect the data**
# 
# View and inspect summary information about the dataframe by **coding the following:**
# 
# 1. `data.head(10)`
# 2. `data.info()`
# 3. `data.describe()`
# 
# *Consider the following questions:*
# 
# **Question 1:** When reviewing the first few rows of the dataframe, what do you observe about the data? What does each row represent?
# 
# **Question 2:** When reviewing the `data.info()` output, what do you notice about the different variables? Are there any null values? Are all of the variables numeric? Does anything else stand out?
# 
# **Question 3:** When reviewing the `data.describe()` output, what do you notice about the distributions of each variable? Are there any questionable values? Does it seem that there are outlier values?
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[4]:


# Display and examine the first ten rows of the dataframe
### YOUR CODE HERE ###
data.head(10)


# In[5]:


# Get summary info
### YOUR CODE HERE ###
data.info()


# In[6]:


# Get summary statistics
### YOUR CODE HERE ###
data.describe()


# ===> ENTER YOUR RESPONSE TO QUESTIONS 1-3 HERE
# 
# Question 1: When reviewing the first few rows of the dataframe, what do you observe about the data? What does each row represent?
# Response 1:
# 
# 
# Row Representation: Each row represents a unique TikTok video that has been flagged or submitted for review within the system.
# 
# 
# Initial Observations: All the initial entries in the dataset are categorized under the claim_status as "claim"].
# 
# Content and Metadata: Each record includes a unique video_id, the video_duration_sec, a video_transcription_text, the author's verified_status, and several engagement metrics like views, likes, and shares].
# 
# Transcription Patterns: The transcriptions often start with specific phrases such as "someone shared with me that...", which suggests the content is framed as sharing information or news rather than personal opinion].
# 
# Question 2: When reviewing the data.info() output, what do you notice about the different variables? Are there any null values? Are all of the variables numeric? Does anything else stand out?
# 
# Response:
# 
# Null Values: Yes, there are missing values in the dataset. While the total number of entries is 19,382, several critical columns—including claim_status, video_transcription_text, and all engagement metrics—only have 19,084 non-null values]. This indicates there are 298 rows with missing data.
# 
# Variable Types: The variables are not all numeric. The dataset consists of 5 float64 variables, 3 int64 variables, and 4 object variables (which represent text or categorical data)].
# 
# Additional Findings: The column labeled # acts as a simple row counter or index, and although video_id is stored as an integer, it serves as a unique identifier rather than a value for mathematical calculation].
# 
# 
# Question 3: When reviewing the data.describe() output, what do you notice about the distributions of each variable? Are there any questionable values? Does it seem that there are outlier values?
# 
# Response:
# 
# Distribution and Variance: There is a massive spread in engagement metrics. For instance, video_view_count ranges from a minimum of 20 to a maximum of 999,817, with a very high standard deviation (322,893), indicating a wide distribution of popularity].
# 
# Questionable Values: Video duration is consistent (5 to 60 seconds). However, it is notable that the minimum value for likes, shares, and downloads is 0.0, even for videos that may have a significant number of views].
# 
# Outliers: There is strong evidence of outliers. In the video_comment_count column, the 75th percentile is only 292, yet the maximum value jumps to 9,599]. This drastic gap between the 3rd quartile and the maximum suggests that a small number of videos receive an exceptionally high level of engagement compared to the rest of the dataset.

# ### **Task 2c. Understand the data - Investigate the variables**
# 
# In this phase, you will begin to investigate the variables more closely to better understand them.
# 
# You know from the project proposal that the ultimate objective is to use machine learning to classify videos as either claims or opinions. A good first step towards understanding the data might therefore be examining the `claim_status` variable. Begin by determining how many videos there are for each different claim status.

# In[7]:


# What are the different values for claim status and how many of each are in the data?
### YOUR CODE HERE ###
data['claim_status'].value_counts()


# **Question:** What do you notice about the values shown?
# 
# Balanced Dataset: The output shows that the counts for both categories are very similar, with 9,608 for "claim" and 9,476 for "opinion".
# 
# Class Distribution: This indicates a well-balanced dataset for the classification task, as neither class significantly outnumbers the other.
# 
# Data Integrity: The sum of these values (19,084) matches the number of non-null entries identified in the data.info() summary, confirming that the missing values do not belong to a specific hidden category in this variable.

# Next, examine the engagement trends associated with each different claim status.
# 
# Start by using Boolean masking to filter the data according to claim status, then calculate the mean and median view counts for each claim status.

# In[8]:


# What is the average view count of videos with "claim" status?
### YOUR CODE HERE ###
# 1. Crear la máscara booleana para filtrar solo los "claims"
mask_claims = data['claim_status'] == 'claim'

# 2. Aplicar la máscara al dataframe y calcular el promedio de la columna de vistas
average_view_count_claims = data[mask_claims]['video_view_count'].mean()

# 3. Mostrar el resultado
print(average_view_count_claims)


# In[9]:


# What is the average view count of videos with "opinion" status?
### YOUR CODE HERE ###
# 1. Crear la máscara booleana para filtrar solo los "opinions"
mask_opinions = data['claim_status'] == 'opinion'

# 2. Aplicar la máscara al dataframe y calcular el promedio de la columna de vistas
average_view_count_opinions = data[mask_opinions]['video_view_count'].mean()

# 3. Mostrar el resultado
print(average_view_count_opinions)


# **Question:** What do you notice about the mean and media within each claim category?
# 
# Now, examine trends associated with the ban status of the author.
# 
# Use `groupby()` to calculate how many videos there are for each combination of categories of claim status and author ban status.
# 
# Significant Disparity: There is a massive difference between the two categories. Videos categorized as "claims" have a mean view count of approximately 501,029, whereas "opinions" average only about 4,956.
# 
# Outlier Influence: For both categories, the mean is higher than the median]. This indicates that the distributions are right-skewed, confirming the presence of "viral" videos with exceptionally high view counts that pull the average upward.
# 
# Predictive Power: The fact that a "claim" is likely to have 100 times more views than an "opinion" suggests that engagement metrics will be highly effective features for our classification model.

# In[10]:


# Get counts for each group combination of claim status and author ban status
### YOUR CODE HERE ###

data.groupby(['claim_status', 'author_ban_status']).count()[['#']]


# **Question:** What do you notice about the number of claims videos with banned authors? Why might this relationship occur?
# 
# There is a much higher number of banned authors in the "claim" category (1,439) compared to the "opinion" category (196). In fact, authors of claims are more than 7 times more likely to be banned than authors of opinions.
# 
# Reasoning: This relationship likely occurs because "claims" often involve stating facts or information that can be verified. If these claims are false, misleading, or violate community guidelines (such as spreading misinformation), the authors are more likely to be reported and subsequently banned. Opinions, being subjective, are less likely to trigger policy violations.
# 
# Continue investigating engagement levels, now focusing on `author_ban_status`.
# 
# Calculate the median video share count of each author ban status.
# 
# 

# In[11]:


### YOUR CODE HERE ###

data.groupby(['author_ban_status']).median()[['video_share_count']]


# In[12]:


# What's the median video share count of each author ban status?
### YOUR CODE HERE ###

# Calculate the median video share count of each author ban status
data.groupby(['author_ban_status']).median()[['video_share_count']]


# **Question:** What do you notice about the share count of banned authors, compared to that of active authors? Explore this in more depth.
# 
# Use `groupby()` to group the data by `author_ban_status`, then use `agg()` to get the count, mean, and median of each of the following columns:
# * `video_view_count`
# * `video_like_count`
# * `video_share_count`
# 
# Remember, the argument for the `agg()` function is a dictionary whose keys are columns. The values for each column are a list of the calculations you want to perform.

# In[13]:


### YOUR CODE HERE ###

# Group by author_ban_status and calculate count, mean, and median for engagement metrics
data.groupby('author_ban_status').agg(
    {
        'video_view_count': ['count', 'mean', 'median'],
        'video_like_count': ['count', 'mean', 'median'],
        'video_share_count': ['count', 'mean', 'median']
    }
)


# **Question:** What do you notice about the number of views, likes, and shares for banned authors compared to active authors?
# 
# Now, create three new columns to help better understand engagement rates:
# * `likes_per_view`: represents the number of likes divided by the number of views for each video
# * `comments_per_view`: represents the number of comments divided by the number of views for each video
# * `shares_per_view`: represents the number of shares divided by the number of views for each video

# In[14]:


# Create a likes_per_view column
### YOUR CODE HERE ###

data['likes_per_view'] = data['video_like_count'] / data['video_view_count']

# Create a comments_per_view column
### YOUR CODE HERE ###

data['comments_per_view'] = data['video_comment_count'] / data['video_view_count']

# Create a shares_per_view column
### YOUR CODE HERE ###

data['shares_per_view'] = data['video_share_count'] / data['video_view_count']

# Mostrar las primeras filas para verificar las nuevas columnas
data.head()


# Use `groupby()` to compile the information in each of the three newly created columns for each combination of categories of claim status and author ban status, then use `agg()` to calculate the count, the mean, and the median of each group.

# In[15]:


### YOUR CODE HERE ###
# Group by claim_status and author_ban_status and calculate statistics for engagement rates
data.groupby(['claim_status', 'author_ban_status']).agg(
    {
        'likes_per_view': ['count', 'mean', 'median'],
        'comments_per_view': ['count', 'mean', 'median'],
        'shares_per_view': ['count', 'mean', 'median']
    }
)


# **Question:**
# 
# How does the data for claim videos and opinion videos compare or differ? Consider views, comments, likes, and shares.
# 
# The data reveals that 'claims' consistently generate higher engagement rates (likes, comments, and shares per view) than 'opinions', regardless of the author's status. Notably, banned authors who post 'claims' exhibit the highest engagement metrics. This suggests that high-engagement 'claim' content is a strong indicator of potential guideline violations, which is critical information for building a predictive moderation model.

# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## **PACE: Construct**
# 
# **Note**: The Construct stage does not apply to this workflow. The PACE framework can be adapted to fit the specific requirements of any project.
# 
# 
# 

# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## **PACE: Execute**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response.

# ### **Given your efforts, what can you summarize for Rosie Mae Bradshaw and the TikTok data team?**
# 
# *Note for Learners: Your answer should address TikTok's request for a summary that covers the following points:*
# 
# *   What percentage of the data is comprised of claims and what percentage is comprised of opinions?
# The dataset is almost perfectly balanced between the two primary categories:
# 
# Claims: Approximately 49.3% of the total videos.
# 
# Opinions: Approximately 50.7% of the total videos.
# 
# Strategic Insight: This balanced distribution is ideal for training future machine learning models, as it prevents bias toward one specific class.
# 
# *   What factors correlate with a video's claim status?
# The strongest factor correlating with whether a video is a "claim" is the author's account status (author_ban_status):
# 
# Videos categorized as "claims" are significantly more likely to come from authors who are "banned" or "under review".
# 
# In contrast, "opinion" videos are almost exclusively posted by "active" authors.
# 
# Conclusion: This suggests that factual assertions (claims) are the primary driver of community guideline violations on the platform.
# 
# *   What factors correlate with a video's engagement level?
# 
# Engagement is not distributed randomly; it shows a strong positive correlation with both the type of content and the author's status:
# 
# Content Type: "Claims" receive much higher views, likes, and shares than "opinions."
# 
# Viral Risk: There is a direct link between high engagement and account bans. Banned authors have a median share count 33 times higher than active authors (14,468 vs 437).
# 
# Engagement Rates: Even after normalizing for views (using the new per_view columns), videos from banned or under-review authors maintain higher interaction rates.
# 
# Data Skewness: In all categories, the mean is substantially higher than the median, confirming that the data is right-skewed by a small number of "mega-viral" outlier videos.
# 
# Final Recommendation for the Team
# Based on this EDA, the engagement metrics—specifically shares and views—along with the claim status, will be the most powerful predictors for our classification model. We should prioritize human moderation for high-velocity "claim" content, as it represents the highest risk of policy violation.

# ==> ENTER YOUR RESPONSE HERE
# The analysis of engagement rates (per view) confirms that claims generate significantly higher interaction density than opinions. Specifically, banned authors posting claims show the highest rates of engagement, suggesting that the platform's moderation system successfully identifies and penalizes high-impact, potentially violative content

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
