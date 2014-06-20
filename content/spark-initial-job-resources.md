Title: Spark: Initial job has not accepted any resources
Date: 2014-06-20 11:00
Tags: spark, hadoop, cloudera, resources, memory, heap size
Slug: spark-initial-job-resources

When playing around with Spark on my [local, virtual cluster]({filename}/installing-virtual-hadoop-cluster.md), I ran into some problems concerning resources, even though I had 3 _workers_ running on 3 nodes. I got the following message repeatedly while working with data in the `spark-shell`: 

> Initial job has not accepted any resources; check your cluster UI to ensure that workers are registered and have sufficient memory

After googling around a bit, I discovered this was due to low memory (Java Heap Size) settings. If you're using Cloudera Manager, like I do, you can change the memory usage as follows:

* On the homepage of Cloudera Manager, where it shows your cluster ('Cluster 1' in my case), click on the **Spark** service.
* Now you see an overview of the Spark service, with a status summary of the _Master_ and the _Workers_. Click on “Configuration > View and Edit”.
* In the **Category** section, first choose _Master Default Group_, and edit the _Java Heap Size of Master in Bytes_ to give it a larger amount of memory. In my case it was 64 MiB (which is probably way too less), so I just clicked _default value_, which set the Heap Size to 512 MiB.
* In the **Category** section, now choose _Worker Default Group_, and edit the _Java Heap Size of Worker in Bytes_ to give it a larger amount of memory. In my case it was 64 MiB (which again, is too less), I set it to the _default value_ again.
* Now also edit the _Total Java Heap Sizes of Worker's Executors in Bytes_ to give the Executors more memory. I set it to 1 GiB, which is half the memory my nodes have. I have a feeling that this is actually the most important setting for dealing with the aforementioned error.
* Now you have to restart the Spark service:
	* On the homepage of CM, it should show a restart icon next to the service name. Click it.
	* You can review the changes, and then click _Restart_
	* Select **Re-deploy client configuration** and click _Restart Now_, and the service should now restart.

I can't actually tell you how much memory you should give the Master, Workers and Executors, because that depends on a lot of factors: how large are your nodes? What else is running on your nodes? And most importantly: how large are the datasets you're trying to process?
Maybe if someone of **Cloudera** reads this, they could chime in with better information on how to tune Spark's memory.
