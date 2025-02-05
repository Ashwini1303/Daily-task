'''
The pattern has two parts – both mirror reflections of each other. The base of the triangle has to be at the bottom of the imaginary mirror and the tip at the top.

Illustration:
Input: size = 7
Output:

      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
 * * * * * * 
* * * * * * * 
* * * * * * * 
 * * * * * * 
  * * * * * 
   * * * * 
    * * * 
     * * 
      *      
'''

size = int(input("Enter size: "))  

for i in range(1, size + 1):
    print(" " * (size - i) + "* " * i)

for i in range(size, 0, -1):
    print(" " * (size - i) + "* " * i)
