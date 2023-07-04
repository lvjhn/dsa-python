from .structs.hash_table import HashTable
import hash_tables.structs.hash_table as _ht

test_matrix = {
    "resolution_mode" : [
        _ht.CHAINING_RESOLUTION, 
        _ht.LINEAR_PROBING_RESOLUTION, 
        _ht.QUADRATIC_PROBING_RESOLUTION, 
    ], 
    "hash_fn_a" : [
        _ht.DIVISION_METHOD, 
        _ht.MULTIPLICATION_METHOD
    ], 
    "hash_fn_b" : [
        _ht.DIVISION_METHOD, 
        _ht.MULTIPLICATION_METHOD
    ]
}

names = [
    None, 
    "CHAINING", 
    "LIN_PROBE", 
    "QUAD_PROBE", 
    "DIV", 
    "MULT"
]

def hash_table_demo(ht, type_): 
    print(f"# DEMO OF HASH-TABLE ({type_}) #")

    # display heap size
    print(f"> Heap Size: {ht.size()}") 
    print()
    assert(ht.size() == 0)

    # set 5 items 
    print(f"> Setting 5 items...")
    keys = [1, 2, 3, 4, 5]
    values = [10, 20, 30, 40, 50]
    for i in range(len(keys)):
        ht.set_item(keys[i], values[i])
    print()
    assert(ht.size() == 5)

    # print keys 
    print(f"> Keys: {list(ht.keys())}")
    print(f"> Values: {list(ht.values())}")
    
    for i in range(len(keys)): 
        key = keys[i] 
        value = values[i] 
        assert(key in ht.keys())
        assert(value in ht.values())

    # update key 1 and 5 (add 10) 
    print(f"> Updating items '1' and '5")
    print(f"> Item '1': {ht.get_item(1)}")
    print(f"> Item '5': {ht.get_item(5)}")
    print(f"> Updating...")
    ht.set_item(1, ht.get_item(1) + 10)
    ht.set_item(5, ht.get_item(5) + 10)
    print(f"> Item '1': {ht.get_item(1)}")
    print(f"> Item '5': {ht.get_item(5)}")

    # delete key 3 
    print()
    print(f"> Deleting key 3")  
    ht.remove_item(3) 
    print(f"> Keys: {list(ht.keys())}")
    assert(3 not in ht.keys()) 
    assert(30 not in ht.values())

    print("=========================================================")

for rm in test_matrix["resolution_mode"]: 
    for hfa in test_matrix["hash_fn_a"]: 
        for hfb in test_matrix["hash_fn_b"]: 
            ht = HashTable(
                resolution_mode=rm, 
                hash_fn_a=hfa, 
                hash_fn_b=hfb
            )
            hash_table_demo(
                ht, f"{names[rm]}-{names[hfa]}-{names[hfb]}"
            )