# PeRfEx

" A simple way to implement your **PERF**ect reg**EX** "

## About this tool

As you know, regexes can consume a lot amount of resources, using them requires to be very careful.

This tool will help you to implement the more accurate ReGex you'll need to extract a certain pattern.

## Packets Needed

apt-get install python3

apt-get install python3-tk

## HowTo

1. This tool only calculates the performances of your regex, so you'll first need to check if the pattern extracted is the one you wanted. (before using this tool you should first go to this website http://regexr.com/)

2. Then you'll need to execute this python script, give one log example and the regex to test

3. Press "Go" and that's it, the script will execute your ReGex 1 million times and display the time elapsed until it has executed all of them

4. Possible outputs are:
  
  " date -- ReGex Matched | Time elapsed: result (ms)"
  
  or
  
  " date -- ReGex Not Matched | Time elapsed: result (ms)"

*One warning though you need to be careful when giving greedy regexes because running the script can slow down your computer. You might wanna decrease the 1 million times loop, if your computer isn't powerful enough :D*

## Simple Example

**Log =** 50.0.134.125 - - [26/Aug/2014 00:27:41] \"GET / HTTP/1.1\" 200 14 0.0005

**Regex1 =** .* (.*)\[(.*)\]:.*

**Regex2 =** [12]\d{3}-[01]\d-[0-3]\d (.*)\[(.*)\]:.*

Experiment: Let's see how these regexes perform with a non-matching log, we will run two times each regex, in the following order: regex1, regex2, regex2, regex1

### The Results

As you can see on the following screenshot, the Regex2 performs a lot better than Regex1 (more than 100 times better). Of course the example was really simple and just a proof of concept but still the more accurate your regexes are the faster they are executed.

![alt tag](https://github.com/zemelusa/PeRfEx/blob/master/screenshotappli.png)

## Best practises to improve your regexes

https://www.loggly.com/blog/five-invaluable-techniques-to-improve-regex-performance/

https://www.loggly.com/blog/regexes-the-bad-better-best/
