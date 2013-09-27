Title: BigData & Hadoop in a Marketing Context
Date: 2012-09-02 15:41
Tags: bigdata, hadoop, marketing, bachelorthesis
Slug: bigdata-hadoop-in-a-marketing-context
Summary: It's been a while since I wrote on this blog. The main reason for that is that I've been working on my Bachelor thesis since July, and I had to wrap up all other courses before that, so I've been quite busy. I'm halfway through the alotted time for the research now, so I'll be presenting my findings in the beginning of November. Today I want to talk a bit about the research I'm doing and the interesting things I found out already. Note that, although the blogs I write tend to be mostly technical-oriented, this article will put emphasis less on technology and more on the functional aspects of BigData. In later articles I will detail installation processes of Hadoop, and delve into using Hadoop and related systems.

It's been a while since I wrote on this blog. The main reason for that is that I've been working on my Bachelor thesis since July, and I had to wrap up all other courses before that, so I've been quite busy. I'm halfway through the alotted time for the research now, so I'll be presenting my findings in the beginning of November. Today I want to talk a bit about the research I'm doing and the interesting things I found out already. Note that, although the blogs I write tend to be mostly technical-oriented, this article will put emphasis less on technology and more on the functional aspects of BigData. In later articles I will detail installation processes of Hadoop, and delve into using Hadoop and related systems.

### The BigData proposal
The research I'm doing is part of my graduate internship with a company called [2organize](http://www.2organize.com). 2organize's main business proposition lies in the realm of Marketing Automation. To put it simple: they automate the campaign processes for their customers. Depending on the clients, that entails providing the execution of client's campaigns, and sometimes managing their campaigns and related processes. That sometimes included making selections from their (customer)base, to determine who gets contacted during what campaign. 2organize also provides Marketing Intelligence insights for their clients, often related to those campaigns. Mostly everything they do, lies firmly at the intersection between Marketing and IT.

The question they asked me to answer, was in what way they can apply BigData technologies, and Hadoop in particular, to the processing and analysis of data that is done for their clients. I was looking for a research topic specifically in the domain of BigData/Hadoop, because that is a large area of interest for me. This particular internship caught my attention because it's less common to see BigData problems identified and tackled in the realm of marketing, than in area's like scientific research, analysing sensor data or in the technology stack of a large social network like [Facebook](www.facebook.com) and [Twitter](www.twitter.com). I was wondering in what ways marketing processes could benefit from using technologies like Hadoop, Pig and Hive. In the end, my goal was also to deliver a Hadoop-based prototype that would solve one or more of the problems I identified through my research.

Below, I will in short fashion present some of the results of my research so far. More comprehensive results will be presented at a later time, when my research and prototyping is done.

### Identifying BigData problems in Marketing
In order to have an idea what manner of data-related problems were cropping up in the daily processes that were part of 2organize's business proposition, and to what extend they were BigData related and could be solved with Hadoop, I interviewed around 1/4th of the 160 employees. I took a sample from the myriad of functions and levels within the company, to get a clear image of what they're dealing with. 
One of the first interesting patterns that emerged, was the lack of knowledge about BigData in general. While most of the interviewees have heard about BigData in one way or the other, the majority doesn't have a clear idea what BigData actually entails, let alone the technologies that deal with BigData. This isn't all that surprising though, and it's a sign that emphasis within 2organize lies more with marketing than with the technology their using. Oracle, Unica, Tripolis, they're tools to get a job done. This is a reflection of their "Best of Breed" practice.

![bigdata-familiarity.png]({filename}/images/bigdata-familiarity.png)

After explaining what BigData is exactly, many of the interviewees were able to identify general applications of BigData (not related to their work). Two bighitters:

- WebAnalytics/Online Behaviour: they're talking mostly about analysing that kind of data
- Processing large quantities of data: this is the most general application of BigData

![general-bigdata-applications.png]({filename}/images/general-bigdata-applications.png)

Not knowing about BigData, doesn't mean data-problems relating BigData aren't encountered with their clients though. Gartner's [_definition_ of BigData](http://blogs.gartner.com/doug-laney/deja-vvvue-others-claiming-gartners-volume-velocity-variety-construct-for-big-data/) talks about the 3V's:

- Volume
- Velocity
- Variety

Within common marketing (automation) processes as they currently happen, _volume_ doesn't seem to play a big role. Considering CRM data and sometimes transactional data, are the only kinds of data that are used, we're talking about millions of records at most, with the largest clients. _Velocity_ isn't a problem either so far. Even if they add thousands of customers each day, the data still is managable. If you grant companies their wish and start adding social media data though, velocity of data starts becoming a problem though. _Variety_ is already becoming a problem. Companies start adding WebAnalytics data to the mix more often, which is almost unstructured, and doesn't fit the relational model the CRM data is currently stored in. In other words, it's hard to actually couple that data to your existing CRM data.
When asked for potential usecases of BigData technologies in their work, the interviewees came up with these answers:

[![hadoop-bigdata-applications.png]({filename}/images/hadoop-bigdata-applications-small.png)]({filename}/images/hadoop-bigdata-applications.png)

_Click to enlarge_

As you can see, the coupling of data to get better insights is a frequently encountered problem. Which brings me to the penultimate BigData usecase in marketing:

### Creating a more complete customerprofile
It appears most of the answers in the interview detailing possible usecases of BigData technologies, are a variation of the datacoupling problem. Now, how is this becoming a problem? There are a few reasons for that:

- A lot of clients of 2organize, are composed of several autonomous business units with each a seperate customerdatabase. There's a lot of incentive to be able to couple those different databases. Not only as a convenience to the customer (do you want to have 3 different customer id's within the same company?), but also to be able to have a better customerprofile composed of all that data and to be able to cross-sell different products. This also makes _Volume_ a problem at some point.
- WebAnalytics and Social Media add new streams of data that can also be used to enhance customerprofiles. At the typical speed of those dataflows, _Velocity_ can become a problem. And if we look at the structure of those datastreams compared to existing CRM and transactional data, we're talking about a different _Variaty_ of data.

In short, even if companies can't necessarily pinpoint the real problem, marketeers are noticing a growing trend towards creating complete and comprehensive customerprofiles. This is something that IBM also noted in their [CMO study 2011](http://www-935.ibm.com/services/us/cmo/cmostudy2011/cmo-registration.html). BigData is identified as one of the largest challenges in years to come. Why? Because large quantities of data are needed to create more comprehensive customerprofiles. In order to get to that, you need to couple lots of datastreams in a sometimes ad-hoc manner. Datastreams that don't always fit the relational model. These are tasks that Hadoop and company are ideally suited for. What I'm advocating here, is using Hadoop to create a new kind of datawarehouse where all those different datastreams come together. Analysts can query that data in situ, while technologies like Hive can be used to create "views" of aggregated data that can eventually be exported to campaign management and execution systems that expect common Oracle databases to do their job.

### Prototyping
Of course, it's impossible to build such a warehouse in the scope of my Bachelor thesis research. Nor is it feasible to start building those complete customerprofiles in this timeframe. Therefor I identified a smaller sub-problem one of 2organize's clients was dealing with, that defied conventional technologies, and requires the use of BigData solutions to be solved. I will talk about that problem in the future and about the technical implementation I'm going to use to solve it. I will also try to do some writeups about practicle Hadoop-use, as promised in the beginning of this article.