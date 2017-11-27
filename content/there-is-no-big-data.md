Title: There Is No Big Data
Date: 2017-11-26 12:00
Slug: there-is-no-big-data

I've been working as a data engineer for various companies for a while now, and one thing I keep noticing is how quickly people get caught up in, and are _mislead by_ the "Big Data Hype". There even seems to be an inverse correlation between the technical skill level of a person, and the likelyhood they'll blindly _preach_ "Big Data" in their company. If Gartner is to be believed, "Big Data" will magically transform your organisation and elevate the bottom line to unprecedented heights. But only if you can stick [three](http://www.zdnet.com/article/volume-velocity-and-variety-understanding-the-three-vs-of-big-data/) [or more](https://www.linkedin.com/pulse/20140306073407-64875646-big-data-the-5-vs-everyone-must-know/) _silly_ [Vs](https://www.impactradius.com/blog/7-vs-big-data/) to your data...

Well... notice the quotes around "Big Data"? That's because **There Is No Big Data**.

### Just Data

Maybe the biggest problem with the term "Big Data", is that everybody means something different by it, and that makes proper discussion on the topic impossible. There are too many companies that see "Big Data" as a goal in and of itself. It never should be.

If there's no "Big Data", then what _can_ we talk about? We can talk about _data_, just. plain. data. Data that has been there for ages. The only difference between _then_ and _now_ is that the amount of data available to the average company is growing, and the ways we know to leverage it, are expanding. But, when looking at the volume of data, there is no magical barrier you can pass, after which you can proudly call yourself a member of the "Big Data Club". In fact, even if there were such a barrier, it'd be a blurry, moving target.

I'd say that for a lot of companies - if not most - it'd be great if they were looking at their data _at all_, let alone pulling open boxes of super specialized tools to use their data in the most advanced ways possible. My advice? Start with consolidating your data, cleaning it and making sure that your data is actually looked at and taken into account when making business decisions. That alone might put you ahead of the competition 👊

So go ahead, hire some data analysts/business intelligence experts/data scientists and start putting that data to good use. You can use "conventional" technologies, like data warehousing and BI tools, and get very, very far.

### Tools to Solve Problems

I'm gonna let you in on a secret: even engineers like myself, [sometimes]({filename}/installing-virtual-hadoop-cluster.md) [use the]({filename}/bigdata-hadoop-in-a-marketing-context.md) B-word. I've been trying to wean myself off of it and educate the people I work with, and this blog post is part of that effort. 

So what do engineers like myself mean, when we're talking about "Big Data"? Well, most of the time I use the B-word, it's when I'm talking about "Big Data _technologies_". And what I _actually mean_ by that, is a set of technologies built on the theory of [_distributed computing_](https://en.wikipedia.org/wiki/Distributed_computing) and aimed at solving a **very specific set of problems** (usually not _your_ problems). At the core of these technologies is [Hadoop](https://en.wikipedia.org/wiki/Apache_Hadoop), but there is in fact a whole ecosystem of distributed applications/systems/tools to help with a very narrow set of problems related to data processing and analysis **at scale**. Examples are: [Kafka](https://kafka.apache.org/), [Spark](https://spark.apache.org/) and [Hive](https://hive.apache.org/), but there are many more.

The point is: you [rarely need these technologies](https://www.chrisstucchio.com/blog/2013/hadoop_hatred.html) to reach your goal of becoming a data-driven organisation and utterly slaying the competition. What you need - most of the time - is people who understand your data, and a company-wide shift in mindset to start trusting this data and ignore gut feelings.

When do you _actually need_ Hadoop et al.? 

- When your datasets are so large that you can't store them in a traditional RDBMS
- When you want to store data in many different forms together in one place and leverage Schema-on-Read, so you don't have to define your data models beforehand. This is what's sometimes referred to as a "Data Lake" (oh my, another set of buzz words). Be mindful that most of your data _does have a schema_, even if you don't define it as such beforehand.
- When the real-timeness of data processing and analysis becomes really important. Spark offers some [excellent tools](http://asyncified.io/2017/07/30/exploring-stateful-streaming-with-spark-structured-streaming/) to help you with keeping state in a streaming system, that you'd have to build yourself otherwise. And if you have to deal with many different real-time data streams at the same time, Spark + Kafka is a killer combination
- When you aren't able to use the excellent SaaS solutions like [Google BigQuery](https://cloud.google.com/bigquery/)

Let me emphasize that last point: please use SaaS solutions when you really need data storage and processing at scale, because Hadoop et al. are notoriously difficult to deploy, manage and maintain.

Until you reach that point where your regular tools stop working, [trust](https://products.office.com/en/excel) [proven](https://www.postgresql.org/) [tools](https://pydata.org/downloads.html).

### Bonus

Now that we got that whole "Big Data" fad out of the way, let me quickly lure you away from a couple of other misunderstood hypes before parting ways:

- Your company doesn't need **Blockchain** technology, unless you're building a cryptocurrency, [which you shouldn't]({filename}/images/blockchain.jpg)
- **Machine Learning** isn't a silver bullet. [Machine Learning is hard](http://ai.stanford.edu/~zayd/why-is-machine-learning-hard.html). It will not magically give you super accurate predictions to solve whatever business problem you have. In fact, it's amazing if your data scientists can come up with a model that outperforms a coin flip. That is not to say that you shouldn't invest in building machine learning models, but you should be realistic in your expectations.

Any other unicorns that need to be put down? Let me know!