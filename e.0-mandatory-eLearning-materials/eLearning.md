# MISP: Introduction, Concepts and Guide

## Structure of this document 

1. **MISP Introduction**: The what, why and how about MISP
2. **MISP Basics**: A concise introduction to MISP data model
3. **How-to**: A user guide with screenshots on how to use MISP to encode and share data

## MISP Introduction

### What is MISP

### Why is MISP relevant

### What functionalities does MISP offer to fulfil your objectives


## MISP Basics

A cheat-sheet describing the core concepts and data-models in MISP is available [here](https://www.misp-project.org/misp-training/cheatsheet.pdf).

### 1.1 Data Layer

First and foremost, it’s important to understand how MISP is organised. Similar to all applications, some predefined data structure exists and are used to represent and save the actual data on the disk. Such structure in MISP could be for example *Attributes* or *MISP Objects*.

#### MISP Attributes
*Attributes* are individual block containing the very information to be used or to be shared. Thanks to their characteristic called `type`, *Attributes* can represent concept such as an IP address, a domain name or cryptographic hash. In addition to having a `type` and a `value`, they can express if they are Indicators of Compromise (IoC) or supporting data where for example, the former could be a hash of a malicious binary and the later could be Observed behaviour or links toward documentation. The differentiation between IoC and observable can be done by flipping the *Attribute*'s `to_ids` flag.

> include attributes picture


#### MISP Objects
In most of the case, these individual blocks of information can be combined together into a more elaborated concept. When multiple *Attributes* are grouped, they form another entity that is called a *MISP Object*. For example, a *File Object* contains multiple *Attributes* such as the filename, its size, its name and so on.

By their very nature, *MISP Objects* organise and facilitate the reading of data in the application. But their efficiency can be improved even more when you add the capability to link them together with relationships to create directed graph allowing to represent stories, processes or behaviours. In MISP, creating such connections is called "create an *Object Reference*". Viewing these relationships as a connected graph can be done by looking at the widget called *Event Graph*.

> include object picture

#### MISP Events

Now that we have the structures to encode information, we need another structure to be able to group them together in order to avoid dealing with a soup of *Attributes* and *MISP Objects*. *MISP Events* or commonly called *Events* are envelopes allowing to assemble *Attributes* and *Objects* contextually linked. Typically, *Events* are used to encode incidents, events or reports.

> include event picture



#### Threat Intelligence Tools: Event Graph, Event Timeline and Event Reports

##### MISP Event Graph

> include content for event graph

##### MISP Event Timeline

> include content for event timeline

##### MISP Event Reports

In addition to encode data into pre-formatted structure, MISP offers a tool to write report. Such report are called *Events reports* and are contained in an *Event* where they use the markdown syntax to write formatted text. They also provide directives specific to MISP allowing writers to reference other entities contained in the *Event*. This extended syntax supports referencing *Attributes*, *Objects*, *Tags* and *Galaxy Clusters*. 


### 1.2 Context Layer

One of the most critical aspects often left aside is contextualisation. If done properly, it allows the reader to know more about where this data comes from, what it is about, how relevant it is for the user and finally, what can be done with it.

In MISP, contextualising data is as simple as attaching a label to the relevant entity. However, choosing the right labels is the difficult part. We can distinguish two types of labels: *Tags* and *Galaxy Clusters*.


#### Tags

*Tags* are simple labels coming from a curated list of vocabulary (Also called [*Taxonomy*](https://github.com/MISP/misp-taxonomies)). They are mainly used to classify data in order to ease data consumption and automation. For example, the following *Tags* can be used to quickly classify information:
- [`tlp`](https://github.com/MISP/misp-taxonomies/blob/main/tlp/machinetag.json): Allow a favorable classification scheme for sharing sensitive information while keeping the control over its distribution at the same time.
- [`adversary`](https://github.com/MISP/misp-taxonomies/blob/main/adversary/machinetag.json): An overview and description of the adversary infrastructure and allowed actions
- [`collaborative-intelligence`](https://github.com/MISP/misp-taxonomies/blob/main/collaborative-intelligence/machinetag.json): Common language to support analysts to perform their analysis. The objective of this language is to advance collaborative analysis and to share earlier than later.
- [`estimative-language`](https://github.com/MISP/misp-taxonomies/blob/main/estimative-language/machinetag.json): Estimative language to describe quality and credibility of underlying sources, data, and methodologies

> include tag pictures
> include more info about tag/taxonomy


#### Galaxy Clusters

*Galaxy Clusters* are knowledge base items having descriptions, links, synonyms and any other meta-information. *Clusters* are regrouped into a higher-level structure called *Galaxy*. *Clusters* enable analysts to assign complex high-level contextual information to data-structures. Example of *Galaxy Clusters*:

- `country="Luxembourg"` having information such as country-code, languages, TLD, Capital and so on.
- `threat-actor="Sofacy"` having information such as suspected-state-sponsor, victims, links-to-documentation, target-category and synonyms.

> include cluster picture
> include more info about clusters/galaxy



### 1.3 Anatomy of a complete Event

> include anatomy picture


### 1.4 Distribution Levels

> explain all available distribution levels in MISP


### 1.5 Synchronisation

> explain the synchronisation + publishing in MISP


### 1.6 Correlation

> explain the correlation in MISP


## How-to

### Create an Event
### Create an Attribute
### Create an Object
### Create an Relationship
### Create an Event Report
### Add Tags
### Add Galaxy Clusters
### Publish