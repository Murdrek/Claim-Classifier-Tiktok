#!/usr/bin/env python
# coding: utf-8

# # **TikTok Project**
# **Course 2 - Go Beyond the Numbers: Translate Data into Insights**

# Your TikTok data team is still in the early stages of their latest project. So far, you’ve completed a project proposal and used Python to inspect and organize the TikTok dataset.
# 
# Orion Rainier, a Data Scientist at TikTok, is pleased with the work you have already completed and is requesting your assistance with some Exploratory Data Analysis (EDA) and data visualization. The management team asked to see a Python notebook showing data structuring and cleaning, as well as any matplotlib/seaborn visualizations plotted to help us understand the data. At the very least, include a graph comparing claim counts to opinion counts, as well as boxplots of the most important variables (like “video duration,” “video like count,” “video comment count,” and “video view count”) to check for outliers. Also, include a breakdown of “author ban status” counts.
# 
# Additionally, the management team has recently asked all EDA to include Tableau visualizations. Tableau visualizations are particularly helpful in status reports to the client and board members. For this data, create a Tableau dashboard showing a simple claims versus opinions count, as well as stacked bar charts of claims versus opinions for variables like video view counts, video like counts, video share counts, and video download counts. Make sure it is easy to understand to someone who isn’t data savvy, and remember that the assistant director is a person with visual impairments.
# 
# You also notice a follow-up email from the Data Science Lead, Willow Jaffey. Willow suggests including an executive summary of your analysis to share with teammates.
# 
# A notebook was structured and prepared to help you in this project. Please complete the following questions.

# # **Course 2 End-of-course project: Exploratory data analysis**
# 
# In this activity, you will examine data provided and prepare it for analysis. You will also design a professional data visualization that tells a story, and will help data-driven decisions for business needs.
# 
# Please note that the Tableau visualization activity is optional, and will not affect your completion of the course. Completing the Tableau activity will help you practice planning out and plotting a data visualization based on a specific business need. The structure of this activity is designed to emulate the proposals you will likely be assigned in your career as a data professional. Completing this activity will help prepare you for those career moments.
# <br/>
# 
# **The purpose** of this project is to conduct exploratory data analysis on a provided data set. Your mission is to continue the investigation you began in C1 and perform further EDA on this data with the aim of learning more about the variables. Of particular interest is information related to what distinguishes claim videos from opinion videos.
# 
# **The goal** is to explore the dataset and create visualizations.
# <br/>
# *This activity has 4 parts:*
# 
# **Part 1:** Imports, links, and loading
# 
# **Part 2:** Data Exploration
# *   Data cleaning
# 
# 
# **Part 3:** Build visualizations
# 
# **Part 4:** Evaluate and share results

# Follow the instructions and answer the question below to complete the activity. Then, you will complete an executive summary using the questions listed on the PACE Strategy Document.
# 
# Be sure to complete this activity before moving on. The next course item will provide you with a completed exemplar to compare to your own work.

# # **Visualize a story in Tableau and Python**

# <img src="images/Pace.png" width="100" height="100" align=left>
# 
# # **PACE stages**

# Throughout these project notebooks, you'll see references to the problem-solving framework PACE. The following notebook components are labeled with the respective PACE stage: Plan, Analyze, Construct, and Execute.

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## **PACE: Plan**
# 
# Consider the questions in your PACE Strategy Document and those below where applicable to craft your response:
# 1. Identify any outliers:
# 
# 
# *   What methods are best for identifying outliers?
# *   How do you make the decision to keep or exclude outliers from any future models?
# 
# 

# ==> ENTER YOUR RESPONSE HERE
# 
# PACE: Plan - Outlier Identification & Strategy
# 1. Methods for Identifying Outliers / Métodos para Identificar Valores Atípicos
# EN: * Boxplots: Visual representation to quickly identify points beyond the whiskers (1.5×IQR).
# 
# Interquartile Range (IQR): A statistical method where we calculate the difference between the third quartile (Q3) and the first quartile (Q1).
# 
# Z-Score: Measuring how many standard deviations a data point is from the mean, useful for normally distributed data.
# 
# ES:Diagramas de caja (Boxplots): Representación visual para identificar rápidamente puntos más allá de los "bigotes" (1.5×IQR).
# 
# Rango Intercuartílico (IQR): Método estadístico donde calculamos la diferencia entre el tercer cuartil (Q3) y el primer cuartil (Q1).
# 
# Z-Score: Mide cuántas desviaciones estándar se aleja un punto de la media, útil para datos con distribución normal.
# 
# 2. Decision Making: Keep or Exclude? / Toma de Decisiones: ¿Mantener o Excluir?
# EN:Decision to Keep: We will keep outliers if they represent genuine user behavior. In TikTok, "viral" videos (extreme views/likes) are organic and essential to distinguish "claims" from "opinions." Removing them could lead to a biased model.
# 
# Decision to Exclude/Transform: We will exclude outliers if they result from data entry errors (e.g., negative counts). If extreme values distort the model, we may use capping (setting a maximum threshold) or log transformations to normalize the scale.
# 
# ES:Decisión de Mantener: Mantendremos los valores atípicos si representan un comportamiento genuino del usuario. En TikTok, los videos "virales" (vistas/likes extremos) son orgánicos y esenciales para distinguir "reclamaciones" de "opiniones". Eliminarlos podría generar un modelo sesgado.
# 
# Decisión de Excluir o Transformar: Excluiremos los valores atípicos si resultan de errores de entrada de datos (ej. conteos negativos). Si los valores extremos distorsionan el modelo, podemos usar capping (establecer un umbral máximo) o transformaciones logarítmicas para normalizar la escala.
# 
# 3. Executive Summary Snippet / Fragmento para el Resumen Ejecutivo
# EN: "We will prioritize keeping organic outliers in engagement metrics to ensure the model captures the full spectrum of viral 'claim' content, applying transformations only where extreme skewness hinders model convergence."
# 
# ES: "Priorizaremos mantener los valores atípicos orgánicos en las métricas de interacción para asegurar que el modelo capture todo el espectro de contenido viral de 'reclamación', aplicando transformaciones solo donde la asimetría extrema dificulte la convergencia del modelo."

# ### **Task 1. Imports, links, and loading**
# Go to Tableau Public
# The following link will help you complete this activity. Keep Tableau Public open as you proceed to the next steps.
# 
# Link to supporting materials:
# Public Tableau: https://public.tableau.com/s/. Note that the TikTok dataset can be downloaded directly from this notebook by going to "Lab Files" in the menu bar at the top of the page, clicking into the "/home/jovyan/work" folder, selecting `tiktok_dataset.csv`, and clicking "Download" above the list of files. 
# 
# For EDA of the data, import the packages that would be most helpful, such as `pandas`, `numpy`, `matplotlib.pyplot`, and `seaborn`.
# 

# In[3]:


# Import packages for data manipulation
### YOUR CODE HERE ###
import pandas as pd
import numpy as np

# Import packages for data visualization
### YOUR CODE HERE ###
import matplotlib.pyplot as plt
import seaborn as sns


# Then, load the dataset into a dataframe. Read in the data and store it as a dataframe object.
# 
# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.
# 

# In[4]:


# Load dataset into dataframe
data = pd.read_csv("tiktok_dataset.csv")


# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## **PACE: Analyze**
# 
# Consider the questions in your PACE Strategy Document and those below where applicable to complete your code.

# ### **Task 2a: Data exploration and cleaning**
# 
# The first step is to assess your data. Check the Data Source page on Tableau Public to get a sense of the size, shape and makeup of the data set.
# 
# Consider functions that help you understand and structure the data.
# 
# *    `.head()`
# *    `.info()`
# *    `.describe()`
# *    `.groupby()`
# *    `.sort_values()`
# 
# Consider the following questions as you work:
# 
# What do you do about missing data (if any)?
# 
# Are there data outliers?
# 
# 1. What do you do about missing data? / ¿Qué hacer con los datos faltantes?
# EN:
# 
# Identification: First, use data.isna().sum() to quantify missing values per column.
# Assessment: If the missing values are a small percentage (e.g., < 5%) and are "Missing Completely at Random" (MCAR), we can drop those rows to maintain a clean dataset for the model.
# TikTok Context: If claim_status is missing, we cannot use that row for supervised learning, so dropping them is often the best path. However, if engagement metrics are missing, we could consider imputation (filling with the median) to avoid losing too much data.
# EN: "There are 298 missing values in engagement metrics (approx. 1.5% of the data). Since this is a small percentage, we can safely drop these rows to ensure model quality."
# 
# ES:Identificación: Primero, usamos data.isna().sum() para cuantificar los valores faltantes por columna.
# Evaluación: Si los valores faltantes son un porcentaje pequeño (ej. < 5%) y son "completamente al azar", podemos eliminar esas filas para mantener un dataset limpio para el modelo.
# Contexto de TikTok: Si falta el claim_status, no podemos usar esa fila para el aprendizaje supervisado, por lo que eliminarlas suele ser lo mejor. Sin embargo, si faltan métricas de interacción, podríamos considerar la imputación (llenar con la mediana) para no perder demasiada información.
# ES: "Hay 298 valores faltantes en las métricas de interacción (aprox. 1.5% de los datos). Dado que es un porcentaje pequeño, podemos eliminar estas filas de forma segura para garantizar la calidad del modelo."
# 
# 2. Are there data outliers? / ¿Existen valores atípicos en los datos?
# EN: Detection: Based on the .describe() table, we compare the mean to the median (50%) and check the maximum values. If the max is significantly higher than the 75th percentile, outliers are present.
# TikTok Context: In social media, outliers are expected (viral videos). We will use boxplots for video_view_count, video_like_count, and video_share_count to visualize them.
# Action: We will not automatically delete them, as viral videos might be the most important "claims" to report. We may apply logarithmic transformations to normalize the distribution for the model.
# 
# EN: "Confirmed. There is significant right-skewness in engagement metrics. The high gap between the median (50%) and the maximum values across all engagement columns confirms the presence of viral outliers."
# 
# ES:Detección: Basándonos en la tabla de .describe(), comparamos la media con la mediana (50%) y revisamos los valores máximos. Si el máximo es significativamente mayor que el percentil 75, hay valores atípicos.
# Contexto de TikTok: En redes sociales, los outliers son esperados (videos virales). Usaremos boxplots para video_view_count, video_like_count y video_share_count para visualizarlos.
# Acción: No los eliminaremos automáticamente, ya que los videos virales podrían ser las "reclamaciones" más importantes a reportar. Podríamos aplicar transformaciones logarítmicas para normalizar la distribución de cara al modelo.
# 
# ES: "Confirmado. Existe una asimetría a la derecha significativa en las métricas de interacción. La gran diferencia entre la mediana (50%) y los valores máximos en todas las columnas de interacción confirma la presencia de valores atípicos (outliers) virales."
# 

# Start by discovering, using `.head()`, `.size`, and `.shape`.

# In[5]:


# Display and examine the first few rows of the dataframe
### YOUR CODE HERE ###
# 1. Visualizar las primeras filas para entender la estructura
print("Primeras 5 filas del dataset:")
display(data.head())


# In[6]:


# Get the size of the data
### YOUR CODE HERE ###
# Get the size of the data
data.size


# In[7]:


# Get the shape of the data
### YOUR CODE HERE ###
# Get the shape of the data
data.shape


# Get basic information about the data, using `.info()`.

# In[8]:


# Get basic information about the data
### YOUR CODE HERE ###

data.info()


# Generate a table of descriptive statistics, using `.describe()`.

# In[7]:


# Generate a table of descriptive statistics
### YOUR CODE HERE ###

data.describe()


# ### **Task 2b. Assess data types**

# In Tableau, staying on the data source page, double check the data types of the columns in the dataset. Refer to the dimensions and measures in Tableau.
# 

# Review the instructions linked in the previous Activity document to create the required Tableau visualization.

# ### **Task 2c. Select visualization type(s)**

# Select data visualization types that will help you understand and explain the data.
# 
# Now that you know which data columns you’ll use, it is time to decide which data visualization makes the most sense for EDA of the TikTok dataset. What type of data visualization(s) would be most helpful? Consider the distribution of the data.
# 
# * Line graph
# * Bar chart
# * Box plot
# * Histogram
# * Heat map
# * Scatter plot
# * A geographic map
# 

# ==> ENTER YOUR RESPONSE HERE
# 
# EN: For this EDA, I select Bar Charts, Box Plots, and Histograms.
# 
# Bar Charts: Essential for comparing the total volume of engagement (views, likes, shares) across different categories like claim_status or author_ban_status.
# 
# Box Plots: Crucial for identifying outliers. In social media data, viral videos create extreme values; box plots allow us to visualize these outliers and decide how to handle them for the model.
# 
# Histograms: Necessary to understand the distribution of the data. Given the nature of TikTok, we expect a significant right-skewed distribution, which histograms will clearly illustrate.
# 
# ES: Para este EDA, selecciono Gráficos de Barras, Diagramas de Caja (Box Plots) e Histogramas.
# 
# Gráficos de Barras: Esenciales para comparar el volumen total de interacción (vistas, likes, compartidos) entre diferentes categorías como claim_status o author_ban_status.
# 
# Box Plots: Cruciales para identificar valores atípicos (outliers). En datos de redes sociales, los videos virales crean valores extremos; los box plots nos permiten visualizar estos valores y decidir cómo manejarlos para el modelo.
# 
# Histogramas: Necesarios para entender la distribución de los datos. Dada la naturaleza de TikTok, esperamos una distribución significativamente sesgada a la derecha, la cual los histogramas ilustrarán claramente.

# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## **PACE: Construct**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Construct stage.

# ### **Task 3. Build visualizations**
# 
# Now that you have assessed your data, it’s time to plot your visualization(s).

# #### **video_duration_sec**
# 
# Create a box plot to examine the spread of values in the `video_duration_sec` column.

# In[9]:


# Create a boxplot to visualize distribution of `video_duration_sec`
### YOUR CODE HERE ##

# Configurar el estilo visual
sns.set_theme(style="whitegrid")

# Crear el boxplot para visualizar la distribución de `video_duration_sec`
plt.figure(figsize=(6,2)) # Definimos un tamaño ajustado para una sola variable
plt.title('Box Plot: Distribución de la duración del video (segundos)')
sns.boxplot(x=data['video_duration_sec'])

plt.show()


# Technical Analysis: Video Duration Box Plot
# Análisis Técnico: Box Plot de Duración de Video
# EN:Uniform Distribution: The box plot shows a remarkably uniform distribution. The median sits around 32 seconds, with the interquartile range (the blue box) spanning from approximately 18 to 48 seconds.
# 
# No Outliers: Unlike engagement metrics (views or likes), the video_duration_sec column contains no outliers. Every video in the dataset falls within the 5 to 60-second range, which is standard for short-form content.
# 
# Data Integrity: This indicates that the duration data is clean and does not require specialized capping or trimming before being used in a machine learning model.
# 
# ES:Distribución Uniforme: El box plot muestra una distribución notablemente uniforme. La mediana se sitúa alrededor de los 32 segundos, con el rango intercuartílico (la caja azul) abarcando aproximadamente desde los 18 hasta los 48 segundos.
# 
# Sin Valores Atípicos (Outliers): A diferencia de las métricas de interacción (vistas o likes), la columna video_duration_sec no contiene outliers. Cada video en el dataset cae dentro del rango de 5 a 60 segundos, lo cual es el estándar para contenido de formato corto.
# 
# Integridad de Datos: Esto indica que los datos de duración están limpios y no requieren de recortes o tratamientos especiales antes de ser utilizados en un modelo de machine learning.

# Create a histogram of the values in the `video_duration_sec` column to further explore the distribution of this variable.

# In[10]:


# Create a histogram
### YOUR CODE HERE ###
# Create a histogram to visualize distribution of `video_duration_sec`
plt.figure(figsize=(8, 4))
sns.histplot(data['video_duration_sec'], bins=range(0, 61, 5), kde=False, color='skyblue', edgecolor='black')

plt.title('Histograma: Distribución de la Duración del Video / Video Duration Distribution')
plt.xlabel('Duración en segundos / Duration (sec)')
plt.ylabel('Cantidad de videos / Count')

plt.show()


# Technical Analysis: Video Duration Histogram
# Análisis Técnico: Histograma de Duración de Video
# EN:
# 
# Uniform Distribution: The histogram shows that all bins (intervals of 5 seconds) have a similar height, with approximately 1,500 to 1,600 videos per interval. This is a classic "Uniform Distribution" where every outcome has an equal probability of occurring.
# 
# Balanced Data: There is no "spike" or predominant duration. Whether a video lasts 10, 30, or 55 seconds, it appears with the same frequency in this dataset.
# 
# Insight: Since the duration is so evenly spread, it likely won't be the strongest predictor on its own for determining if a video is a "claim" or "opinion," as both categories likely share these varied durations.
# 
# ES:
# 
# Distribución Uniforme: El histograma muestra que todas las barras (intervalos de 5 segundos) tienen una altura similar, con aproximadamente 1,500 a 1,600 videos por intervalo. Esta es una clásica "Distribución Uniforme" donde cada resultado tiene la misma probabilidad de ocurrir.
# 
# Datos Balanceados: No hay un "pico" o duración predominante. Ya sea que un video dure 10, 30 o 55 segundos, aparece con la misma frecuencia en este conjunto de datos.
# 
# Conclusión: Dado que la duración está tan uniformemente distribuida, es probable que por sí sola no sea el predictor más fuerte para determinar si un video es una "reclamación" o una "opinión", ya que ambas categorías probablemente comparten estas duraciones variadas.

# **Question:** What do you notice about the duration and distribution of the videos?
# 
# Analysis of Video Duration and Distribution
# Análisis de la Duración y Distribución de los Videos
# EN:
# 
# Duration: The videos are constrained to a specific range, between 5 and 60 seconds. The median duration is approximately 32 seconds, indicating a well-defined limit for the content in this dataset.
# 
# Distribution: The distribution is Uniform. Unlike many real-world variables that follow a Bell Curve (Normal Distribution), every duration interval has an almost equal number of videos. This means there is no "preferred" length for the videos; a 10-second video is just as common as a 60-second one.
# 
# ES:
# 
# Duración: Los videos están limitados a un rango específico, entre 5 y 60 segundos. La duración mediana es de aproximadamente 32 segundos, lo que indica un límite bien definido para el contenido en este conjunto de datos.
# 
# Distribución: La distribución es Uniforme. A diferencia de muchas variables del mundo real que siguen una Campana de Gauss (Distribución Normal), cada intervalo de duración tiene casi la misma cantidad de videos. Esto significa que no hay una longitud "preferida" para los videos; un video de 10 segundos es tan común como uno de 60 segundos.

# #### **video_view_count**
# 
# Create a box plot to examine the spread of values in the `video_view_count` column.

# In[11]:


# Create a boxplot to visualize distribution of `video_view_count`
### YOUR CODE HERE ###

# Create a boxplot to visualize distribution of `video_view_count`
plt.figure(figsize=(7,2))
plt.title('Box Plot: Distribución de Vistas de Video / Video View Count Distribution')
sns.boxplot(x=data['video_view_count'])

plt.show()


# Technical Analysis: Video View Count Distribution
# Análisis Técnico: Distribución de Conteos de Vistas
# EN:
# 
# Extremely Wide Distribution: The box is stretched across the entire range, from 0 to nearly 1,000,000 views (10 
# 6).
# 
# Right-Skewed Behavior: Although there are no dots (outliers) beyond the whiskers, the median (the center line) is positioned slightly to the left, and the whiskers are very long. This shows that while many videos have low views, many others reach nearly a million.
# 
# No Outliers: Interestingly, the dataset is "capped" at 1 million views. Because the data is so spread out but contained within this limit, the whiskers extend to the full range, resulting in zero statistical outliers.
# 
# ES:
# 
# Distribución Extremadamente Amplia: La caja se estira a lo largo de todo el rango, desde 0 hasta casi 1,000,000 de vistas (10 
# 6).
# 
# Comportamiento Sesgado a la Derecha: Aunque no hay puntos (outliers) más allá de los bigotes, la mediana (la línea central) está posicionada ligeramente a la izquierda y los bigotes son muy largos. Esto muestra que, aunque muchos videos tienen pocas vistas, muchos otros alcanzan casi el millón.
# 
# Sin Outliers: Curiosamente, el conjunto de datos está "limitado" a 1 millón de vistas. Debido a que los datos están tan dispersos pero contenidos dentro de este límite, los bigotes se extienden a todo el rango, resultando en cero valores atípicos estadísticos.

# Create a histogram of the values in the `video_view_count` column to further explore the distribution of this variable.

# In[12]:


# Create a histogram
### YOUR CODE HERE ###
# Create a histogram to visualize distribution of `video_view_count`
plt.figure(figsize=(8, 4))
sns.histplot(data['video_view_count'], bins=range(0, 1000001, 100000), kde=False, color='salmon', edgecolor='black')

plt.title('Histograma: Distribución de Vistas de Video / Video View Count Distribution')
plt.xlabel('Cantidad de Vistas / View Count')
plt.ylabel('Cantidad de videos / Count')

plt.show()


# Technical Analysis: Video View Count Histogram
# Análisis Técnico: Histograma de Conteo de Vistas
# EN:
# 
# Uniform Distribution: The histogram shows a very flat distribution. Every bin (representing intervals of 100,000 views) has a similar frequency, with approximately 1,900 to 2,000 videos each.
# 
# Data Characteristics: This confirms that the dataset was likely constructed to represent all levels of popularity equally, from 0 to 1 million views. In a natural social media environment, you would usually see a "long tail" (most videos having very few views), but here, high-view videos are just as common as low-view ones.
# 
# Modeling Implication: For your model, this means it will be trained on a very balanced set of performance metrics, which helps prevent bias toward only popular or only unpopular content.
# 
# ES:
# 
# Distribución Uniforme: El histograma muestra una distribución muy plana. Cada intervalo (que representa bloques de 100,000 vistas) tiene una frecuencia similar, con aproximadamente 1,900 a 2,000 videos cada uno.
# 
# Características de los Datos: Esto confirma que el dataset probablemente fue construido para representar todos los niveles de popularidad por igual, de 0 a 1 millón de vistas. En un entorno natural de redes sociales, normalmente verías una "cola larga" (la mayoría de los videos con muy pocas vistas), pero aquí, los videos de muchas vistas son tan comunes como los de pocas.
# 
# Implicación para el Modelo: Para tu modelo, esto significa que será entrenado en un conjunto muy equilibrado de métricas de rendimiento, lo que ayuda a prevenir sesgos hacia solo contenido popular o solo impopular.

# **Question:** What do you notice about the distribution of this variable?
# 
# Analysis of Video View Count Distribution
# Análisis de la Distribución del Conteo de Vistas
# EN:
# 
# Uniform Distribution: The variable video_view_count follows a uniform distribution. This is evident because each "bin" in the histogram has approximately the same number of observations (around 2,000 videos per 100k views interval).
# 
# Wide but Balanced Range: The data spans from 0 to 1,000,000 views. Unlike typical social media data—which is usually heavily "right-skewed" (meaning most videos have few views and only a few go viral)—this dataset has been balanced so that high-view videos are represented just as much as low-view videos.
# 
# No Outliers: Due to this uniform spread and the clear 1-million-view cap, the box plot shows no statistical outliers.
# 
# ES:
# 
# Distribución Uniforme: La variable video_view_count sigue una distribución uniforme. Esto es evidente porque cada "barra" en el histograma tiene aproximadamente la misma cantidad de observaciones (alrededor de 2,000 videos por cada intervalo de 100k vistas).
# 
# Rango Amplio pero Equilibrado: Los datos abarcan desde 0 hasta 1,000,000 de vistas. A diferencia de los datos típicos de redes sociales —que suelen estar fuertemente "sesgados a la derecha" (lo que significa que la mayoría de los videos tienen pocas vistas y solo unos pocos se vuelven virales)— este conjunto de datos ha sido equilibrado para que los videos de muchas vistas estén representados tanto como los de pocas vistas.
# 
# Sin Valores Atípicos (Outliers): Debido a esta dispersión uniforme y al límite claro de 1 millón de vistas, el box plot no muestra valores atípicos estadísticos.

# #### **video_like_count**
# 
# Create a box plot to examine the spread of values in the `video_like_count` column.

# In[13]:


# Create a boxplot to visualize distribution of `video_like_count`
### YOUR CODE HERE ###

# Create a boxplot to visualize distribution of `video_like_count`
plt.figure(figsize=(10, 3))
plt.title('Box Plot: Distribución de Likes de Video / Video Like Count Distribution')
sns.boxplot(x=data['video_like_count'])

plt.show()


# Technical Analysis: Video Like Count Distribution
# Análisis Técnico: Distribución de Likes de Video
# EN:
# 
# Right-Skewed Distribution: The "box" (interquartile range) is heavily shifted to the left, near zero. This indicates that a vast majority of videos have a relatively low number of likes.
# 
# Presence of Outliers: You can see a long line of individual dots extending far to the right. These are the outliers. In this context, they represent highly viral videos that received an exceptional amount of engagement compared to the median.
# 
# Concentration: Most of the data is concentrated below 100,000 likes, while the outliers stretch all the way to 600,000+ likes.
# 
# ES:
# 
# Distribución Sesgada a la Derecha: La "caja" (rango intercuartílico) está fuertemente desplazada hacia la izquierda, cerca del cero. Esto indica que la gran mayoría de los videos tienen una cantidad relativamente baja de likes.
# 
# Presencia de Outliers (Valores Atípicos): Puedes ver una línea larga de puntos individuales que se extienden hacia la derecha. Estos son los outliers. En este contexto, representan videos altamente virales que recibieron una interacción excepcional en comparación con la mediana.
# 
# Concentración: La mayoría de los datos se concentran por debajo de los 100,000 likes, mientras que los outliers se extienden hasta superar los 600,000 likes.

# Create a histogram of the values in the `video_like_count` column to further explore the distribution of this variable.

# In[14]:


# Create a histogram
### YOUR CODE HERE ###
# Create a histogram to visualize distribution of `video_like_count`
plt.figure(figsize=(10, 5))
sns.histplot(data['video_like_count'], bins=range(0, 700001, 100000), color='lightgreen', edgecolor='black')

plt.title('Histograma: Distribución de Likes de Video / Video Like Count Distribution')
plt.xlabel('Cantidad de Likes / Like Count')
plt.ylabel('Cantidad de videos / Count')

plt.show()


# Technical Analysis: Video Like Count Histogram
# Análisis Técnico: Histograma de Likes de Video
# EN:
# 
# Right-Skewed Distribution: The data is heavily concentrated on the left. The first bin (0 to 100,000 likes) contains more than 12,000 videos, which is roughly 60% of the entire dataset.
# 
# Rapid Decay: There is a sharp drop-off in frequency as the number of likes increases. Very few videos reach the higher tiers (400k-700k likes).
# 
# Significance: This suggests that "liking" is a much more selective action than "viewing." While many videos get views, only a specific subset (likely the claims) generates the high engagement seen in the tail of the histogram.
# 
# ES:
# 
# Distribución Sesgada a la Derecha: Los datos están fuertemente concentrados a la izquierda. El primer intervalo (0 a 100,000 likes) contiene más de 12,000 videos, lo que representa aproximadamente el 60% de todo el dataset.
# 
# Caída Rápida: Hay una disminución abrupta en la frecuencia a medida que aumenta el número de likes. Muy pocos videos alcanzan los niveles superiores (400k-700k likes).
# 
# Significado: Esto sugiere que dar "like" es una acción mucho más selectiva que "ver". Mientras que muchos videos obtienen vistas, solo un subconjunto específico (probablemente las reclamaciones) genera la alta interacción que se ve en la "cola" del histograma.

# **Question:** What do you notice about the distribution of this variable?
# 
# Analysis of Video Like Count DistributionAnálisis de la Distribución del Conteo de Likes
# 
# EN:Right-Skewed Distribution: Unlike the uniform distribution observed in views, video_like_count is clearly right-skewed.
# 
# Concentration at the Low End: The vast majority of videos (over $60\%$) are clustered in the first bin, receiving between 0 and 100,000 likes.
# 
# Presence of Outliers: The distribution has a "long tail" that extends toward 700,000 likes. These represent the viral outliers we saw in the box plot. This indicates that high engagement is the exception, not the rule, for most content in this dataset.
# 
# ES:Distribución Sesgada a la Derecha: A diferencia de la distribución uniforme observada en las vistas, video_like_count está claramente sesgada a la derecha.
# 
# Concentración en el Extremo Inferior: La gran mayoría de los videos (más del $60\%$) se agrupan en el primer intervalo, recibiendo entre 0 y 100,000 likes.
# 
# Presencia de Outliers: La distribución tiene una "cola larga" que se extiende hacia los 700,000 likes. Estos representan los valores atípicos virales que vimos en el box plot e indican que una alta interacción es la excepción, no la regla, para la mayoría del contenido en este conjunto de datos.

# #### **video_comment_count**
# 
# Create a box plot to examine the spread of values in the `video_comment_count` column.

# In[15]:


# Create a boxplot to visualize distribution of `video_comment_count`
### YOUR CODE HERE ###
# Create a boxplot to visualize distribution of `video_comment_count`
plt.figure(figsize=(10, 3))
plt.title('Box Plot: Distribución de Comentarios de Video / Video Comment Count Distribution')
sns.boxplot(x=data['video_comment_count'])

plt.show()


# Technical Analysis: Video Comment Count Distribution
# Análisis Técnico: Distribución de Comentarios de Video
# EN:
# 
# Massive Right-Skew: The box plot shows that the vast majority of videos have nearly zero comments. The "box" itself is almost invisible because the median and the first/third quartiles are all concentrated at the very low end of the scale.
# 
# Extreme Outliers: There is a very dense "tail" of outliers extending toward 9,500 comments. This indicates that while the average video gets almost no conversation, a small number of videos trigger an explosion of comments.
# 
# Moderate vs. High Engagement: Most videos have a comment count that doesn't even reach 2,000, but the outliers create a long horizontal line that characterizes a "Power Law" distribution.
# 
# ES:
# 
# Sesgo a la Derecha Masivo: El box plot muestra que la gran mayoría de los videos tienen casi cero comentarios. La "caja" en sí es casi invisible porque la mediana y el primer/tercer cuartil están concentrados en el extremo más bajo de la escala.
# 
# Outliers Extremos: Hay una "cola" muy densa de valores atípicos que se extiende hacia los 9,500 comentarios. Esto indica que, mientras que el video promedio casi no genera conversación, un pequeño número de videos provoca una explosión de comentarios.
# 
# Interacción Moderada vs. Alta: La mayoría de los videos tienen un conteo de comentarios que ni siquiera llega a los 2,000, pero los outliers crean una línea horizontal larga que caracteriza una distribución de "Ley de Potencia".

# Create a histogram of the values in the `video_comment_count` column to further explore the distribution of this variable.

# In[16]:


# Create a histogram
### YOUR CODE HERE ###
# Create a histogram to visualize distribution of `video_comment_count`
plt.figure(figsize=(8, 4))
sns.histplot(data['video_comment_count'], bins=range(0, 10001, 1000), color='orange', edgecolor='black')

plt.title('Histograma: Distribución de Comentarios de Video / Video Comment Count Distribution')
plt.xlabel('Cantidad de Comentarios / Comment Count')
plt.ylabel('Cantidad de videos / Count')

plt.show()


# Technical Analysis: Video Comment Count Histogram
# Análisis Técnico: Histograma de Comentarios de Video
# EN:
# 
# Extreme Skewness: The distribution is heavily concentrated in the first bin (0–1,000 comments). In fact, the frequency is so high in that first interval (nearly 14,000 videos) that the rest of the bins are barely visible on the scale.
# 
# Engagement Rareness: This proves that while videos are watched (Uniform views), meaningful engagement like commenting is very rare. Most videos attract minimal discussion.
# 
# The Viral Threshold: The very small bars reaching toward 10,000 comments represent the "Engagement Gold" or "Controversy Spikes" that the Orion project is designed to flag for review.
# 
# ES:
# 
# Asimetría Extrema: La distribución está fuertemente concentrada en el primer intervalo (0–1,000 comentarios). De hecho, la frecuencia es tan alta en ese primer bloque (casi 14,000 videos) que el resto de los intervalos son apenas visibles en la escala.
# 
# Rareza de la Interacción: Esto demuestra que, aunque los videos se ven (vistas uniformes), la interacción significativa como comentar es muy rara. La mayoría de los videos atraen una discusión mínima.
# 
# El Umbral Viral: Las barras muy pequeñas que se extienden hacia los 10,000 comentarios representan el "Oro de Interacción" o "Picos de Controversia" que el proyecto Orion está diseñado para marcar para revisión.

# **Question:** What do you notice about the distribution of this variable?
# 
# "The distribution of video_comment_count is heavily right-skewed. The vast majority of videos receive between 0 and 1,000 comments, while a tiny fraction of highly engaging videos creates a long tail that extends to nearly 10,000 comments."
# 
# (La distribución de video_comment_count está fuertemente sesgada a la derecha. La gran mayoría de los videos reciben entre 0 y 1,000 comentarios, mientras que una pequeña fracción de videos con alta interacción crea una cola larga que se extiende hasta casi los 10,000 comentarios).

# #### **video_share_count**
# 
# Create a box plot to examine the spread of values in the `video_share_count` column.

# In[17]:


# Create a boxplot to visualize distribution of `video_share_count`
### YOUR CODE HERE ###
# Create a boxplot to visualize distribution of `video_share_count`
plt.figure(figsize=(10, 3))
plt.title('Box Plot: Distribución de Videos Compartidos / Video Share Count Distribution')
sns.boxplot(x=data['video_share_count'])

plt.show()


# Technical Analysis: Video Share Count Distribution
# Análisis Técnico: Distribución de Videos Compartidos
# EN:
# 
# Right-Skewed Distribution: The "box" is extremely compressed on the left side of the chart, near zero. This indicates that the vast majority of videos are shared very few times.
# 
# Significant Outliers: There is a heavy density of outliers (the individual dots) stretching across the entire x-axis up to 250,000 shares.
# 
# Viral Magnitude: Although the number of shares is lower in absolute terms compared to likes or views, the presence of so many outliers suggests that when a video "breaks out," it does so aggressively.
# 
# ES:
# 
# Distribución Sesgada a la Derecha: La "caja" está extremadamente comprimida en el lado izquierdo del gráfico, cerca del cero. Esto indica que la gran mayoría de los videos se comparten muy pocas veces.
# 
# Outliers Significativos: Hay una alta densidad de valores atípicos (los puntos individuales) que se extienden por todo el eje x hasta los 250,000 compartidos.
# 
# Magnitud Viral: Aunque el número de compartidos es menor en términos absolutos comparado con likes o vistas, la presencia de tantos outliers sugiere que cuando un video "explota", lo hace de manera muy agresiva.

# *Create* a histogram of the values in the `video_share_count` column to further explore the distribution of this variable.

# In[18]:


# Create a histogram
### YOUR CODE HERE ###
# Create a histogram to visualize distribution of `video_share_count`
plt.figure(figsize=(8, 4))
sns.histplot(data['video_share_count'], bins=range(0, 270001, 10000), color='mediumpurple', edgecolor='black')

plt.title('Histograma: Distribución de Videos Compartidos / Video Share Count Distribution')
plt.xlabel('Cantidad de Compartidos / Share Count')
plt.ylabel('Cantidad de videos / Count')

plt.show()


# Technical Analysis: Video Share Count Histogram
# Análisis Técnico: Histograma de Videos Compartidos
# EN:
# 
# Heavily Right-Skewed: The distribution follows the same pattern as likes and comments, but it is even more concentrated. The first bin (0 to 25,000 shares) contains nearly 18,000 videos, representing about 90% of the data.
# 
# Low Engagement Baseline: This visualization highlights that "sharing" is a rare event for the majority of content. Most videos never cross the 25,000 shares mark.
# 
# The "Viral" Outliers: The very sparse bars stretching toward 250,000 shares represent the small fraction of content that achieves mass virality. These are the high-impact videos that are most likely to be flagged as "claims".
# 
# ES:
# 
# Fuertemente Sesgado a la Derecha: La distribución sigue el mismo patrón que los likes y comentarios, pero está aún más concentrada. El primer intervalo (0 a 25,000 compartidos) contiene casi 18,000 videos, lo que representa aproximadamente el 90% de los datos.
# 
# Base de Interacción Baja: Esta visualización resalta que "compartir" es un evento raro para la mayoría del contenido. La mayor parte de los videos nunca cruzan la marca de los 25,000 compartidos.
# 
# Outliers "Virales": Las barras muy dispersas que se extienden hacia los 250,000 compartidos representan la pequeña fracción de contenido que logra una viralidad masiva. Estos son los videos de alto impacto que tienen más probabilidades de ser marcados como "claims" (reclamaciones).

# **Question:** What do you notice about the distribution of this variable?
# "The distribution of video_share_count is heavily right-skewed. The vast majority of observations are clustered in the 0–25,000 range, with a long, thin tail extending to 250,000 shares. This indicates that high sharing counts are exceptional and limited to a very small subset of videos."
# 
# (La distribución de video_share_count está fuertemente sesgada a la derecha. La gran mayoría de las observaciones se agrupan en el rango de 0–25,000, con una cola larga y delgada que se extiende hasta los 250,000 compartidos. Esto indica que los conteos altos de compartidos son excepcionales y se limitan a un subconjunto muy pequeño de videos).

# #### **video_download_count**
# 
# Create a box plot to examine the spread of values in the `video_download_count` column.

# In[19]:


# Create a boxplot to visualize distribution of `video_download_count`
### YOUR CODE HERE ###
# Create a boxplot to visualize distribution of `video_download_count`
plt.figure(figsize=(10, 3))
plt.title('Box Plot: Distribución de Descargas de Video / Video Download Count Distribution')
sns.boxplot(x=data['video_download_count'])

plt.show()


# Technical Analysis: Video Download Count Distribution
# Análisis Técnico: Distribución de Descargas de Video
# EN:
# 
# Strong Right-Skew: The box is heavily compressed against the zero mark. This indicates that for the majority of videos, downloading is an uncommon action.
# 
# Outlier Density: There is a significant number of outliers extending toward 15,000 downloads. Interestingly, the density of these outliers seems high throughout the range, suggesting that while rare, there is a consistent subset of content that users find valuable enough to save.
# 
# High-Value Indicator: Downloads often represent the highest level of user intent. In the context of the Orion project, videos with 10k+ downloads are primary candidates for high-priority classification.
# 
# ES:
# 
# Fuerte Sesgo a la Derecha: La caja está fuertemente comprimida contra la marca del cero. Esto indica que para la gran mayoría de los videos, la descarga es una acción poco común.
# 
# Densidad de Outliers: Hay una cantidad significativa de valores atípicos que se extienden hacia las 15,000 descargas. Curiosamente, la densidad de estos outliers parece alta en todo el rango, lo que sugiere que, aunque es raro, hay un subconjunto consistente de contenido que los usuarios consideran lo suficientemente valioso como para guardarlo.
# 
# Indicador de Alto Valor: Las descargas suelen representar el nivel más alto de intención del usuario. En el contexto del proyecto Orion, los videos con más de 10,000 descargas son candidatos principales para una clasificación de alta prioridad.
# 
# Question: What do you notice about the distribution of this variable?
# 
# "The distribution of video_download_count is right-skewed. The majority of videos have very few downloads, but a long tail of outliers extends up to 15,000, identifying a small group of highly 'saveable' content."
# 
# (La distribución de video_download_count está sesgada a la derecha. La mayoría de los videos tienen muy pocas descargas, pero una cola larga de outliers se extiende hasta las 15,000, identificando un pequeño grupo de contenido altamente 'guardable').

# Create a histogram of the values in the `video_download_count` column to further explore the distribution of this variable.

# In[20]:


# Create a histogram
### YOUR CODE HERE ###
# Create a histogram to visualize distribution of `video_download_count`
plt.figure(figsize=(8, 4))
sns.histplot(data['video_download_count'], bins=range(0, 15001, 1000), color='teal', edgecolor='black')

plt.title('Histograma: Distribución de Descargas de Video / Video Download Count Distribution')
plt.xlabel('Cantidad de Descargas / Download Count')
plt.ylabel('Cantidad de videos / Count')

plt.show()


# Technical Analysis: Video Download Count Histogram
# Análisis Técnico: Histograma de Descargas de Video
# EN:
# 
# Extreme Right-Skew: The distribution is heavily skewed to the right. The first bin (0–1,000 downloads) contains approximately 18,000 videos, which is the vast majority of the dataset.
# 
# The "Viral" Long Tail: Beyond the first bin, the frequency drops significantly. Only a very small fraction of videos reach the 10,000–15,000 download range.
# 
# Key Insight: Downloading is a high-intent action. The fact that the distribution is so concentrated at the low end confirms that while many people watch videos (as seen in the uniform views), very few videos are deemed valuable enough to be saved by users.
# 
# ES:
# 
# Sesgo a la Derecha Extremo: La distribución está fuertemente sesgada a la derecha. El primer intervalo (0–1,000 descargas) contiene aproximadamente 18,000 videos, que es la gran mayoría del conjunto de datos.
# 
# La "Cola Larga" Viral: Más allá del primer intervalo, la frecuencia cae significativamente. Solo una fracción muy pequeña de videos alcanza el rango de 10,000–15,000 descargas.
# 
# Conclusión Clave: Descargar es una acción de alta intención. El hecho de que la distribución esté tan concentrada en el extremo inferior confirma que, aunque mucha gente ve los videos (como se vio en las vistas uniformes), muy pocos videos son considerados lo suficientemente valiosos por los usuarios como para ser guardados.

# **Question:** What do you notice about the distribution of this variable?
# 
# "The distribution of video_download_count is heavily right-skewed. Nearly all observations are clustered between 0 and 1,000 downloads, with an extremely thin tail extending to 15,000. This reinforces the pattern that high-engagement actions are rare and highly concentrated in a small subset of videos."
# 
# (La distribución de video_download_count está fuertemente sesgada a la derecha. Casi todas las observaciones se agrupan entre 0 y 1,000 descargas, con una cola extremadamente delgada que se extiende hasta las 15,000. Esto refuerza el patrón de que las acciones de alta interacción son raras y están muy concentradas en un pequeño subconjunto de videos).

# #### **Claim status by verification status**
# 
# Now, create a histogram with four bars: one for each combination of claim status and verification status.

# In[21]:


# Calcular porcentajes de verificación para cada tipo de contenido
counts = data.groupby(['claim_status', 'verified_status']).size().unstack()
proportions = counts.div(counts.sum(axis=1), axis=0) * 100

print(proportions)


# In[22]:


# Create a histogram
### YOUR CODE HERE ###
# Create a histogram with four bars (combination of claim and verification status)
plt.figure(figsize=(7, 4))
sns.histplot(data=data, 
             x='claim_status', 
             hue='verified_status', 
             multiple='dodge', 
             shrink=0.9)

plt.title('Claim Status by Verification Status / Estado de Reclamación por Estado de Verificación')
plt.xlabel('Estado de Reclamación / Claim Status')
plt.ylabel('Cantidad de Videos / Count')
plt.show()


# Technical Analysis: Claim Status vs. Verification Status
# Análisis Técnico: Estado de Reclamación vs. Verificación
# EN:
# 
# Unverified Users and Claims: There is a disproportionately high number of unverified users associated with claims. Notice how the "not verified" bar for claims is significantly taller than the "verified" bar in the same category.
# 
# Verified Users and Opinions: Conversely, verified users are much more likely to be associated with opinions than with claims.
# 
# Imbalance for Modeling: This suggests that verified_status is a strong predictor for claim_status. For the Orion model, an unverified account might be a "red flag" when trying to identify potential claims that need moderation.
# 
# ES:
# 
# Usuarios No Verificados y Reclamaciones: Hay una cantidad desproporcionadamente alta de usuarios no verificados asociados con reclamaciones (claims). Observa cómo la barra de "no verificado" para claims es significativamente más alta que la barra de "verificado" en la misma categoría.
# 
# Usuarios Verificados y Opiniones: Por el contrario, es mucho más probable que los usuarios verificados estén asociados con opiniones que con reclamaciones.
# 
# Desequilibrio para el Modelado: Esto sugiere que verified_status es un predictor fuerte para claim_status. Para el modelo de Orion, una cuenta no verificada podría ser una "bandera roja" al intentar identificar reclamos potenciales que necesitan moderación.

# **Question:** What do you notice about the number of verified users compared to unverified? And how does that affect their likelihood to post opinions?
# 
# 1. Number of Verified vs. Unverified Users
# 1. Cantidad de Usuarios Verificados vs. No Verificados
# 
# EN: There is a massive disproportion in the volume of users. Unverified users (Not Verified) make up the vast majority of the dataset. This is expected in social media, where the "verified" badge is a restricted status granted only to a small fraction of the population.
# 
# ES: Hay una desproporción masiva en el volumen de usuarios. Los usuarios no verificados representan la gran mayoría del conjunto de datos. Esto es de esperar en las redes sociales, donde la insignia de "verificado" es un estatus restringido otorgado solo a una pequeña fracción de la población.
# 
# 2. Likelihood to Post Opinions
# 2. Probabilidad de Publicar Opiniones
# 
# EN: Verified users have a significantly higher relative likelihood to post opinions. Looking at the chart, you can see that for verified accounts, the "opinion" bar is much taller than the "claim" bar. They seem to focus on subjective content, which is safer and less likely to be flagged for moderation.
# 
# ES: Los usuarios verificados tienen una probabilidad relativa significativamente mayor de publicar opiniones. Al observar el gráfico, se ve que para las cuentas verificadas, la barra de "opinión" es mucho más alta que la de "reclamación". Parecen centrarse en contenido subjetivo, que es más seguro y menos propenso a ser marcado para moderación.
# 
# 3. The "Claim" Dominance in Unverified Accounts
# 3. El Dominio de las "Reclamaciones" en Cuentas No Verificadas
# 
# EN: Almost all "claims" in the dataset are posted by unverified users. This creates a very strong correlation: if the user is unverified, the chance that the video is a factual "claim" (and thus a candidate for moderation) increases drastically.
# 
# ES: Casi todas las "reclamaciones" (claims) en el dataset son publicadas por usuarios no verificados. Esto crea una correlación muy fuerte: si el usuario no está verificado, la probabilidad de que el video sea una "reclamación" fáctica (y por tanto un candidato para moderación) aumenta drásticamente.
# 
# Impact on the Orion Model / Impacto en el Modelo Orion
# The "Bias" Risk (EN): Because the data shows that unverified users post almost all the claims, the model might learn to "distrust" unverified accounts automatically. As a data scientist, you must monitor if the model is ignoring the content of the video and simply flagging it based on the user's badge.
# 
# El Riesgo de "Sesgo" (ES): Debido a que los datos muestran que los usuarios no verificados publican casi todas las reclamaciones, el modelo podría aprender a "desconfiar" de las cuentas no verificadas automáticamente. Como científico de datos, debes monitorear si el modelo ignora el contenido del video y simplemente lo marca basándose en la insignia del usuario.

# #### **Claim status by author ban status**
# 
# The previous course used a `groupby()` statement to examine the count of each claim status for each author ban status. Now, use a histogram to communicate the same information.

# In[23]:


# Calcular porcentajes de baneo para cada tipo de contenido
ban_counts = data.groupby(['claim_status', 'author_ban_status']).size().unstack()
ban_proportions = ban_counts.div(ban_counts.sum(axis=1), axis=0) * 100

print(ban_proportions)


# In[24]:


# Create a histogram
### YOUR CODE HERE ###
# Create a histogram to visualize claim_status by author_ban_status
plt.figure(figsize=(7, 4))
sns.histplot(data=data, 
             x='claim_status', 
             hue='author_ban_status', 
             multiple='dodge', 
             hue_order=['active', 'under review', 'banned'],
             shrink=0.9)

plt.title('Estado de Reclamación por Estado de Baneo / Claim Status by Author Ban Status')
plt.xlabel('Estado de Reclamación / Claim Status')
plt.ylabel('Cantidad de Videos / Count')
plt.show()


# **Question:** What do you notice about the number of active authors compared to banned authors for both claims and opinions?
# 
# Technical Analysis: Claims and Account Sanctions
# Análisis Técnico: Reclamaciones y Sanciones de Cuenta
# 1. The Safety of Opinions / La Seguridad de las Opiniones
# 
# EN: Look at the "opinion" bars. The overwhelming majority of authors are active (the blue bar). There are almost no "banned" or "under review" authors in this category. This confirms that sharing personal views is generally safe and doesn't violate community guidelines.
# 
# ES: Mira las barras de "opinion". La gran mayoría de los autores están activos (la barra azul). Casi no hay autores "baneados" o "bajo revisión" en esta categoría. Esto confirma que compartir puntos de vista personales es generalmente seguro y no viola las normas de la comunidad.
# 
# 2. The Risk of Claims / El Riesgo de las Reclamaciones
# 
# EN: Now look at the "claim" bars. While many are still active, the proportion of banned (green) and under review (orange) authors increases dramatically. Claims are far more likely to be associated with accounts that have been penalized.
# 
# ES: Ahora mira las barras de "claim". Aunque muchos siguen activos, la proporción de autores baneados (verde) y bajo revisión (naranja) aumenta drásticamente. Es mucho más probable que las reclamaciones estén asociadas con cuentas que han sido penalizadas.
# 
# 3. Why this matters / Por qué esto importa
# 
# EN: This visualization proves that there is a "signal" in the data: problematic content (claims) is already being caught by TikTok's systems, leading to bans. Our model will use this history to predict future violations.
# 
# ES: Esta visualización demuestra que hay una "señal" en los datos: el contenido problemático (reclamaciones) ya está siendo detectado por los sistemas de TikTok, lo que lleva a baneos. Nuestro modelo usará este historial para predecir violaciones futuras.
# 
# "There is a stark difference between the two. Authors of opinions are rarely banned, maintaining a mostly active status. In contrast, authors of claims show a significantly higher rate of being banned or under review, indicating that factual claims are the primary source of policy violations."
# 
# Hay una diferencia marcada entre ambos. Los autores de opiniones rara vez son baneados, manteniendo un estado mayoritariamente activo. Por el contrario, los autores de reclamaciones muestran una tasa significativamente mayor de estar baneados o bajo revisión, lo que indica que las afirmaciones fácticas son la fuente principal de violaciones de las políticas.

# #### **Median view counts by ban status**
# 
# Create a bar plot with three bars: one for each author ban status. The height of each bar should correspond with the median number of views for all videos with that author ban status.

# In[26]:


# Create a bar plot
### YOUR CODE HERE ###

import numpy as np

# Create a bar plot to visualize median video_view_count by author_ban_status
plt.figure(figsize=(7, 4))
sns.barplot(data=data, 
            x='author_ban_status', 
            y='video_view_count', 
            estimator=np.median, 
            order=['active', 'under review', 'banned'],
            palette='magma',
            ci=None)  # <--- Cambiamos errorbar por ci

plt.title('Mediana de Vistas por Estado de Baneo / Median Views by Author Ban Status')
plt.xlabel('Estado de Baneo / Author Ban Status')
plt.ylabel('Mediana de Vistas / Median View Count')

plt.show()


# **Question:** What do you notice about the median view counts for non-active authors compared to that of active authors? 
# Bilingual Response:
# "The median view counts for banned authors and those under review are drastically higher than for active authors. This suggests that videos which violate policies (leading to bans) often achieve significant viral reach before being moderated."
# 
# Las vistas medianas para autores baneados y bajo revisión son drásticamente más altas que para los autores activos. Esto sugiere que los videos que violan las políticas (llevando a baneos) a menudo logran un alcance viral significativo antes de ser moderados.
# 
# Based on that insight, what variable might be a good indicator of claim status?
# EN: > "The video_view_count is the most effective predictive variable. Claims generate a level of engagement that opinions simply do not reach. When combined with verified_status, these variables will likely form the backbone of the Orion classification model."
# 
# ES: > "El video_view_count es la variable predictiva más efectiva. Las reclamaciones generan un nivel de interacción que las opiniones simplemente no alcanzan. Al combinarse con verified_status, estas variables probablemente formarán la columna vertebral del modelo de clasificación Orion."
# 
# Technical Analysis: Median View Counts
# Análisis Técnico: Mediana de Vistas
# 1. Massive Disparity / Disparidad Masiva
# 
# EN: The visual difference is shocking. The median views for active accounts are so low that the bar is barely visible compared to the others. Meanwhile, banned and under review accounts show huge bars, both exceeding 400,000 views.
# 
# ES: La diferencia visual es impactante. Las vistas medianas de las cuentas activas son tan bajas que la barra apenas es visible en comparación con las demás. Mientras tanto, las cuentas baneadas y bajo revisión muestran barras enormes, ambas superando las 400,000 vistas.
# 
# 2. The "Viral Claim" Phenomenon / El Fenómeno de la "Reclamación Viral"
# 
# EN: This confirms that videos containing claims (factual assertions) tend to go viral much faster and more broadly than simple opinions. Unfortunately, this also means they reach a huge audience before the author is caught and banned.
# 
# ES: Esto confirma que los videos que contienen reclamaciones (afirmaciones de hechos) tienden a volverse virales mucho más rápido y ampliamente que las simples opiniones. Desafortunadamente, esto también significa que alcanzan a una audiencia enorme antes de que el autor sea detectado y baneado.
# 
# 3. Strategic Importance for Orion / Importancia Estratégica para Orion
# 
# EN: If we only moderated videos with a low view count, we would be missing the most "dangerous" or influential content. The model must prioritize these high-view videos from unverified or suspicious authors.
# 
# ES: Si solo moderáramos videos con un recuento bajo de vistas, nos estaríamos perdiendo el contenido más "peligroso" o influyente. El modelo debe priorizar estos videos de muchas vistas provenientes de autores no verificados o sospechosos.

# In[27]:


# Calculate the median view count for claim status.
### YOUR CODE HERE ###
# Calculate the median view count for each claim status
data.groupby('claim_status')[['video_view_count']].median()


# In[28]:


### YOUR CODE HERE ###
# Get medians for all engagement metrics by claim status
data.groupby('claim_status')[['video_view_count', 'video_like_count', 'video_share_count', 'video_download_count', 'video_comment_count']].median()


# 

# #### **Total views by claim status**
# 
# Create a pie graph that depicts the proportions of total views for claim videos and total views for opinion videos.

# In[29]:


# Create a pie graph
### YOUR CODE HERE ###
# Create a pie graph to depict the proportions of total views for claim videos and opinion videos
plt.figure(figsize=(6, 6))
plt.pie(data.groupby('claim_status')['video_view_count'].sum(), 
        labels=['Claim', 'Opinion'], 
        autopct='%1.1f%%', 
        colors=['#ff9999','#66b3ff'])

plt.title('Proporción de Vistas Totales por Estado / Proportion of Total Views by Claim Status')
plt.show()


# **Question:** What do you notice about the overall view count for claim status?
# 
# Análisis Técnico Bilingüe / Bilingual Technical Analysis
# 1. The Dominance of Claims / El Dominio de las Reclamaciones
# 
# EN: The pie chart shows that claims account for almost 99% of the total views in the dataset. Even if the number of videos were balanced, the actual reach of claims is vastly superior.
# 
# ES: El gráfico de pastel muestra que las reclamaciones representan casi el 99% de las vistas totales en el conjunto de datos. Incluso si el número de videos estuviera equilibrado, el alcance real de las reclamaciones es masivamente superior.
# 
# 2. Opinion "Invisibility" / La "Invisibilidad" de las Opiniones
# 
# EN: The "opinion" slice is tiny (around 1%). This tells us that personal opinions rarely go viral. They stay within small circles or are simply not promoted by the algorithm as much as factual-sounding claims.
# 
# ES: La rebanada de "opinión" es diminuta (alrededor del 1%). Esto nos dice que las opiniones personales rara vez se vuelven virales. Se quedan en círculos pequeños o simplemente el algoritmo no las promociona tanto como las reclamaciones que suenan a hechos.

# ### **Task 4. Determine outliers**
# 
# When building predictive models, the presence of outliers can be problematic. For example, if you were trying to predict the view count of a particular video, videos with extremely high view counts might introduce bias to a model. Also, some outliers might indicate problems with how data was captured or recorded.
# 
# The ultimate objective of the TikTok project is to build a model that predicts whether a video is a claim or opinion. The analysis you've performed indicates that a video's engagement level is strongly correlated with its claim status. There's no reason to believe that any of the values in the TikTok data are erroneously captured, and they align with expectation of how social media works: a very small proportion of videos get super high engagement levels. That's the nature of viral content.
# 
# Nonetheless, it's good practice to get a sense of just how many of your data points could be considered outliers. The definition of an outlier can change based on the details of your project, and it helps to have domain expertise to decide a threshold. You've learned that a common way to determine outliers in a normal distribution is to calculate the interquartile range (IQR) and set a threshold that is 1.5 * IQR above the 3rd quartile.
# 
# In this TikTok dataset, the values for the count variables are not normally distributed. They are heavily skewed to the right. One way of modifying the outlier threshold is by calculating the **median** value for each variable and then adding 1.5 * IQR. This results in a threshold that is, in this case, much lower than it would be if you used the 3rd quartile.
# 
# Write a for loop that iterates over the column names of each count variable. For each iteration:
# 1. Calculate the IQR of the column
# 2. Calculate the median of the column
# 3. Calculate the outlier threshold (median + 1.5 * IQR)
# 4. Calculate the numer of videos with a count in that column that exceeds the outlier threshold
# 5. Print "Number of outliers, {column name}: {outlier count}"
# 
# ```
# Example:
# Number of outliers, video_view_count: ___
# Number of outliers, video_like_count: ___
# Number of outliers, video_share_count: ___
# Number of outliers, video_download_count: ___
# Number of outliers, video_comment_count: ___
# ```

# In[30]:


### YOUR CODE HERE ###

# List of count columns to iterate over
count_columns = ['video_view_count', 'video_like_count', 'video_share_count', 
                 'video_download_count', 'video_comment_count']

for column in count_columns:
    # 1. Calculate the IQR (Interquartile Range)
    percentile25 = data[column].quantile(0.25)
    percentile75 = data[column].quantile(0.75)
    iqr = percentile75 - percentile25
    
    # 2. Calculate the median
    median = data[column].median()
    
    # 3. Calculate the outlier threshold (median + 1.5 * IQR)
    threshold = median + (1.5 * iqr)
    
    # 4. Calculate the number of videos that exceed the threshold
    outlier_count = (data[column] > threshold).sum()
    
    # 5. Print the results
    print(f"Number of outliers, {column}: {outlier_count}")


# #### **Scatterplot**

# In[27]:


# Create a scatterplot of `video_view_count` versus `video_like_count` according to 'claim_status'
### YOUR CODE HERE ###
# Create a scatterplot of `video_view_count` versus `video_like_count` according to 'claim_status'
plt.figure(figsize=(7, 4))
sns.scatterplot(data=data, 
                x='video_view_count', 
                y='video_like_count', 
                hue='claim_status', 
                size='claim_status', # Opcional: para resaltar la diferencia
                alpha=0.5, 
                s=10)

plt.title('Vistas vs Likes por Estado de Reclamación / Video Views vs Likes by Claim Status')
plt.xlabel('Cantidad de Vistas / Video View Count')
plt.ylabel('Cantidad de Likes / Video Like Count')

plt.show()


# EN:
# Clear Boundary: You will see a distinct separation. Opinions are clustered at the bottom-left corner (low views, low likes). Claims spread across the entire diagonal, showing they are the ones driving high engagement.
# 
# Linear Correlation: The points form a diagonal line, indicating that for every "X" views, there is a predictable "Y" amount of likes. This linear relationship is very strong in this dataset.
# 
# ES:
# Frontera Clara: Verás una separación clara. Las opiniones están agrupadas en la esquina inferior izquierda (pocas vistas, pocos likes). Las reclamaciones se extienden por toda la diagonal, demostrando que son las que impulsan la alta interacción.
# 
# Correlación Lineal: Los puntos forman una línea diagonal, lo que indica que por cada "X" vistas, hay una cantidad predecible "Y" de likes. Esta relación lineal es muy fuerte en este conjunto de datos.

# In[31]:


# Create a scatterplot of ``video_view_count` versus `video_like_count` for opinions only
### YOUR CODE HERE ###
# Filter the data for opinions only
opinion_data = data[data['claim_status'] == 'opinion']

# Create a scatterplot of `video_view_count` versus `video_like_count` for opinions only
plt.figure(figsize=(7, 4))
sns.scatterplot(data=opinion_data, 
                x='video_view_count', 
                y='video_like_count', 
                s=15, 
                alpha=0.5)

plt.title('Vistas vs Likes (Solo Opiniones) / Views vs Likes (Opinions only)')
plt.xlabel('Vistas / Video View Count')
plt.ylabel('Likes / Video Like Count')

plt.show()


# Análisis Comparativo Final / Final Comparative Analysis
# 1. Scale Shift / Cambio de Escala
# 
# EN: When you plotted both together, the x-axis reached into the billions. Now, it likely stops around 10,000. This shows that even the most "popular" opinion is still much smaller than a typical claim.
# 
# ES: Cuando graficaste ambos juntos, el eje X llegaba a los miles de millones. Ahora, probablemente se detiene alrededor de 10,000. Esto muestra que incluso la opinión más "popular" sigue siendo mucho más pequeña que una reclamación típica.
# 
# 2. Uniformity / Uniformidad
# 
# EN: The relationship between views and likes remains linear. This tells us that users interact with opinions in the same way they do with claims—they just aren't exposed to them as often by the algorithm.
# 
# ES: La relación entre vistas y likes sigue siendo lineal. Esto nos dice que los usuarios interactúan con las opiniones de la misma manera que con las reclamaciones; simplemente el algoritmo no los expone a ellas con tanta frecuencia.

# You can do a scatterplot in Tableau Public as well, which can be easier to manipulate and present. If you'd like step by step instructions, you can review the instructions linked in the previous Activity page.

# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## **PACE: Execute**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Execute stage.

# ### **Task 5a. Results and evaluation**
# 
# Having built visualizations in Tableau and in Python, what have you learned about the dataset? What other questions have your visualizations uncovered that you should pursue?
# 
# ***Pro tip:*** Put yourself in your client's perspective, what would they want to know?
# 
# Use the following code cells to pursue any additional EDA. Also use the space to make sure your visualizations are clean, easily understandable, and accessible.
# 
# ***Ask yourself:*** Did you consider color, contrast, emphasis, and labeling?
# 

# ==> ENTER YOUR RESPONSE HERE
# 
# I have learned ....
# ES: Existe una dicotomía clara: las "reclamaciones" (claims) son el motor de la interacción masiva, mientras que las "opiniones" tienen un alcance muy limitado. Además, la falta de verificación del autor está fuertemente ligada al contenido tipo claim.
# 
# EN: There is a clear dichotomy: "claims" drive massive engagement, while "opinions" have very limited reach. Furthermore, lack of author verification is strongly linked to claim-type content.
# 
# My other questions are ....
# 
# ES: ¿Existe una relación entre la duración del video y la probabilidad de que sea una reclamación? ¿Ciertos autores no verificados son "reincidentes" en publicar reclamos que luego son reportados?
# 
# EN: Is there a relationship between video duration and the likelihood of it being a claim? Are certain unverified authors "repeat offenders" in posting claims that later get reported?
# 
# My client would likely want to know ...
# Como analista de datos, tu cliente querría saber: / As a data analyst, your client would want to know:
# 
# Priorización / Prioritization:
# 
# ES: "¿Podemos usar el recuento de vistas como el primer filtro automático para priorizar la moderación humana?"
# 
# EN: "Can we use view count as the primary automated filter to prioritize human moderation?"
# 
# Riesgo / Risk:
# 
# ES: "¿Cuál es la diferencia en la velocidad de viralización entre una 'reclamación' (claim) y una 'opinión'?"
# 
# EN: "What is the difference in the rate of virality between a 'claim' and an 'opinion'?"
# 
# Acción / Action:
# 
# ES: "¿Deberíamos endurecer los requisitos de verificación para aquellas cuentas que superan un umbral específico de vistas?"
# 
# EN: "Should we tighten verification requirements for accounts that exceed a specific view count threshold?"
# 

# ### **Task 5b. Conclusion**
# *Make it professional and presentable*
# 
# You have visualized the data you need to share with the director now. Remember, the goal of a data visualization is for an audience member to glean the information on the chart in mere seconds.
# 
# *Questions to ask yourself for reflection:*
# Why is it important to conduct Exploratory Data Analysis? What other visuals could you create?
# 

# EDA is important because ...
# 
# EN: EDA is important because it allows us to validate the quality of the data before building predictive models. It helps identify distributions, detect significant outliers, and uncover hidden relationships between variables (such as the link between engagement and claims) that will be crucial for the model's accuracy.
# 
# ES: El EDA es importante porque nos permite validar la calidad de los datos antes de construir modelos predictivos. Ayuda a identificar distribuciones, detectar valores atípicos (outliers) significativos y descubrir relaciones ocultas entre variables (como el vínculo entre la interacción y las reclamaciones) que serán cruciales para la precisión del modelo.
# ==> ENTER YOUR RESPONSES HERE
# Visualizations helped me understand ..
# 
# ==> ENTER YOUR RESPONSES HERE
# Engagement Gap: Claims drive disproportionately higher views and likes compared to opinions.
# 
# Verification Bias: Unverified accounts are the primary source of claim-type content.
# 
# Data Skewness: Most interaction metrics are heavily right-skewed, meaning viral content is the exception, not the rule.
# 
# ES: Las visualizaciones me ayudaron a entender que:
# 
# Brecha de Interacción: Las reclamaciones generan vistas y likes desproporcionadamente más altos que las opiniones.
# 
# Sesgo de Verificación: Las cuentas no verificadas son la principal fuente de contenido tipo "reclamación".
# 
# Sesgo de los Datos: La mayoría de las métricas de interacción están fuertemente sesgadas a la derecha, lo que significa que el contenido viral es la excepción, no la regla.
# 
# EN: To further the investigation, I could create:
# 
# Heatmaps: To see the correlation between video duration and report counts.
# 
# Time-Series Analysis: To observe if claims are posted at specific times or frequencies.
# 
# Word Clouds: To analyze common keywords in video descriptions for both categories.
# 
# ES: Para profundizar en la investigación, podría crear:
# 
# Mapas de Calor: Para ver la correlación entre la duración del video y el conteo de reportes.
# 
# Análisis de Series Temporales: Para observar si las reclamaciones se publican en horarios o frecuencias específicas.
# 
# Nubes de Palabras: Para analizar palabras clave comunes en las descripciones de los videos para ambas categorías.
# 
# Reflexión Final para el Director / Final Reflection for the Director
# EN: "The data suggests that the Orion model should prioritize unverified accounts with high engagement velocity, as these features are the strongest indicators of potential claims requiring moderation."
# 
# ES: "Los datos sugieren que el modelo Orion debe priorizar las cuentas no verificadas con alta velocidad de interacción, ya que estas características son los indicadores más fuertes de posibles reclamaciones que requieren moderación."

# You’ve now completed a professional data visualization according to a business need. Well done! Be sure to save your work as a reference for later work in Tableau.

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
