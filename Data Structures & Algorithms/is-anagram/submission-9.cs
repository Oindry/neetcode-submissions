class Solution {
    public bool IsAnagram(string s, string t) {
        
    if (s.Length != t.Length) 
        {
            return false;
        }
    else
    {
       Dictionary<char,int> s_Letter= new Dictionary<char,int>();
       Dictionary<char,int> t_Letter= new Dictionary<char,int>();
       //List<char> processedLetter= new List<char>();
       foreach (char c in s)
       {
            
            if(t.Contains(c))
            {
               if(!s_Letter.ContainsKey(c))
                {
                    
                    s_Letter[c]=1;
                }
                else
                {
                    s_Letter[c]++;
                }  
            }
            else 
            {
                return false;
            }
            
       }
       foreach (char c in t)
       {
            
            if(s.Contains(c))
            {

               if(!t_Letter.ContainsKey(c))
                {
                    
                    t_Letter[c]=1;
                }
                else
                {
                    t_Letter[c]++;
                }  
            }
            else 
            {
                return false;
            }
            
       }
       List<bool> b= new List<bool>();
       foreach(var key in s_Letter.Keys) 
       {
            if (!t_Letter.ContainsKey(key) || t_Letter[key] != s_Letter[key]) {
                return false;
            }
            
       }

       return true;

       
    }
    }
}
