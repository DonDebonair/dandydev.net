Title: Projects

Here you can find any information and/or downloads related to the projects I work on, that is not available through 
[my Github account](https://github.com/DandyDev). Probably, mostly binary downloads.

### Salesforce2hadoop

Salesforce2hadoop allows you to import data from Salesforce and put it in HDFS, serialised as Avro. Despite its
boring name, it's a powerful tool that helps you get all relevant data of your business in _one place_. It only needs
access to the Salesforce API using a username/password combination, and the Enterprise WSDL of your Salesforce
Organisation.

Features:

- Choose the type(s) of records you want to import
- Data types are preserved by looking at the Enterprise WSDL of your Salesforce Organisation
- Do a complete import of your data, or incrementally import only the records that have been changed since your last import
- Salesforce2hadoop keeps track of the last time each record type was imported.
- Stores data into any filesystem Hadoop supports. Can be HDFS but also a local filesystem.
- Built for the JVM, so works on any system that has Java 7 or greater installed

#### Binaries

Latest: [sf2hadoop.jar]({filename}/files/sf2hadoop.jar)
