#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 00:59:14 2020

@author: umut
"""



from plotly.offline import plot
from wordcloud import WordCloud
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#%% load data and information abot timesData
timesData = pd.read_csv("timesData.csv")
timesData.info()
timesData.head(10)
#%% line plot using, line plot as LINE CHART
# Citation and Teaching vs World Rank of Top 100 Universites

# prepare data frame

#create trace1 trace :green line, turkish mean: iz.

"""
Most popular traces attributes
Traces: x = x axis
        y = y axis
        mode = type of plot like marker:
            1) line
            2) line + markers
        name = name of the plots
        marker = marker is used with dictionary
            color = color of lines with RGB and opacity (alpha, ex: 0.7, 0.6)
        text = the hover text
        data = is a list that we add traces into it
        layout = it is dictionary
            title = title of layout
            x axis = it is dictionary
                title = label of x axis
                ticklen = length of x axis ticks
                zeroline = showing zero line or not
            

"""

df = timesData.iloc[:100,:]
trace1 = go.Scatter(
    x = df.world_rank,
    y = df.citations,
    mode = "lines",
    name = "citations",
    marker = dict(color='rgba(16,112,2,0.8)'),
    text = df.university_name)


#creating trace2 : purple line

trace2 = go.Scatter(
    x = df.world_rank,
    y = df.teaching,
    mode = "lines+markers",
    name = "teaching",
    marker = dict(color='rgba(80,26,80,0.8)'),
    text = df.university_name)

data = [trace1, trace2] #concatination on the list 
layout = dict(title= 'Citation and Teaching vs World Rank of Top 100 Universities',
              xaxis=dict(title='World Rank', ticklen=5, zeroline=False)
              )

figure = dict(data=data, layout=layout)
plot(figure)

#%% scatter plot Citation vs World Rank of Top 100 universites with 2014, 2015 and 2016 years
import plotly.graph_objs as go
# prepare dta frames
df2014 = timesData[timesData.year == 2014].iloc[:100,:] #print top 100 universites
df2015 = timesData[timesData.year == 2015].iloc[:100,:]
df2016 = timesData[timesData.year == 2016].iloc[:100,:]

# import graph objects as "go"

#creating trace1

trace1 = go.Scatter(
    x = df2014.world_rank,
    y = df2014.citations,
    mode = "markers",
    name = "2014",
    marker = dict(color='rgba(255,128,255,0.8)'),
    text = df2014.university_name
    )

# creating trace2

trace2 = go.Scatter(
    x = df2015.world_rank,
    y = df2015.citations,
    mode = "markers",
    name = "2015",
    marker = dict(color='rgba(255,128,2,0.8)'),
    text = df2015.university_name
    )

# creating trace3

trace3 = go.Scatter(
    x = df2016.world_rank,
    y = df2016.citations,
    mode = "markers",
    name = "2016",
    marker = dict(color='rgba(0,255,200,0.8)'),
    text = df2016.university_name
    )

data = [trace1, trace2, trace3]
layout = dict(title='Citation vs World Rank of top 100 universitites with 2014, 2015 and 2016 years',
              xaxis = dict(title = 'World Rank', ticklen=5, zeroline=False),
              yaxis = dict(title= 'Citation', ticklen=5, zeroline=False)
              )

figure = dict(data=data, layout=layout)
plot(figure)


#%% Bar Charts, Citations and Teaching of Top 3 Universities in 2014

df2014 = timesData[timesData.year==2014].iloc[:3,:]


trace1 = go.Bar(
    x = df2014.university_name,
    y = df2014.citations,
    name = "citations",
    marker = dict(color = 'rgba(255,174,255,0.5)',
                  line = dict(color = 'rgb(0,0,0)',width=1.5)),
    text = df2014.country
    )

# create trace2

trace2 = go.Bar(
    x = df2014.university_name,
    y = df2014.teaching,
    name = "teaching",
    marker = dict(color = 'rgba(255,255,128,0.5)',
                  line = dict(color='rgb(0,0,0)',width=1.5)),
    text = df2014.country
    )

data = [trace1, trace2]
layout = go.Layout(barmode = "group")
fig = go.Figure(data=data, layout=layout)
plot(fig)


#%% second bar chart example

df2014 = timesData[timesData.year==2014].iloc[:3,:]

x = df2014.university_name

trace1 = {
    'x':x,
    'y':df2014.citations,
    'name':'citation',
    'type':'bar'
    };

trace2 = {
    'x':x,
    'y':df2014.teaching,
    'name':'teaching',
    'type':'bar'
    };

data = [trace1, trace2];
layout = {
    'xaxis':{'title':'Top 3 universities'},
    'barmode':'relative',
    'title':'citations and teaching of top 3 universities in 2014'
    };

fig = go.Figure(data=data, layout=layout)
plot(fig)

#%% Pie Plot - Student rate of top 7 universities in 2016

"""
fig: create figure
data:plt type
    values: value of plot
    labels: label of plot
    name: name of plot
    hoverinfo: information in hover
    hole: hole width
    type: plt type like pie
    
layout: layout of plot
    title: title of layout
    annotations: font, showarrow, text, x, y
"""

#number of students, object value. Object to float

df2016 = timesData[timesData.year==2016].iloc[:7,:]
pie1 = df2016.num_students
pie1_list = [float(each.replace(',', '.')) for each in df2016.num_students]  # 2,4 => 2.4, after str to float
labels = df2016.university_name

# figure

fig = {
       "data":[
           {
           "values": pie1_list,
           "labels": labels,
           "domain": {"x":[0, .5]},
           "name": "Number of Students Rates",
           "hoverinfo":"label+percent+name",
           "hole": .3,
           "type": "pie"
            }, ],
       
       "layout":{
           "title": "Universities Number of Students Rates",
           "annotations": [
               {"font":  {"size":20},
                "showarrow": False,
                "text": "Number of Students",
                "x": 0.20,
                "y":1
                },
               ]
           }
       }

plot(fig)

#%% Bubble Plot - University World Rank (first 20) vs Teaching Score with Number of Student (size) and international score(color) in 2016

"""
x = x axis
y = y axis
mode = markers(scatter)
marker = marker properties
    color = third dimension of plot. International score
    size = fourth dimension of plot. Number of students
text = university name
"""


 # data preparation 

df2016 = timesData[timesData.year == 2016].iloc[:20,:]
num_students_size = [float(each.replace(',','.')) for each in df2016.num_students] #str to float
international_color = [float(each) for each in df2016.international]

data = [
        {
            'y': df2016.teaching,
            'x': df2016.world_rank,
            'mode': 'markers',
            'marker':{
                'color': international_color,
                'size': num_students_size,
                'showscale': True
                },
            "text": df2016.university_name
            }
        ]
plot(data)

#%% Histogram Students-staff ratio in 2011 and 2012 years

"""

trace1 = first histogram
    x = x axis
    y = y axis
    opacity = opacity of histogram
    name = name of legend
    marker = color of histogram
trace2 = second histogram
layout = layout
    barmode = mode of histohram like overlay. Also you can change with stack

"""


x2011 = timesData.student_staff_ratio[timesData.year == 2011]
x2012 = timesData.student_staff_ratio[timesData.year == 2012]

trace1 = go.Histogram(
    x=x2011,
    opacity=0.75,
    name = "2011",
    marker=dict(color='rgba(171,50,96,0.6)'))

trace2 = go.Histogram(
    x = x2012,
    opacity=0.75,
    name="2012",
    marker=dict(color='rgba(12,50,196,0.6)'))

data = [trace1, trace2]
layout = go.Layout(barmode="overlay",
                   title="Students Staff Ratio in 2011 and 2012",
                   xaxis = dict(title='students-staff ratio'),
                   yaxis = dict(title='Count'))


fig = go.Figure(data=data, layout=layout)
plot(fig)

#%% world cloud, which country is mentioned most in 2011
from wordcloud import WordCloud

"""
    World Cloud is not a pyplot
    
    background_color = Color of Background
    generate = generates the country name list a world cloud
"""

#data prepration

x2011 = timesData.country[timesData.year == 2011]
plt.subplots(figsize=(8,8))
worldcloud = WordCloud(
    background_color="white",
    width=512,
    height=384).generate(" ".join(x2011)) #kelimeleri ayır ve en çok yazılanları büyükçe plot ettirmemizi sağlar

plt.imshow(worldcloud)
plt.axis("off")
plt.savefig("graph.png")

#%% Box Plot
#find quantile, upper fece, meadian, mid and max values
"""
trace = box
    y = data we want to visualize with box plot
    marker = color

"""

x2015 = timesData[timesData.year==2015]

trace0 = go.Box(
    y=x2015.total_score,
    name = 'total score of universites in 2015',
    marker = dict(color='rgb(12,12,140)'),
    )   
  

trace1 = go.Box(
    y = x2015.research,
    name = 'research of universities in 2015',
    marker = dict(color = 'rgb(12,128,128)'),
    )


data = [trace0, trace1]
plot(data)


#%% Scatter Matris Plot, see covaria nce and relation between more than 2 features
"""
import figure factory as ff
create_scatterplotmatrix = create scatter plot
    data2015 = prepared data.
    colormap= color map of scatter plot
    colormap_type = color type of scatter plot
    height and weight
"""
                                                            
import plotly.figure_factory as ff


dataframe = timesData[timesData.year == 2015]
data2015 = dataframe.loc[:,["research", "international", "total_score"]]
data2015["index"] = np.arange(1, len(data2015)+1)

#scatter matrix

fig = ff.create_scatterplotmatrix(data2015, diag='box', index='index', colormap='Portland', colormap_type='cat', height=700, width=700)
plot(fig)

#%% Inset Plot - 2 plots are in one frame

trace1 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.teaching,
    name="teaching",
    marker = dict(color='rgba(12,112,2,0.8)'),
    )


trace2 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.income,
    xaxis='x2',
    yaxis='y2',
    name="income",
    marker = dict(color='rgba(160,112,20,0.8)'),
    )

data = [trace1, trace2]
layout = go.Layout(
    xaxis2=dict(
        domain=[0.6, 0.85],
        anchor='y2',
        ),
    yaxis2=dict(
        domain =  [0.6,0.95],
        anchor='x2',
        ),
    
    title = "Income and Teaching vs World Rank of Universities"
    
    )

fig = go.Figure(data=data, layout=layout)
plot(fig)


#%% 3D Scatter Plot

"""
go.Scatter3d: create 3d scatter
x,y,z: axis of plots
mode: marker that is scatter
size: marker size
color:axis of colorscale
colorscale: actually it is 4th dimension
"""

trace1 = go.Scatter3d(
    x=dataframe.world_rank,
    y=dataframe.research,
    z=dataframe.citations,
    mode='markers',
    marker=dict(
        size=10,
        color='rgb(255,0,0)',                #
        )
    )

data = [trace1]
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0))
fig = go.FigureWidget(data=data, layout=layout)
plot(fig)

#%% Multiple Subplots

trace1 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.research,
    name = "research"
)
trace2 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.citations,
    xaxis='x2',
    yaxis='y2',
    name = "citations"
)
trace3 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.income,
    xaxis='x3',
    yaxis='y3',
    name = "income"
)
trace4 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.total_score,
    xaxis='x4',
    yaxis='y4',
    name = "total_score"
)
data = [trace1, trace2, trace3, trace4]
layout = go.Layout(
    xaxis=dict(
        domain=[0, 0.45]
    ),
    yaxis=dict(
        domain=[0, 0.45]
    ),
    xaxis2=dict(
        domain=[0.55, 1]
    ),
    xaxis3=dict(
        domain=[0, 0.45],
        anchor='y3'
    ),
    xaxis4=dict(
        domain=[0.55, 1],
        anchor='y4'
    ),
    yaxis2=dict(
        domain=[0, 0.45],
        anchor='x2'
    ),
    yaxis3=dict(
        domain=[0.55, 1]
    ),
    yaxis4=dict(
        domain=[0.55, 1],
        anchor='x4'
    ),
    title = 'Research, citation, income and total score VS World Rank of Universities'
)
fig = go.Figure(data=data, layout=layout)
plot(fig)

























"""
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np

x=np.random.randn(2000)
y=np.random.randn(2000)

plot([go.Histogram2dcontour(x=x, y=y, contours=dict(coloring="heatmap")),
      go.Scatter(x=x,y=y,mode="markers",marker=dict(color="black",size=5,opacity=0.7))])
"""
