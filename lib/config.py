#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# UNATTENDED FFMPEG ENCODER
# https://github.com/supermasita/ufe
# 

# Core root
core_root = "/var/www/ufe/"
# Absolute path to folder where original videos are copied
original = "/var/www/ufe/video_original/"
# Absolute path to folder where encoded videos are created
encoded = "/var/www/ufe/video_encoded/"
# Absolute path to temporal folder (no trailing slash)
tmppath = "/var/tmp"

# Tolerance from last access to a video in video_origin
# Used by "ufe-add" to determine if video can be added for encoding
timedif_to = 10

# This host's name in db table "servers"
server_name = "encoder01"

# DB credentials
db_host = "127.0.0.1"
db_user = "ufe"
db_pass = "ufe"
db_database = "ufe"

# Absolute name of binaries
ffmpeg_bin = "/opt/local/bin/ffmpeg"

# Create JSON? (True or False)
create_video_json = True
