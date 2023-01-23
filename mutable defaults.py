def add_names_to_agg_list(names, aggregate_list=[]):
    for name in names:
        aggregate_list.append(name)
    return aggregate_list

def add_names_to_agg_list_proper(names, aggregate_list=None):
    if isinstance(aggregate_list, type(None)):
        aggregate_list = []
    for name in names:
        aggregate_list.append(name)
    return aggregate_list

print(add_names_to_agg_list(['John', 'Mary', '6ix9ine']))
print(add_names_to_agg_list(['John', 'Mary', '6ix9ine']))
    #The problem with the first statement is that the mutable type will only ever get init ONCE, this means that that pointer will get called back to itself and cause some funky results
print(add_names_to_agg_list_proper(['John', 'Mary', '6ix9ine']))
print(add_names_to_agg_list_proper(['John', 'Mary', '6ix9ine']))
    #Since the list is mutable (and is therefore only called once and can't be reinit), we're going to set it as a type of none in order to reinit this as a blank list

#This issue doesn't happen alot... Reallythis only happens to mutable types, so we won't see this with floats, ints, etc (nonmutables). But if we do see things like this happen this can cause HUGE headaches that are very hard to diagnose down the road