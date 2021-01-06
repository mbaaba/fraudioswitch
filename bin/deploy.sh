#!/bin/bash

#this has ti run within the rshell
#we have to be in the project-troot
rsync src/ /pyboard/ ; repl ~ import machine ~ machine.reset()