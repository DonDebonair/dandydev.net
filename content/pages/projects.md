Title: Projects

Here you can find information related to the projects I work on.

### Salesforce2hadoop

_Salesforce2hadoop_ allows you to import data from Salesforce and put it in HDFS (or your local filesystem), serialised as 
Avro. Despite its boring name, it's a powerful tool that helps you get all relevant data of your business in _one place_. 
It only needs access to the Salesforce API using a username/password combination, and the Enterprise WSDL of your 
Salesforce Organisation.

Features:

- Choose the type(s) of records you want to import
- Data types are preserved by looking at the Enterprise WSDL of your Salesforce Organisation
- Data is stored in [Avro](https://avro.apache.org/docs/current/) format, providing great compatibility with a number of tools
- Do a complete import of your data, or incrementally import only the records that have been changed since your last import
- Salesforce2hadoop keeps track for you of the last time each record type was imported.
- Stores data into any filesystem that Hadoop/KiteSDK supports. Can be HDFS but also a local filesystem.
- Built with the help of [KiteSDK](http://kitesdk.org/), Salesforce [WSC](https://github.com/forcedotcom/wsc) and our own [wsdl2avro](https://github.com/datadudes/wsdl2avro) library.
- Built for the JVM, so works on any system that has Java 7 or greater installed

Find it [on Github](https://github.com/datadudes/salesforce2hadoop)

### WSDL2Avro

WSDL2Avro is a Scala library that lets you convert datatypes from a SOAP WSDL to Avro Schemas. It takes the XML types as 
defined in the `<types>` section of a WSDL document and converts them into Avro Schema objects that can then be used 
programmatically or saved to disk. This library is particulary useful when you want to consume a SOAP service, and store 
the data somewhere (e.g. in a Hadoop cluster) serialized in Avro format.

This library has been extensively used in production.

Features:

- Provide a path to a WSDL document, or a File object, and get a `Map` with type names and Avro `Schema` objects in return.
- Converts XML primitives to Avro primitives
- Takes care of inheritance (which Avro doesn't support) by keeping track of base types and combining the fields of 
base types with those of inherited types.

Find it [on Github](https://github.com/datadudes/wsdl2avro)

### Athena

<script type="text/javascript" src="https://asciinema.org/a/15439.js" id="asciicast-15439" async></script>

Athena is a convenient command line tool that enables you to interact with and query a Hadoop cluster from your local terminal, 
removing the need for remote SSH sessions. Athena makes the life of every data scientist and engineer a lot easier by 
providing comprehensive querying features and easy automation of daily tasks, from the convenience of your local command line!

**Features**

- Query Impala and show the results in your terminal or save the results to a CSV file
- Run a batch of queries (as defined in a YAML file) on Impala, saving the results to the specified CSV file(s)
- Define a report with one or more queries and mail it to one or more people. Reports are rendered in a neutral and good looking template.
- Schedule reports using the built-in scheduler. Send reports on specific dates or intervals, to any number of people.
- Ship a Pig script and related libraries/UDFs to your Hadoop cluster and run it there.
- Start an SSH session to a node on your cluster, or even create a tunnel without having to remember hostnames/ip addresses.
- Start a distributed copy job by just providing a source and destination. Works with HDFS and S3.
- Works with static hostnames/IPs or dynamic hostnames for clusters on Amazon Web Services.

Find it [on Github](https://github.com/datadudes/athena)

### Pelican-bootstrap3

The theme that this blog was built on. It is a theme for use with the Pelican static blog generator.

Find it [on Github](https://github.com/DandyDev/pelican-bootstrap3)

Blog posts [about this theme](http://dandydev.net/tags/pelican)

### Impala REST API

This is a thin REST API for Cloudera Impala, written in Python. It provides a simple endpoint to send queries to, returning the results either in CSV format or as JSON. It also caches the results for later usage. Currently the whole cache is expired at 9 o'clock in the morning.

Impala REST API is useable, but not 100% mature yet.

Find it [on Github](https://github.com/datadudes/impala-rest-api)

### Gitsentry

Get notified on certain files changing in a Git repository. Documentation pending...

Find it [on Github](https://github.com/DandyDev/gitsentry)

### And more...

... can be found on Github:

[github.com/DandyDev](https://github.com/DandyDev)

[github.com/datadudes](https://github.com/datadudes)