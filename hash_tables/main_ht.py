from .structs.hash_table import HashTable
import hash_tables.structs.hash_table as _ht_
import random 
import  time

mode = 2

N_ITEMS = 100

pht = {}

if mode == 0: 
    ht = HashTable(2)
if mode == 1: 
    ht = HashTable(HashTable.init_cap(N_ITEMS))
elif mode == 2:
    ht = HashTable(
        HashTable.init_cap(N_ITEMS), 
        resolution_mode=_ht_.QUADRATIC_PROBING_RESOLUTION, 
        hash_fn_a=_ht_.DIVISION_METHOD
    )

print(HashTable.init_cap(100000))

for i in range(N_ITEMS):
    ht.insert_item(i, i)
    pht[i] = i

ht.display()
