# 0x0A. Configuration management

## Configuration management

This is the systematic handling changes to a system that integerity is maintained over time.

* Automation - this is important in server configuration management. It makes the server reach a desired state made possible by predefined designed instructions in a script through a specific language and its features. Heart of servers configuration management. CMtools are commonly referred to as **IT automation tools/automation tools**. Another automation feature of CM tool is Server Orchestration or IT Orchestration

* Examples of configuration management tools are Puppet, Ansi, Salt - their purpose is to ensure that system's state matches provided script state

## Advantages of Configuration Management for Servers

* Quick Provisioning of New Servers

* Quick Recovering from Critical Events

* No More Snowflakes Servers

* Version Control for the Server Environment

* Replicated Environment

## Overview of Configuration Management Tools

Although CM tools have different approaches, their are similarities. **Most CM tools use a controller/master and node/agent model**. The controller directs the configuration of the node, based on series of of instruction/tasks in provisioning scripts. Below are common features of CM tools.

* Automation Framework - each CM tool provides specific syntax and features for writing provisioning scripts

* Idempotent Behavior -keeping track of resources in order to avoid repetetion of tasks already executed before

* System facts - data available through global variable **facts**

* Templating systems - use of templating systems in setting up configuration files and settings

* Extensibility reusability either as modules or plugins

## Choosing a Configuration Management Tool

Consider the ffg;

* Infrastructure Complexity - Most CMs require a minmum  hierarchy of controller machine and a node to be managed by it. Eg in Puppet, agent app installed on each node, and master application to be installed on controller machine. Ansi uses a decentralized structure, but relies on SSH to exe provisioning tasks
...

## Configuration Management 101: Writing Puppet Manifests

$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet

