import sum_module #importing my module
#Because import all of them here other imports just for understanding


print(sum_module.sum(5,6)) #sum functions in my module



from sum_module import sum

print(sum(6,5)) #because just import sum I dont have to say sum_module.sum()
#BUT cant use other things in module


import sum_module as s #import but instead of sum_module I will say just s

print(s.nums) 


from sum_module import * #import all of them but I dont want to write sum_module all time

print(nums) 