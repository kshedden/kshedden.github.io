The 2016 U-M Undergraduate Data Mining Competition
--------------------------------------------------

In the competition this year you will analyze a dataset consisting of
internet routing "prefix announcements".  You can aim to identify
faults or possible malicious behavior present in the prefix
announcements.  Or, you can devise another goal, such as
characterizing the prefix announcements graphically or via a
statistical model.

To obtain access to the data, send an email to <kshedden@umich.edu>.
Although the data have been anonymized, routing table data and other
internet traffic data are in general somewhat sensitive.  Therefore,
you must not distribute these data files or use them for any purpose
other than this competition.

The data were provided for our use by researchers at
[MERIT](https://www.merit.edu/), a major network operator and research
organization based in Ann Arbor.

## Background

**Note:** *We may provide more background information, sample code, or
hints here as the competition progresses.*

You will need a very basic understanding of how internet routing works
to understand the data.  The main concept to understand is that the
internet is divided into *subnetworks*, and traffic among the networks
is handled by *routers*.  The major internet routers (each of which
handles huge volumes of traffic directed to many thousands of users),
communicate with each other to facilitate the routing of packets of
data over the network.  When a router is able to handle data that is
headed to a given subnetwork, it sends out a "prefix announcement" to
inform the other routers.  This is a dynamic process, at any point in
time a router can announce that it will accept traffic bound for any
given subnetwork.

The data for the competition is two text files containing a two-hour
snapshot of "routing tables".  These tables capture a subset of the
prefix announcements sent by the the main internet routers.  It only
contains prefix announcements received by the MERIT network router,
which is the router handling traffic to U-M.  Each row in the data
files consists of seven fields separated by pipes.  We are only
interested in the data in fields 6 and 7.  Field 6 identifies a
specific subnetwork.  Field 7 is a sequence of router identifiers.
For example, if field 7 contains the numbers

  11164 4637 17444 55649

this means that router 55649 is announcing that it can now handle
traffic directed to the subnet given in field 6 of the same row
(e.g. subnet 1.0.128.0/19).  After this prefix announcement is made by
router 55649, it is then picked up by routers 17444, 4637, 11164, and
237 in sequence.  Router 237 is the MERIT router and is not listed in
field 7 of the data file, although it is always at the end of the
chain of messages.

You are welcome to analyze this data in any way you see fit.  However
the main motivation for choosing this particular segment of data is
that a routing error occurred at one point within this window of time.
One router incorrectly sent a prefix announcement indicating that it
could receive traffic from a network that it is not supposed to
handle.  You can try to detect this anomalous event, or identify a
subset of the data that is likely to hold the anomalous event.  We may
give more hints later, but for now this is all we are revealing about
the anomaly.

You may also focus your project on other goals, such as describing the
characteristics of prefix calls and the paths that they follow through
the main internet routers.

## Contest rules

* All reports must be submitted by email to Gina Cornacchia
  (ginalc@umich.edu) by 9AM on Monday, April 11th.

* The most important judging criterion is to identify an interesting
  finding in the data, and to support and interpret it in an engaging
  and accessible way.  You do not have to find the anomaly to have a
  valid entry.

* Each participant or team must submit one written report in PDF
  format.

* There is no mandated page length, content or structure for the
  report.  A strong report will be focused, coherent, and interesting
  to read, and should be readable by someone who is not an expert data
  scientist or statistician.

* Use of advanced or specialized techniques will not necessarily be
  viewed as a strength.  If you choose to use advanced techniques be
  sure to motivate and explain each technique in an accessible manner.

* Use of visualization (e.g. graphs and diagrams) is encouraged.
  Visual materials should be incorporated into the report if possible.
  A separate file containing visual materials will also be accepted.

* Questions about the contest should be directed to Gina Cornacchia or
  Kerby Shedden.


## Prizes and judging

The reports will be judged by a panel of experts.  Prizes will be
awarded as follows:

* First place $500

* Second place $300

* Third place $200

When a team is awarded a prize, the prize amount will be divided
equally among the team members.

You can view the page for [last year's competition](data_mining_2015.html).