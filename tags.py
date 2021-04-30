from math import log2
from collections import defaultdict
inf=float('inf')
def get_tags(cache_size=-1,block_size=-1,address=-1,n_way_associative=inf):
    dict=defaultdict(int)
    blocks=cache_size/block_size
    block_offset=log2(block_size)
    if n_way_associative==inf:
        no_of_sets=1
        n_way_associative=blocks
        dict['n way associative']='fully associative'
    else:
        no_of_sets=blocks/n_way_associative
    if n_way_associative==1:
        dict['n way associative']='directly mapped'
    else:
        dict['n way associative']=n_way_associative
    index=log2(no_of_sets)
    tag_bits=address-index-block_offset
    dict["Blocks"] = blocks
    dict["block_offset"]=block_offset
    dict["no of sets"]=no_of_sets
    dict["index"]=index
    dict["tag bits"]=tag_bits

    return dict;
# n way associative inf for fully associative
# n way associative 1 for direct mapped
# 2 4 8 for other sets as per requirement
print(get_tags(128*1024,64,40,inf))
print(get_tags(128*1024,64,40,2))

