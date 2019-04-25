#!/usr/bin/env python
import sys
import os
import hashlib

#reads file by chunks
def chunk_reader(fobj, chunk_size=1024):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

#function to get hash of a filename
def get_hash(filename, first_chunk_only=False, hash=hashlib.sha1):
    hashobj = hash()
    file_object = open(filename, 'rb')

    if first_chunk_only:
        hashobj.update(file_object.read(1024))
    else:
        for chunk in chunk_reader(file_object):
            hashobj.update(chunk)
    hashed = hashobj.digest()

    file_object.close()
    return hashed

#main function
#paths is an array of paths
def check_for_duplicates(paths, hash=hashlib.sha1):
    hashes_by_size = {} #stores file duplicates by size
    hashes_on_1k = {} # if dup by size is found store hash of first mb 
    hashes_full = {} # if 1mb hash is dup then take full hash dups will be chosen and removed from here
    total_size=0
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                try:
                    file_size = os.path.getsize(full_path) #getting the file_size
                except (OSError,):
                    # not accessible (permissions, etc) - pass on
                    pass

                duplicate = hashes_by_size.get(file_size) #if any file with same size exists get its path(value) on file_size(keyz)

                if duplicate:
                    hashes_by_size[file_size].append(full_path)
                else:
                    hashes_by_size[file_size] = []  # create the list for this file size
                    hashes_by_size[file_size].append(full_path)

    # For all files with the same file size, get their hash on the 1st 1024 bytes
    for __, files in hashes_by_size.items():
        if len(files) < 2:
            continue    # this file size is unique, no need to spend cpy cycles on it

        for filename in files:
            small_hash = get_hash(filename, first_chunk_only=True)

            duplicate = hashes_on_1k.get(small_hash)
            if duplicate:                               #if some of the files are already iterated
                hashes_on_1k[small_hash].append(filename)
            else:                                       #if first file is iterated
                hashes_on_1k[small_hash] = []          # create the list for this 1k hash
                hashes_on_1k[small_hash].append(filename)

    # For all files with the hash on the 1st 1024 bytes, get their hash on the full file - collisions will be duplicates
    for __, files in hashes_on_1k.items():
        if len(files) < 2:
            continue    # this hash of fist 1k file bytes is unique, no need to spend cpy cycles on it

        for filename in files:
            full_hash = get_hash(filename, first_chunk_only=False)

            duplicate = hashes_full.get(full_hash)
            if duplicate:
                print "\n Duplicate found: \n %s  \n and \n %s" % (filename, duplicate)
                print str(os.path.getsize(filename)/1024) + 'KB' 
                total_size+=os.path.getsize(filename)/1024
                os.unlink(filename)
                
                #add details of the deleted file to stats
            else:
                hashes_full[full_hash] = filename
    print "\n Total file size removed : " +   str(total_size/1024) + 'mb (approx)'

#/Users/gauravsingh/Pictures
if sys.argv[1:]:
    check_for_duplicates(sys.argv[1:])
else:
    print "\n Please pass the paths to check as parameters to the script \n"