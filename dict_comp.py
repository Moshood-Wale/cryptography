
def dict_comp(stop, step):
  
  get_list = list(range(1, stop+1))

  output = [get_list [i:i+ step]for i in range(0,len(get_list),step)]
  
  if len(output[-1]) != step:    
      output.pop()

  key=[f'item-{i}'for i in range(1,len(output)+1)]

  my_dict={k:v for (k,v)in zip(key,output)}
  
  print (my_dict)


dict_comp(10, 4)

