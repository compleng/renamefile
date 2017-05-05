#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 
from os import rename

mypath="/home/compleng/Masaüstü/music/"

onlyfiles =os.listdir(mypath)

for filename in onlyfiles:
   if filename.startswith("WWW.IZLEVIDEO.NET-"):
        rename(os.path.join(mypath, filename), os.path.join(mypath, filename[18:]))

	


