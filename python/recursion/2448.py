import sys
input=sys.stdin.readline
#print(len("            "))
a='''
                       *                        
                      * *                       
                     *****                      
                    *     *                     
                   * *   * *                    
                  ***** *****                   
                 *           *                  
                * *         * *                 
               *****       *****                
              *     *     *     *               
             * *   * *   * *   * *              
            ***** ***** ***** *****             
           *                       *            
          * *                     * *           
         *****                   *****          
        *     *                 *     *         
       * *   * *               * *   * *        
      ***** *****             ***** *****       
     *           *           *           *      
    * *         * *         * *         * *     
   *****       *****       *****       *****    
  *     *     *     *     *     *     *     *   
 * *   * *   * *   * *   * *   * *   * *   * *  
***** ***** ***** ***** ***** ***** ***** *****
'''

b='''
                       *                        
                      * *                       
                     *****                      
                    *     *                     
                   * *   * *                    
                  ***** *****                   
                 *           *                  
                * *         * *                 
               *****       *****                
              *     *     *     *               
             * *   * *   * *   * *              
            ***** ***** ***** *****             
           *                       *            
          * *                     * *           
         *****                   *****          
        *     *                 *     *         
       * *   * *               * *   * *        
      ***** *****             ***** *****       
     *           *           *           *      
    * *         * *         * *         * *     
   *****       *****       *****       *****    
  *     *     *     *     *     *     *     *   
 * *   * *   * *   * *   * *   * *   * *   * *  
***** ***** ***** ***** ***** ***** ***** *****
'''
#print(a==b)
n=int(input())
map=[[" " for i in range(n*2)] for i in range(n)]
standard=["  *   "," * *  ","***** "]

def rec(cut,startX,startY):
    if cut==3:
        for i in range(3):
            for j in range(6):
                map[startY+i][startX+j]=standard[i][j]
        return

    rec(cut//2,startX+cut//2,startY)
    rec(cut//2,startX,startY+cut//2)
    rec(cut//2,startX+cut,startY+cut//2)

rec(n,0,0)
for i in map:
    print("".join(i[:n*2-1]))
'''

x n*2-1
y n
'''